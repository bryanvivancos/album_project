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



################################################################################


def field_form_component(label: str, placeholder: str, name_var: str, on_change_function, type_field: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder= placeholder,
                    on_change= on_change_function,
                    name= name_var,
                    type= type_field,
                    required= True,
                ),
                as_child= True,
            ),
        rx.form.message(
            "El campo no puede ser nulo",
            match= "valueMissing",
            color= "red",
        ),
        direction= "column",
        spacing= "2",
        align= "stretch",
        ),
        name= name_var,
        width= "30vw",
    )

def field_form_component_general(label: str, placeholder: str, name: str, message_validate: str, on_change_function, show) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder= placeholder,
                    on_change= on_change_function,
                    name= name,
                    required= True,
                ),
                as_child= True,
            ),
        rx.form.message(
            message_validate,
            name= name,
            match= "valueMissing",
            force_match= show,
            color= "red",
        ),
        direction= "column",
        spacing= "2",
        align= "stretch",
        ),
        name= name,
        width= "30vw",
    )