import reflex as rx 
import album_project.styles.styles as styles
from ..state.AuthState import AuthState

def signup() -> rx.Component:
    return rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(
                        rx.icon("door-closed", size=16),
                        rx.text("Sign up", size="4"),
                    )
                ),
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
                                        "Sign up", type="submit",
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
                            AuthState.signup(AuthState.user_email, AuthState.password)
                        ],
                        reset_on_submit= True,
                    ),
                ),
            ),