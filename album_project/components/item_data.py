import reflex as rx 
from album_project.model.Items import Items
from album_project.styles.styles import Color
from album_project.styles.styles import Size

def item_data(data: Items) -> rx.Component:
    return rx.vstack(
        rx.text(
            data.title,
            size= "1px",
        ),
        rx.text(
            data.date
        ),
        rx.image(
            src= data.image,
            width="100%",
            height="auto",
            alt=f"Imagen destacada para: {data.title}",
        ),
    )

