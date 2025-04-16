import anyio

from beautifulapp import MainApp

app = MainApp()

anyio.run(app.async_run)
