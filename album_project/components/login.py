import reflex as rx 
import album_project.styles.styles as styles

def login() -> rx.Component:
    return rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(
                        rx.icon("circle-user-round", size=16),
                        rx.text("Login", size="4"),
                    )
                ),
                rx.dialog.content(
                    rx.dialog.title(
                        "Ingresa tu usuario y contraseña"
                    ),
                    rx.form(
                        rx.flex(
                            rx.input(
                                placeholder="User", name="user"
                            ),
                            rx.input(
                                placeholder="Password",
                                name="password",
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
                                        "Submit", type="submit",
                                        style= styles.confirm_button_style,
                                    ),
                                ),
                                spacing="3",
                                justify="end",
                            ),
                            direction="column",
                            spacing="4",
                        ),
                    )
                )
            ),
