import reflex as rx
import album_project.styles.styles as styles
from album_project.styles.styles import Size
from album_project.views.grid import grid
from album_project.components.navbar import navbar
from album_project.state.PageState import PageState


@rx.page(
        on_load= PageState.items_grid,
)
def index() -> rx.Component:
    # Album Page
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                grid(),
                width= "100%",
                margin_y= Size.XBIG.value,
                margin_x=Size.MEDIUM.value,
            ), 
            width= "100%",
            justify= "center",
        ),
        width= "100d%",
    )