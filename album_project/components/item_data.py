import reflex as rx 
import album_project.styles.styles as styles
from album_project.state.AuthState import AuthState
from album_project.styles.colors import TextColor 
from album_project.model.Items import Items
from album_project.styles.styles import Size
from album_project.components.item_trash_button import item_trash_button
from album_project.components.edit_item_button import edit_item_button

def item_data(data: Items) -> rx.Component:
    return rx.box(
        rx.box(
            # rx.image(
            #     src= data.image,
            #     width="100%",
            #     height="auto",
            #     alt=f"Imagen destacada para: {data.title}",
            # ),
            rx.text(
                data.title,
                size= "2",
            ),
            rx.text(
                data.description,
                size= "2",
            ),
            rx.hstack(
                rx.text(
                    data.id,
                    size= "2",
                    color= TextColor.FOOTER,
                ),
                rx.cond(
                    AuthState.is_authenticated,
                    rx.stack(
                        edit_item_button(data.id),
                        item_trash_button(data.title, data.id), #boton de papelera en cada item
                        spacing= "2",
                    ),
                ),
                justify= "between",
                align="end",
            ),
            style= styles.item_data_style,
            padding= Size.MEDIUM.value,
        ),
        # href="",
        # disable= True,
        style= styles.link_style,
    )

