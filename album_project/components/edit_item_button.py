import reflex as rx 
import album_project.styles.styles as styles
from album_project.state.PageState import PageState
from album_project.styles.styles import Size

def edit_item_button(item_id: int) -> rx.Component:
    return rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(rx.icon("pencil", size= 16),
                        style= styles.edit_button_style,
                    ),
                ),
                rx.dialog.content(
                    rx.dialog.title("Actualizar Elemento"),
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
                                    "Confirmar",
                                    type= "submit",
                                    style= styles.confirm_button_style,
                                    
                                    # on_click= [
                                    #     PageState.update_button(
                                    #             PageState.title_input, 
                                    #             PageState.description_input,
                                    #             item_id,
                                    #             ),
                                    #         PageState.items_grid,
                                    #     ],
                                ),
                                # rx.cond(
                                #         SupabaseAPI.delete_item.del,
                                #         rx.toast.s("gdsfs"),
                                #     ),
                            ),
                            spacing= Size.DEFAULT.value, 
                            margin_top= Size.DEFAULT.value,
                            justify= "end",
                        ),
                        on_submit= [
                            PageState.update_button(item_id),
                            PageState.items_grid(),
                        ],
                        reset_on_submit=True,
                    ),
                ),
            ),
