import aiohttp
import aiofiles
import asyncio
import os

os.chdir(os.path.dirname(__file__))


async def save_image(session: aiohttp.ClientSession, url: str, directory: str) -> None:
    async with session.get(url) as resp:
        if resp.status == 200:
            img_data = await resp.read()
            img_name = os.path.join(directory, os.path.basename(url))

            async with aiofiles.open(img_name, 'wb') as file:
                await file.write(img_data)
            print(f"Зображення збережено: {img_name}")

        else:
            print(f"Не вдалося завантажити зображення з: {url}")


async def retrieve_dog_images(count: int, directory: str) -> None:
    api_url = 'https://dog.ceo/api/breeds/image/random'

    async with aiohttp.ClientSession() as session:
        for _ in range(count):
            async with session.get(api_url) as resp:
                if resp.status == 200:
                    response_data = await resp.json()
                    img_url = response_data.get('message')
                    await save_image(session, img_url, directory)
                else:
                    print(f"Не вдалося отримати URL-адресу зображення з: {api_url}")


async def main():
    directory = 'dog_pictures'
    count = 15

    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        await retrieve_dog_images(count, directory)
    except Exception as error:
        print(f"Сталася помилка: {error}")

if __name__ == "__main__":
    asyncio.run(main())
