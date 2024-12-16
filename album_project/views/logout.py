import reflex as rx 
import album_project.styles.styles as styles
from ..state.AuthState import AuthState

def logout() -> rx.Component:
    return rx.button(
                        rx.icon("door-open", size=16),
                        rx.text("Logout", size="4"),
                    )