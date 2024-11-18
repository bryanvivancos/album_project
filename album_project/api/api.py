from album_project.model.Items import Items
from .SupabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()

async def items_api() -> list[Items]:
    return SUPABASE_API.select_items()


async def input_api(title: str, description: str) -> list[Items]:
    return SUPABASE_API.insert_item(title, description)
   

async def delete_api(item_id: int):
    #print(item_id)
    return SUPABASE_API.delete_item(item_id)


async def update_api(item_id: int, title: str, description: str) -> list[Items]:
    return SUPABASE_API.update_item(title, description, item_id)