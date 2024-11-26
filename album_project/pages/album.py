import reflex as rx
import album_project.styles.styles as styles
from album_project.styles.colors import Color
from album_project.styles.styles import Size
from album_project.views.grid import grid
from album_project.components.navbar_login import navbar
from album_project.views.menu_bar import menu_bar


@rx.page(
      #  on_load= PageState.items_grid,
)
def index() -> rx.Component:
    # Album Page
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                menu_bar(),
                
                rx.divider(),
                grid(),
                max_width= styles.MAX_WIDTH,
                width="100%",
                margin_y= Size.XBIG.value,
                bg_color=Color.SECONDARY.value,
                border_radius= Size.DEFAULT.value,
                padding= Size.DEFAULT.value,
                spacing= "4",
            ), 
            margin_x=Size.MEDIUM.value,
        ),
    )