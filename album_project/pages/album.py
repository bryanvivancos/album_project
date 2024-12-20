import reflex as rx
import album_project.styles.styles as styles
from album_project.styles.fonts import FontWeight
from album_project.state.AuthState import AuthState
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
                rx.cond(
                    AuthState.is_authenticated,
                    menu_bar(),
                    rx.center(
                        rx.text("Inicia sesion para interactuar con la base",
                                color= Color.BACKGROUND.value,
                                font_weight= FontWeight.BOLD.value,),
                        width= "100%",
                    ),
                ),
                rx.divider(),
                grid(),
                max_width= styles.MAX_WIDTH,
                width="100%",
                margin_y= Size.XBIG.value,
                bg_color=Color.SECONDARY.value,
                border_radius= 10,
                padding= Size.DEFAULT.value,
                spacing= "4",
            ), 
            margin_x=Size.MEDIUM.value,
        ),
    )