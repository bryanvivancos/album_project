import reflex as rx 
import album_project.styles.styles as styles
from album_project.styles.colors import Color
from album_project.state.AuthState import AuthState
from ..views.login import login
from ..views.signup import signup

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
                        rx.button(
                            rx.icon("door-open", size=16),
                            rx.text("Logout", size="4"),
                            on_click=AuthState.logout,
                        ),
                        rx.hstack(
                            rx.button(
                                rx.icon("circle-user-round", size=16),
                                rx.text("Login", size="4"),   
                                on_click=AuthState.set_which_dialog_open("login"), #para abrir el menu de login al hacer click      
                            ),
                            rx.button(
                                rx.icon("door-closed", size=16),
                                rx.text("Signup", size="4"),   
                                on_click=AuthState.set_which_dialog_open("signup"), #para abrir el menu de signup al hacer click      
                            ),
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
                    rx.cond(
                        AuthState.is_authenticated,
                        rx.menu.content(
                            rx.menu.item(
                                rx.icon("door-open", size=16),
                                rx.text("Logout", size="4"),
                                on_click=AuthState.logout,
                            ),
                            bg= Color.PRIMARY.value,
                        ),
                        rx.menu.content(
                            rx.menu.item(
                                rx.icon("circle-user-round", size=16),
                                rx.text("Login", size="4"),   
                                on_click= AuthState.set_which_dialog_open("login"), #para abrir el menu de login al hacer click
                            ),
                            rx.menu.item(
                                rx.icon("door-closed", size=16),
                                rx.text("Sign up", size="4"),
                                on_click= AuthState.set_which_dialog_open("signup"), #para abrir el menu de signup al hacer click                
                            ),
                        bg= Color.PRIMARY.value,
                        ),
                    ),
                    justify="end",
                ),
                login(),
                signup(),
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