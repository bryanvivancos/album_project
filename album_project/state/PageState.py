import reflex as rx
import datetime
from album_project.api.api import items_api, input_api, delete_api,update_api
from album_project.model.Items import Items


class PageState(rx.State):
    
    items_info: list[Items]

    form_data: dict= {} #para agregar datos desde el formulario
    # title_input: str #para agregar elementos individualmente
    # description_input: str #para agregar elementos individualmente

    item_id: int

    async def items_grid(self):
        # data = await items_api()
        # print(data)
        self.items_info = await items_api()

    @rx.event
    async def handle_submit(self,form_data):
        #print(form_data['title'], form_data['description'], datetime.date.today())
        await input_api(form_data['title'], form_data['description'])  #agrega datos desde el formulario
        #print(self.title_input, self.description_input)
        #await input_api(self.title_input, self.description_input) #agrega los datos individualmente
    
    @rx.event
    async def delete_button(self, item_id):
        # print(int(form_data["title"]), type(int(form_data["title"])))
        await delete_api(item_id)

    @rx.event
    async def update_button(self, item_id, form_data):
        #await update_api(self.title_input, self.description_input, item_id)
        print(item_id,form_data)
        await update_api(item_id, form_data['title'], form_data['description'])