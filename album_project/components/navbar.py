import reflex as rx 
from album_project.styles.colors import Color

def navbar() -> rx.Component:
    return rx.box(
        bg_color= Color.SECONDARY.value,
        height= "40px",
        width= "100%",
    )