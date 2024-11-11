import os
import dotenv
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
    
    def items(self) -> list[Items]:
        
        response = self.supabase.table("items").select("*").execute()
        
        items_data = []
        
        if len(response.data) > 0:
            for items_item in response.data:
                items_data.append(
                    Items(
                        title=items_item["title"], 
                        date= items_item["creation_date"],
                        image= items_item["image"],
                        )
                    )
        
        return items_data, len(response.data)