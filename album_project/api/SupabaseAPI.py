import os
import dotenv
import datetime
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
                        title=items_item["title"],
                        description= items_item["description"],
                        )
                    )
        return items_data

    def insert_items(self, title: str, image: str) -> dict:

        data= {"title": title, "image": image, "creation_date": datetime.date.today()}
        response= self.supabase.table("items").insert(data).execute()

        if response.data:
            return {"message": "Item inserted sucessfully", "form_data": data}
        else:
            return {"message": "Failed to insert item", "error": response.error}