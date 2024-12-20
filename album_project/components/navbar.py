### NAVBAR ANTIGUO

import reflex as rx 
import album_project.styles.styles as styles
from album_project.styles.colors import Color

def navbar() -> rx.Component:
    return rx.box(
        rx.stack(
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(
                        rx.icon("circle-user-round", size=18),
                        rx.text("Login", size="4"),
                        margin= styles.Size.DEFAULT.value
                    )
                ),
                rx.dialog.content(
                    rx.dialog.title(
                        "Ingresa tu usuario"
                    ),
                    rx.form(
                        rx.flex(
                            rx.input(
                                placeholder="User Name", name="name"
                            ),
                            rx.input(
                                placeholder="user@reflex.dev",
                                name="email",
                            ),
                            rx.flex(
                                rx.dialog.close(
                                    rx.button(
                                        "Cancel",
                                        variant="soft",
                                        color_scheme="gray",
                                    ),
                                ),
                                rx.dialog.close(
                                    rx.button(
                                        "Submit", type="submit"
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
        ),
        bg_color= Color.SECONDARY.value,
        height= "40px",
        z_index = "999",
        width= "100%",
        top= "0",
    )