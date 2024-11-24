import reflex as rx
from album_project.styles.styles import Size
from album_project.components.item_data import item_data
from album_project.state.PageState import PageState

def grid() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Boton que se utilizaba para refrescar y actualizar el grid de elementos
            # rx.center(
            #     rx.button("Refresh", 
            #         on_click= PageState.items_grid,
            #         ),
            #     width= "100%",
            # ),
            rx.cond(
                PageState.items_info,
                rx.vstack(
                    rx.grid(
                        rx.foreach(
                            PageState.items_info,
                            item_data, # Aplica `item_data` a cada `item`
                        ),
                        columns=rx.breakpoints(initial="1",xs="2", sm="2",md="3",lg="3"),
                        spacing= "2",
                        width= "100%",
                    ),
                    spacing= "2",
                    width= "100%",
                ),
                rx.center(
                    rx.text("No items found"),  # Muestra un mensaje si `items` está vacio
                    width= "100%",
                ),
            ),
            on_mount= PageState.items_grid,
            spacing= "2",
            width= "480px",
        ),
        width= "100%",
        padding_bottom= Size.DEFAULT.value, 
    )