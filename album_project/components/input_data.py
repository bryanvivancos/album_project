import reflex as rx
from album_project.styles.colors import Color as Color
from album_project.state.PageState import PageState
from album_project.api.SupabaseAPI import SupabaseAPI


def input_data() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Product",
                    name="title",
                    width="100%",
                    required= True,
                ),
                rx.input(
                    placeholder="Description",
                    name="description",
                    width="100%",
                    required= True,
                ),
                rx.center(
                    rx.hstack(
                        rx.button(
                            "Submit", 
                            type="submit",
                        ),
                        rx.button(
                            "Delete",
                            #on_click= PageState.delete_button,
                        ),
                    ),
                    width="100%",
                ),
            ),
            on_submit=[
                PageState.handle_submit,
                #PageState.items_grid, 
                #rx.window_alert(" "),
            ],
            reset_on_submit=True,
        ),
        width="100%",
    )