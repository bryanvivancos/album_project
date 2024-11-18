import reflex as rx 
from album_project.model.Items import Items
from album_project.styles.styles import Color
from album_project.styles.styles import Size
import album_project.styles.styles as styles
from album_project.state.PageState import PageState

def item_data(data: Items) -> rx.Component:
    return rx.link(
        rx.box(
            # rx.image(
            #     src= data.image,
            #     width="100%",
            #     height="auto",
            #     alt=f"Imagen destacada para: {data.title}",
            # ),
            rx.text(
                data.title,
                size= "1px",
            ),
            rx.text(
                data.description,
                size= "1px",
            ),
            rx.hstack(
                rx.text(
                    data.id,
                    size= "1px",
                ),
                rx.flex(
                    rx.dialog.root(
                        rx.dialog.trigger(rx.button(
                            rx.icon(
                                "trash",
                                ),
                            style= styles.trash_button_style,
                            )
                        ),
                        rx.dialog.content(
                            rx.dialog.title("Eliminar Elemento"),
                            rx.dialog.description("Está seguro de eliminar el elemento " + data.title),
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
                                            PageState.delete_button(data.id),
                                            PageState.items_grid,
                                            ]
                                    )
                                ),
                                spacing= Size.DEFAULT.value, 
                                margin_top= Size.DEFAULT.value,
                                justify= "end",
                            )
                        )
                    ),
                ),
                justify= "between",
            ),
            style= styles.item_data_style,
            padding= Size.MEDIUM.value,
        ),
        href="#",
        style= styles.link_style,
    )

