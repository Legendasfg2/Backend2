import asyncio
import aiohttp
import os
from aiofiles import open as aio_open
from tabulate import tabulate


async def download_image(session, url, save_dir, results):
    filename = os.path.join(save_dir, url.split("/")[-1])
    try:
        async with session.get(url) as resp:
            if resp.status == 200:
                async with aio_open(filename, "wb") as f:
                    await f.write(await resp.read())
                results.append((url, "Успех"))
            else:
                results.append((url, f"Ошибка ({resp.status})"))
    except Exception as e:
        results.append((url, f"Ошибка ({e.__class__.__name__})"))


async def main():
    # Проверка пути
    while True:
        print("Введите путь для сохранения изображений:", flush=True)
        save_dir = input().strip()
        if os.path.isdir(save_dir) and os.access(save_dir, os.W_OK):
            break
        print("❌ Некорректный путь или нет доступа. Попробуйте снова.", flush=True)

    # Сбор ссылок
    urls = []
    print("Введите ссылки на изображения (пустая строка для завершения):", flush=True)
    while True:
        link = input().strip()
        if not link:
            break
        urls.append(link)

    if not urls:
        print("⚠️  Ссылки не введены. Завершение.", flush=True)
        return

    results = []
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url, save_dir, results) for url in urls]
        await asyncio.gather(*tasks)

    # Вывод итоговой таблицы
    print("\nСводка об успешных и неуспешных загрузках:\n", flush=True)
    print(tabulate(results, headers=["Ссылка", "Статус"], tablefmt="grid"), flush=True)


if __name__ == "__main__":
    asyncio.run(main())
