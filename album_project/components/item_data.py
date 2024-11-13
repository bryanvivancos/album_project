import reflex as rx 
from album_project.model.Items import Items
from album_project.styles.styles import Color
from album_project.styles.styles import Size
import album_project.styles.styles as styles

def item_data(data: Items) -> rx.Component:
    return rx.link(
        rx.box(
            # rx.image(
            #     src= data.image,
            #     width="100%",
            #     height="auto",
            #     alt=f"Imagen destacada para: {data.title}",
            # ),
            rx.text(
                data.title,
                size= "1px",
            ),
            rx.text(
                data.description,
                size= "1px",
            ),
            style= styles.item_data_style,
            padding= Size.MEDIUM.value,
        ),
        href="#",
        style= styles.link_style,
    )

