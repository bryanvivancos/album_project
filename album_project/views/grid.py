import reflex as rx
import album_project.styles.styles as styles
from album_project.styles.styles import Size
from album_project.styles.colors import Color
from album_project.model.Items import Items
from album_project.components.item_data import item_data
from album_project.state.PageState import PageState
from album_project.components.title import title

def grid() -> rx.Component:
    return rx.vstack(
        rx.cond(
            PageState.items_info,
            rx.vstack(
                title("Items"),
                rx.flex(
                    rx.foreach(
                        PageState.items_info,
                        lambda item: item_data(item),  # Aplica `item_data` a cada `item`
                    ),
                    flex_direction=["column", "row"],
                ),
            ),
            rx.text("No items found"),  # Muestra un mensaje si `items` está vacío
        ),
        bg_color=Color.SECONDARY.value,
        border_radius= Size.DEFAULT.value,
        padding= Size.DEFAULT.value,
    ),
    
    
    # columns= rx.breakpoints(initial="1", sm="3", md="4"),
        # spacing="3",
        # align_items= "center",
        # justify_content= "center", 
        # width="100%",