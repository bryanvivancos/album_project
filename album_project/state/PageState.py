import reflex as rx
from album_project.api.api import items_api
from album_project.model.Items import Items

class PageState(rx.State):
    
    items_info: list[Items]
    
    async def items_grid(self):
        data = await items_api()
        print(data)
        self.items_info = await items_api()