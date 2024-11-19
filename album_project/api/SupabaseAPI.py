import os
import dotenv
import datetime
import reflex as rx
from supabase import create_client, Client
from album_project.model.Items import Items

class SupabaseAPI:
    
    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    
    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )

    
    ### LLAMADA DE DATOS AL CARGAR LA PAGINA
    def select_items(self) -> list[Items]:
        
        response = self.supabase.table("items").select("*").execute()
        
        items_data = []
        
        if len(response.data) > 0:
            for items_item in response.data:
                items_data.append(
                    Items(
                        id= items_item["id"],
                        title=items_item["title"],
                        description= items_item["description"],
                        )
                    )
        return items_data


    ### INGRESO DE DATOS A LA BASE
    def insert_item(self, title: str, description: str) -> dict:

        date=  datetime.date.today()
        data= {"title": title.title(), "description": description, "creation_date": date.isoformat()}
        
        insert_response= self.supabase.table("items").insert(data).execute()

        message: dict= {}

        if insert_response.data:
            #message= {"message": "Item inserted sucessfully", "form_data": data}
            return rx.toast.success(
                    f"Item inserted sucessfully, 'form_data': {data}",
                    position="bottom-right",
                    )
        else:
            #message= {"message": "Failed to insert item", "error": insert_response.error}
            return rx.toast.error(
                    f"Failed to insert item, 'error': {insert_response.error}",
                    position="bottom-right",
                    )


    ### ELIMINACION DE ELEMENTOS DE LA BASE
    def delete_item(self, item_id: int):
        
        message: dict= {}
        #print(item_id)
        delete_response= self.supabase.table("items").delete().eq("id",item_id).execute()

        if delete_response.data:
            message= {"message": "Item deleted successfully"}
            # return {"message": "Item deleted successfully"}
            #return message
        else:
            message= {"message": "Failed to delete item", "error": delete_response.error}
            #return {"message": "Failed to delete item", "error": delete_response.error}
        
        return message
    

    ### ACTUALIZACION DE ELEMTNOS DE LA BASE
    def update_item(self, title: str, description: str, item_id: int) -> dict:

        data= {"title": title.title(), "description": description}

        update_response= self.supabase.table("items").update(data).eq("id",item_id).execute()

        if update_response.data:
            message= {"message": "Item upadted successfully"}
        else:
            message= {"message": "Failed to update item"}
        
        return message
