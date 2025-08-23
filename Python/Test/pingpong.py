# pingpong.py
import sys
import pygame
from pygame.locals import K_w, K_s, K_UP, K_DOWN, K_ESCAPE, QUIT

# -----------------------------
# Настройки игры
# -----------------------------
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 12, 100
BALL_SIZE = 14

PADDLE_SPEED = 7.0  # скорость ракеток (px/кадр)
BALL_SPEED_X = 5.0  # стартовая скорость мяча по X (px/кадр)
BALL_SPEED_Y = 4.0  # стартовая скорость мяча по Y (px/кадр)

SCORE_TO_WIN = 10

BG_COLOR = (16, 18, 24)
FG_COLOR = (240, 240, 240)
NET_COLOR = (90, 90, 90)


# -----------------------------
# Вспомогательные функции
# -----------------------------
def reset_ball(to_left=True):
    ball_x = WIDTH / 2.0
    ball_y = HEIGHT / 2.0
    vx = -BALL_SPEED_X if to_left else BALL_SPEED_X
    vy = BALL_SPEED_Y
    return ball_x, ball_y, vx, vy


def draw_center_net(surface):
    segment_h = 12
    gap = 10
    x = WIDTH // 2 - 1
    y = 0
    while y < HEIGHT:
        pygame.draw.rect(surface, NET_COLOR, (x, y, 2, segment_h))
        y += segment_h + gap


# -----------------------------
# Основная игра
# -----------------------------
def main():
    pygame.init()
    pygame.display.set_caption("Ping Pong — 2 Players (W/S vs ↑/↓)")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 28, bold=True)
    big_font = pygame.font.SysFont("Arial", 48, bold=True)

    # Ракетки
    left_paddle = pygame.Rect(
        40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT
    )
    right_paddle = pygame.Rect(
        WIDTH - 40 - PADDLE_WIDTH,
        HEIGHT // 2 - PADDLE_HEIGHT // 2,
        PADDLE_WIDTH,
        PADDLE_HEIGHT,
    )

    # Мяч
    ball_rect = pygame.Rect(0, 0, BALL_SIZE, BALL_SIZE)
    ball_x, ball_y, ball_vx, ball_vy = reset_ball(to_left=True)
    ball_rect.center = (int(ball_x), int(ball_y))

    score_left = 0
    score_right = 0

    running = True
    paused_after_score = False
    pause_timer_ms = 0

    while running:
        dt_ms = clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()

        # Управление левым игроком (W/S)
        if keys[K_w]:
            left_paddle.y -= int(PADDLE_SPEED)
        if keys[K_s]:
            left_paddle.y += int(PADDLE_SPEED)

        # Управление правым игроком (стрелки ↑/↓)
        if keys[K_UP]:
            right_paddle.y -= int(PADDLE_SPEED)
        if keys[K_DOWN]:
            right_paddle.y += int(PADDLE_SPEED)

        # Ограничения по экрану
        left_paddle.top = max(0, left_paddle.top)
        left_paddle.bottom = min(HEIGHT, left_paddle.bottom)

        right_paddle.top = max(0, right_paddle.top)
        right_paddle.bottom = min(HEIGHT, right_paddle.bottom)

        # Логика мяча
        if paused_after_score:
            pause_timer_ms -= dt_ms
            if pause_timer_ms <= 0:
                paused_after_score = False
        else:
            ball_x += ball_vx
            ball_y += ball_vy
            ball_rect.center = (int(ball_x), int(ball_y))

            # Отскоки от верх/низ
            if ball_rect.top <= 0:
                ball_rect.top = 0
                ball_y = ball_rect.centery
                ball_vy = -ball_vy
            elif ball_rect.bottom >= HEIGHT:
                ball_rect.bottom = HEIGHT
                ball_y = ball_rect.centery
                ball_vy = -ball_vy

            # Столкновение с левой ракеткой
            if ball_rect.colliderect(left_paddle) and ball_vx < 0:
                ball_rect.left = left_paddle.right
                ball_x = ball_rect.centerx
                offset = (ball_rect.centery - left_paddle.centery) / (
                    PADDLE_HEIGHT / 2.0
                )
                ball_vx = -ball_vx
                ball_vy = max(-7.0, min(7.0, BALL_SPEED_Y * offset * 1.5))

            # Столкновение с правой ракеткой
            if ball_rect.colliderect(right_paddle) and ball_vx > 0:
                ball_rect.right = right_paddle.left
                ball_x = ball_rect.centerx
                offset = (ball_rect.centery - right_paddle.centery) / (
                    PADDLE_HEIGHT / 2.0
                )
                ball_vx = -ball_vx
                ball_vy = max(-7.0, min(7.0, BALL_SPEED_Y * offset * 1.5))

            # Голы
            if ball_rect.right < 0:
                score_right += 1
                ball_x, ball_y, ball_vx, ball_vy = reset_ball(to_left=True)
                ball_rect.center = (int(ball_x), int(ball_y))
                paused_after_score = True
                pause_timer_ms = 900

            elif ball_rect.left > WIDTH:
                score_left += 1
                ball_x, ball_y, ball_vx, ball_vy = reset_ball(to_left=False)
                ball_rect.center = (int(ball_x), int(ball_y))
                paused_after_score = True
                pause_timer_ms = 900

        # Рендеринг
        screen.fill(BG_COLOR)
        draw_center_net(screen)

        # Ракетки и мяч
        pygame.draw.rect(screen, FG_COLOR, left_paddle, border_radius=4)
        pygame.draw.rect(screen, FG_COLOR, right_paddle, border_radius=4)
        pygame.draw.ellipse(screen, FG_COLOR, ball_rect)

        # Счёт
        score_text = font.render(f"{score_left} : {score_right}", True, FG_COLOR)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

        # Подсказки
        help_left = font.render("Left: W/S", True, (180, 180, 180))
        help_right = font.render("Right: ↑ / ↓", True, (180, 180, 180))
        screen.blit(help_left, (20, 10))
        screen.blit(help_right, (WIDTH - help_right.get_width() - 20, 10))

        # Проверка победы
        if score_left >= SCORE_TO_WIN or score_right >= SCORE_TO_WIN:
            winner = "Left" if score_left > score_right else "Right"
            win_text = big_font.render(f"{winner} Player Wins!", True, FG_COLOR)
            sub_text = font.render("Press ESC to quit", True, (200, 200, 200))
            screen.blit(
                win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - 40)
            )
            screen.blit(
                sub_text, (WIDTH // 2 - sub_text.get_width() // 2, HEIGHT // 2 + 20)
            )
            paused_after_score = True
            ball_vx = 0.0
            ball_vy = 0.0

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
