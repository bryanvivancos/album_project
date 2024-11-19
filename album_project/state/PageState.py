import reflex as rx
import datetime
from album_project.api.api import items_api, input_api, delete_api,update_api
from album_project.model.Items import Items


class PageState(rx.State):
    
    items_info: list[Items]

    #form_data: dict= {} #para agregar datos desde el formulario
    #title_input: str #para agregar elementos individualmente
    #description_input: str #para agregar elementos individualmente

    #item_id: int para delete button

    ### LLAMADA DE DATOS AL CARGAR LA PAGINA
    async def items_grid(self):
        # data = await items_api()
        # print(data)
        self.items_info = await items_api()


    ### INGRESO DE DATOS A LA BASE
    @rx.event
    async def handle_submit(self,form_data: dict):
        #print(self.title_input, self.description_input)
        #print(form_data['title'], form_data['description'], datetime.date.today())
        #await input_api(self.title_input, self.description_input) #agrega los datos individualmente
        await input_api(form_data['title'], form_data['description'])  #agrega datos desde el formulario
        

    ### ELIMINACION DE ELEMENTOS DE LA BASE
    @rx.event
    async def delete_button(self, item_id: int):
        # print(int(form_data["title"]), type(int(form_data["title"])))
        await delete_api(item_id)


    ### ACTUALIZACION DE ELEMENTOS DE LA BASE
    @rx.event
    async def update_button(self, form_data: dict):
        #await update_api(item_id, form_data['title'], form_data['description'])
        #print(self.title_input, self.description_input, item_id)
        print(form_data)
        #await update_api(self.title_input, self.description_input, item_id,)


    @rx.event
    def prueba(self,form_data: dict):
        print(form_data)


        