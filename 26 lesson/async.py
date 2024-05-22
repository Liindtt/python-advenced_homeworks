from time import perf_counter
import asyncio


async def take_order(order_id):
    print(f"Taking order {order_id}...")
    await asyncio.sleep(2)  # Прийом замовлення займає 2 хвилини
    print(f"Order {order_id} taken!")


async def make_coffee(order_id):
    print(f"Making coffee for order {order_id}...")
    await asyncio.sleep(3)    # Приготування кави займає 3 хвилини
    print(f"Coffee for order {order_id} is ready!")


async def make_sandwich(order_id):
    print(f"Making sandwich for order {order_id}...")
    await asyncio.sleep(4)  # Приготування сендвіча займає 4 хвилини
    print(f"Sandwich for order {order_id} is ready!")


async def serve_order(order_id):
    print(f"Serving order {order_id}...")
    await asyncio.sleep(1)  # Подача замовлення займає 1 хвилину
    print(f"Order {order_id} served!")


async def process_order(order_id):
    await take_order(order_id)
    await make_coffee(order_id)
    await make_sandwich(order_id)
    await serve_order(order_id)


async def main():
    start_time = perf_counter()
    orders = [1, 2, 3]
    async_orders = await asyncio.gather(process_order(orders[0]), process_order(orders[1]), process_order(orders[2]))
    print("All orders have been processed!")
    print(f"Program ends in: {perf_counter() - start_time:.2f} seconds")

# Запускаємо асинхронний процес обслуговування клієнтів
asyncio.run(main())
