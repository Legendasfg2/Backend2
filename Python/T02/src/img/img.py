import asyncio
import aiohttp
import os
from tabulate import tabulate


async def download_image(session, url, save_dir, results):
    filename = os.path.join(save_dir, url.split("/")[-1])
    try:
        async with session.get(url) as resp:
            if resp.status == 200:
                content = await resp.read()
                with open(filename, "wb") as f:
                    f.write(content)
                results.append((url, "Успех"))
            else:
                results.append((url, f"Ошибка ({resp.status})"))
    except Exception as e:
        results.append((url, f"Ошибка ({e.__class__.__name__})"))


async def main():
    # Ввод всего сразу
    print("Введите путь для сохранения изображений:", flush=True)
    save_dir = input().strip()
    while not (os.path.isdir(save_dir) and os.access(save_dir, os.W_OK)):
        print("❌ Некорректный путь или нет доступа. Попробуйте снова:", flush=True)
        save_dir = input().strip()

    print("Введите ссылки (по одной в строке, пустая строка — конец):", flush=True)
    try:
        urls = []
        while True:
            line = input().strip()
            if not line:
                break
            urls.append(line)
    except EOFError:
        pass  # если пользователь завершил ввод Ctrl+D / Ctrl+Z

    if not urls:
        print("⚠️ Ссылки не введены. Завершение.", flush=True)
        return

    results = []
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url, save_dir, results) for url in urls]
        await asyncio.gather(*tasks)

    print("\nСводка об успешных и неуспешных загрузках:\n", flush=True)
    print(tabulate(results, headers=["Ссылка", "Статус"], tablefmt="grid"), flush=True)


if __name__ == "__main__":
    asyncio.run(main())
