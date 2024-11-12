import reflex as rx
import album_project.styles.styles as styles
from album_project.styles.styles import Size
from album_project.views.grid import grid
from album_project.components.navbar import navbar
from album_project.state.PageState import PageState


@rx.page(
    on_load= PageState.items_grid
)
def index() -> rx.Component:
    # Album Page
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                    grid(),
                max_width= styles.MAX_WIDTH, 
                margin_y= Size.XBIG.value,
            ),
        ),
        width= "100%",
    )