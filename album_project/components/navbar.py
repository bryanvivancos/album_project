import reflex as rx 
import album_project.styles.styles as styles
from album_project.styles.colors import Color

def navbar() -> rx.Component:
    return rx.box(
        bg_color= Color.SECONDARY.value,
        height= "40px",
        z_index = "999",
        width= "100%",
        top= "0",
    )