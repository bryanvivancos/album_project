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

    def insert_items(self, title: str, description: str) -> dict:

        date=  datetime.date.today()
        data= {"title": title, "description": description, "creation_date": date.isoformat()}
        response= self.supabase.table("items").insert(data).execute()

        message: dict= {}

        if response.data:
            message= {"message": "Item inserted sucessfully", "form_data": data}
            return message
        else:
            message= {"message": "Failed to insert item", "error": response.error}
            return message
        

    ####################################################
    def delete_item(self, item_id: int):
        print(item_id)

        data= {"id": item_id}
        print(data)
        response= self.supabase.table("items").delete().eq("id",item_id).execute()

        if response.data:
            return {"message": "Item deleted successfully"}
        else:
            return {"message": "Failed to delete item", "error": response.error}
