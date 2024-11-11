from album_project.model.Items import Items
from .SupabaseAPI import SupabaseAPI

SUPABASE_API = SupabaseAPI()

async def items_api() -> list[Items]:
    return SUPABASE_API.items()