import reflex as rx
import album_project.styles.styles as styles
from album_project.state.PageState import PageState
from album_project.styles.styles import Size

def item_trash_button(item_title:str, item_id: int) -> rx.Component:
    return rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(rx.icon("trash",size= 16),
                        style= styles.trash_button_style,
                    ),
                ),
                rx.dialog.content(
                    rx.dialog.title("Eliminar Elemento"),
                    rx.dialog.description("Está seguro de eliminar el elemento " + item_title),
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
                                style= styles.confirm_button_style,
                                on_click= [
                                    PageState.delete_button(item_id),
                                    PageState.items_grid,
                                    ],
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
                ),
            ),