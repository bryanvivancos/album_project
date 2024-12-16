import reflex as rx 
import album_project.styles.styles as styles
from album_project.styles.colors import Color
from album_project.state.AuthState import AuthState
from ..views.login import login
from ..views.signup import signup
from ..views.logout import logout

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        " ", size="3", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    rx.cond(
                        AuthState.is_authenticated,
                        logout(),
                        rx.hstack(
                            login(), #Dialog que abre el form de login
                            signup(),
                        )
                    ),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        " ", size="3", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", 
                                size=24,
                                color= Color.PRIMARY.value
                                )
                    ),
                    rx.menu.content(
                            login(), #Dialog que abre el form de login
                            signup(),
                            bg= Color.PRIMARY.value,
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg_color= Color.SECONDARY.value,
        padding= styles.Size.DEFAULT.value,
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )