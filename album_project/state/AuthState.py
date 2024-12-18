import reflex as rx 
from ..api.SupabaseAPI import SupabaseAPI

supabase_client = SupabaseAPI().supabase

class AuthState(rx.State):

    which_dialog_open: str= ""

    user_email: str= ""
    password: str= ""
    is_authenticated: bool= False
    error_message: str= ""

    async def login(self, email: str, password: str):
        """Inicia sesion en Supabase"""
        try:
            login_response= supabase_client.auth.sign_in_with_password({"email": email, "password": password})
            
            if login_response.user is None:
                self.error_message = "Invalid email or password"
                self.is_authenticated= False
            else:
                self.user_email= email
                self.is_authenticated= True
        except Exception as e:
            self.error_message= str(e)


    
    async def signup(self, email: str, password: str):
        """Registro de un nuevo usuario en Supabase"""
        try:
            sign_response= supabase_client.auth.sign_up({"email": email,"password": password})
            
            if sign_response.user is None:
                self.error_message = "Insert valid parameters"
            else:
                self.error_message = "Registration successful! Check your email."
                self.is_authenticated= True
        except Exception as e:
            self.error_message = str(e)
            
            
    
    async def logout(self):
        """Cierra sesión del usuario."""
        supabase_client.auth.sign_out()
        self.is_authenticated = False
        self.user_email = ""