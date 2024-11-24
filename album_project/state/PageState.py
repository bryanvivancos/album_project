import reflex as rx
import datetime
from album_project.api.api import items_api, input_api, delete_api,update_api
from album_project.model.Items import Items


class PageState(rx.State):
    
    items_info: list[Items]

    form_data: dict= {} #para agregar datos desde el formulario
    item_id: int #captura id de elemento


    ### LLAMADA DE DATOS AL CARGAR LA PAGINA
    async def items_grid(self):
        # data = await items_api()
        # print(data)
        self.items_info = await items_api()


    ### INGRESO DE DATOS A LA BASE
    @rx.event
    async def handle_submit(self,form_data):
        submit_response= await input_api(form_data['title'], form_data['description'])  #agrega datos desde el formulario
        
        if submit_response.get('message'): #devuelve un mensaje al momento de ejecutar el evento
            return rx.toast.success(submit_response['message'])
        else:
            return rx.toast.error(submit_response['message'])
        

    ### ELIMINACION DE ELEMENTOS DE LA BASE
    @rx.event
    async def delete_button(self, item_id):
        delete_response= await delete_api(item_id)
        
        if delete_response.get('message'): #devuelve un mensaje al momento de ejecutar el evento
            return rx.toast.success(delete_response['message'])
        else:
            return rx.toast.error(delete_response['message'])


    ### ACTUALIZACION DE ELEMENTOS DE LA BASE
    @rx.event
    def item_id_update(self,id_item: int):
        self.item_id = id_item #actualiza valor al id del elemento seleccionado
    
    @rx.event
    async def update_button(self,form_data): #devuelve un mensaje al momento de ejecutar el evento
        #print(form_data, self.item_id)
        update_response= await update_api(form_data['title'], form_data['description'], self.item_id)
        
        if update_response.get('message'):
            return rx.toast.success(update_response['message'])
        else:
            return rx.toast.error(update_response['message'])