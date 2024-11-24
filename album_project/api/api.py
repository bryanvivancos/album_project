from album_project.model.Items import Items
from .SupabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()


### LLAMADA DE DATOS AL CARGAR LA PAGINA
async def items_api() -> list[Items]:
    return SUPABASE_API.select_items()


### INGRESO DE DATOS A LA BASE
async def input_api(title: str, description: str) -> list[Items]:
    return SUPABASE_API.insert_item(title, description)


### ELIMINACION DE ELEMENTOS DE LA BASE
async def delete_api(item_id: int):
    #print(item_id)
    return SUPABASE_API.delete_item(item_id)


### ACTUALIZACION DE ELEMENTOS DE LA BASE
async def update_api(title: str, description: str, item_id: int) -> list[Items]:
    return SUPABASE_API.update_item(title, description, item_id)