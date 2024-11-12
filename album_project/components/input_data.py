import reflex as rx
from album_project.styles.colors import Color as Color

def input_data() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Product",
                    name="first_name",
                    width="100%",
                ),
                rx.input(
                    placeholder="Description",
                    name="first_name",
                    width="100%",
                ),
                rx.center(
                    rx.button(
                    "Submit", 
                    type="submit",
                    ),
                    width="100%",
                ),
            ),
        ),
        width="100%",
    )