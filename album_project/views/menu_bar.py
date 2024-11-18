import reflex as rx
from album_project.components.title import title
from album_project.components.input_data import input_data
from album_project.styles.styles import Size
from album_project.styles.colors import Color
import album_project.styles.styles as styles

def menu_bar() -> rx.Component:
    return rx.center(
        rx.accordion.root(
            rx.accordion.item(
                # rx.accordion.trigger(
                #     "Ingrese aquí los datos:",
                #     style= styles.accordion_trigger_style,
                # ),
                # rx.accordion.content(rx.center(input_data())),
                header= "Ingrese aquí los datos:",
                content= rx.center(input_data())
                #style= styles.accordion_trigger_style,
            ),
            rx.accordion.item(
                header= "Filtros:",
                content="Yes. It's unstyled by default, giving you freedom over the look and feel.",
            ),
            show_dividers= True,
            collapsible=True,
            width= "420px",
            #style= styles.accordion_style,
        ),
        width= "100%",
        padding_top= Size.DEFAULT.value, 
    )

