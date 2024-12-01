import reflex as rx
import datetime
import os
import dotenv
import re
from album_project.api.api import items_api, input_api, delete_api,update_api
from album_project.model.Items import Items


class PageState(rx.State):
    
    dotenv.load_dotenv()
    USER_KEY=  os.environ.get("USER_KEY")
    PASS_KEY= os.environ.get("PASS_KEY")
    
    login_state: bool  #para identificar si el usuario esta logueado o no

## Login vars
    loader: bool= False
    username: str #= "ejemplo@mail.com"
    password: str
    error= False
    #response: dict= {}

## CRUD vars
    items_info: list[Items]
    form_data: dict= {} #para agregar datos desde el formulario
    item_id: int #captura id de elemento


### METODO PARA LOGIN
    async def loginService(self, login_data: dict):
        self.loader= True
        self.error= False
        #response= rq.post("http: //localhost: 8000/auth/login", json= login_data, headers= {"Content-Type": "application/json"})
        response= 200

        print(self.username, self.password)
        
        # if response== 200:
        #     #self.response.json()
        #     self.loader= False
        #     #return True

        #     self.login_state= True

        if self.username== self.USER_KEY and self.password== self.PASS_KEY:
            self.loader= False
            self.login_state= True
        else: 
            self.loader= False
            self.error= True

            self.login_state= False  
            
        self.USER_KEY= ""
        self.PASS_KEY= ""


    # @rx.var
    # def user_invalid(self) -> bool:
    #     return not (re.match(r"[^@]+@[^@]+.[^@]+", self.username) and "ejemplo@mail.com")

    @rx.var
    def user_empty(self) -> bool:
        return not self.username.strip()
    
    @rx.var
    def password_empty(self) -> bool:
        return not (self.password.strip())
    
    @rx.var
    def validate_fields(self) -> bool:
        return (
            self.user_empty
            #or self.user_invalid
            or self.password_empty
        )



#### METODOS DEL CRUD
    
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