import reflex as rx
import datetime
from album_project.api.api import items_api, input_api, delete_api
from album_project.model.Items import Items


class PageState(rx.State):
    
    form_data: dict= {}
    items_info: list[Items]
    input_title_value: str= ""
    


    async def items_grid(self):
        # data = await items_api()
        # print(data)
        self.items_info = await items_api()

    @rx.event
    async def handle_submit(self, form_data):
        #print(form_data['title'], form_data['description'], datetime.date.today())
        await input_api(form_data['title'], form_data['description'])
    

    ############################################
    @rx.event
    async def delete_button(self, form_data):
        print(int(form_data["title"]), type(int(form_data["title"])))
        await delete_api(int(form_data["title"]))
