import reflex as rx
import album_project.styles.styles as styles
from album_project.styles.styles import Size
from album_project.styles.colors import Color
from album_project.model.Items import Items
from album_project.components.item_data import item_data
from album_project.state.PageState import PageState
from album_project.components.title import title
from album_project.components.input_data import input_data
from album_project.views.menu_bar import menu_bar

def grid() -> rx.Component:
    return rx.vstack(
        rx.center(
            menu_bar(),
            width="100%",
            padding="2em"
        ),
        rx.divider(),
        rx.cond(
            PageState.items_info,
            rx.vstack(
                rx.grid(
                    rx.foreach(
                        PageState.items_info,
                        item_data, # Aplica `item_data` a cada `item`
                    ),
                    columns=rx.breakpoints(initial="1",sm="2",md="2",lg="4"),
                    spacing=Size.DEFAULT.value,
                ),
                spacing=Size.DEFAULT.value
            ),
            rx.text("No items found"),  # Muestra un mensaje si `items` está vacio
        ),
        bg_color=Color.SECONDARY.value,
        border_radius= Size.DEFAULT.value,
        padding= Size.DEFAULT.value,
    ),