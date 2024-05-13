from time import perf_counter
from PIL import Image
from urllib.request import urlopen, HTTPError
from concurrent.futures import ProcessPoolExecutor


def download_and_resize_image(url, num):
    MAX_SIZE = (200, 200)
    try:
        image = Image.open(urlopen(url))
    except HTTPError as e:
        print(f"Path №{num} is incorrect! {e}")
        return None
    else:
        image.thumbnail(MAX_SIZE)
        image.save(f"img/image-{num}.jpg")
        return f"Image {num} processed."


if __name__ == "__main__":
    img_urls = [
        'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
        'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
        'https://images.unsplash.com/photo-1524429656589-6633a470097c',
        'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
        'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
        'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
        'https://images.unsplash.com/photo-1522364723953-452d3431c267',
        'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
        'https://images.unsplash.com/photo-1507143550189-fed454f93097',
        'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
        'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
        'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
        'https://images.unsplash.com/photo-1516972810927-80185027ca84',
        'https://images.unsplash.com/photo-1550439062-609e1531270e',
        'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
    ]
    start_time = perf_counter()

    with ProcessPoolExecutor() as executor:  # Запускаємо 5 потоків для обробки
        futures = [executor.submit(download_and_resize_image, url, num) for num, url in enumerate(img_urls, start=1)]
        for future in futures:
            result = future.result()
            if result:
                print(result)

    print(f"Program end in {perf_counter() - start_time:.2f} seconds.")
