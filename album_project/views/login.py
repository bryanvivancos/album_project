import reflex as rx 
import album_project.styles.styles as styles
from ..state.AuthState import AuthState

def login() -> rx.Component:
    return rx.dialog.root(
                # rx.dialog.trigger(
                #     rx.button(
                #         rx.icon("circle-user-round", size=16),
                #         rx.text("Login", size="4"),
                #     )
                # ),
                rx.dialog.content(
                    rx.dialog.title(
                        "Ingresa tu usuario y contraseña"
                    ),
                    rx.form(
                        rx.flex(
                            rx.input(
                                placeholder="User", 
                                name="user",
                                on_change= AuthState.set_user_email,
                            ),
                            rx.input(
                                placeholder="Password",
                                name="password",
                                type= "password",
                                on_change= AuthState.set_password,
                            ),
                            rx.flex(
                                rx.dialog.close(
                                    rx.button(
                                        "Cancelar",
                                        style= styles.denied_button_style,
                                    ),
                                ),
                                rx.dialog.close(
                                    rx.button(
                                        "Login", type="submit",
                                        style= styles.confirm_button_style,
                                    ),
                                ),
                                spacing="3",
                                justify="end",
                            ),
                            direction="column",
                            spacing="4",
                        ),
                        on_submit=[
                            AuthState.login(AuthState.user_email, AuthState.password)
                        ],
                        reset_on_submit= True,
                    ),
                ),
                open= AuthState.which_dialog_open== "login",
                on_open_change= AuthState.set_which_dialog_open("") #para abrir el menu de login al hacer click                
    ),