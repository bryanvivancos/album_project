from album_project.model.Items import Items
from .SupabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()

async def items_api() -> list[Items]:
    return SUPABASE_API.select_items()

async def input_api(title: str, description: str) -> list[Items]:
    return SUPABASE_API.insert_items(title, description)
   

async def delete_api(id: int):
    #print(id)
    return SUPABASE_API.delete_item(id)