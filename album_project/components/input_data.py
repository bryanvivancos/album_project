import reflex as rx
import album_project.styles.styles as styles
from album_project.styles.colors import Color as Color
from album_project.state.PageState import PageState


def input_data() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Product",
                    name="title",
                    #on_change= PageState.set_title_input,
                    width="100%",
                    required= True,
                ),
                rx.input(
                    placeholder="Description",
                    name="description",
                    #on_change= PageState.set_description_input,
                    width="100%",
                    required= True,
                ),
                rx.center(
                    rx.button(
                        "Submit", 
                        type="submit",
                        style= styles.submit_button_style,
                        # on_click= PageState.items_grid,
                        # on_click= [
                        #     #agrega los datos individualmente para asi poder actualizar
                        #     #automaticamente con la funcion items_grid
                        #     PageState.handle_submit(
                        #         PageState.title_input, 
                        #         PageState.description_input),
                        #     PageState.items_grid,
                        #     # PageState.handle_submit(),
                        #     # PageState.items_grid(),
                        # ],
                    ),
                    width="100%",
                ),
            ),
            on_submit=[
                PageState.handle_submit,  #agrega los datos desde el formulario
                PageState.items_grid(),
            ],
            reset_on_submit=True,
        ),
        width="100%",
    )