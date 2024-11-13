import reflex as rx
from album_project.components.title import title
from album_project.components.input_data import input_data
from album_project.styles.styles import Size
from album_project.styles.colors import Color

def menu_bar() -> rx.Component:
    return rx.center(
        rx.stack(
            rx.accordion.root(
            rx.accordion.item(
                header= "Ingrese aquí los datos:",
                content=rx.center(input_data()),
                #hover_style={"background_color": "#132D46"},
            ),
            rx.accordion.item(
                header= "Filtros:",
                content="Yes. It's unstyled by default, giving you freedom over the look and feel.",
            ),
            collapsible=True,
            ),
            max_width= "450px",
            width= "100%",
        ),
    )

