from aiohttp import web


async def handle_root(request):
    return web.Response(text="Hello, this is the root endpoint!")


async def handle_hello(request):
    name = request.rel_url.query.get('name', 'Anonymous')
    return web.Response(text=f"Hello, {name}!")

app = web.Application()
app.add_routes([web.get('/', handle_root)])
app.add_routes([web.get('/hello', handle_hello)])

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)

