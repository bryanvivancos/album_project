import reflex as rx 
import album_project.styles.styles as styles
from ..state.AuthState import AuthState

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
                                        "Login", type="submit",
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
                            AuthState.login(AuthState.user_email, AuthState.password)
                        ],
                        reset_on_submit= True,
                    ),
                ),
    ),
#                     #############################
#                     # rx.form.root(
#                     #     rx.flex(
#                     #         field_form_component_general(
#                     #             "Usuario",
#                     #             "Ingrese su correo",
#                     #             "username",
#                     #             "Ingrese un correo valido",
#                     #             PageState.set_username,
#                     #             PageState.user_invalid
#                     #         ),
#                     #         field_form_component(
#                     #             "Contraseña",
#                     #             "Ingrese su contraseña",
#                     #             "password",
#                     #             PageState.set_password,
#                     #             "password"
#                     #         ),
#                     #         rx.flex(
#                     #             rx.dialog.close(
#                     #                 rx.button(
#                     #                     "Cancelar",
#                     #                     style= styles.denied_button_style,
#                     #                 ),
#                     #             ),
#                     #             rx.dialog.close(
#                     #                 rx.form.submit(
#                     #                     rx.cond(
#                     #                         PageState.loader,
#                     #                         rx.spinner(color= "red", size= "1"),
#                     #                             rx.button(
#                     #                                 "Log In",
#                     #                                 disabled= PageState.validate_fields,
#                     #                                 style= styles.confirm_button_style,
#                     #                             ),
#                     #                     ),
#                     #                     as_child= True,
#                     #                 ),
#                     #             ),
#                     #             spacing="3",
#                     #             justify="end",
#                     #         ),
#                     #         # rx.cond(
#                     #         #     PageState.error,
#                     #         #     rx.toast.error("Credenciales incorrectas"),
#                     #         # ),
#                     #         direction="column",
#                     #         spacing="4",
#                     #     ),
#                     #     on_submit=[
#                     #         PageState.loginService
#                     #     ],
#                     #     reset_on_submit= True,
#                     # )
#                 ),
#             ),



# ################################################################################


# def field_form_component(label: str, placeholder: str, name_var: str, on_change_function, type_field: str) -> rx.Component:
#     return rx.form.field(
#         rx.flex(
#             rx.form.label(label),
#             rx.form.control(
#                 rx.input(
#                     placeholder= placeholder,
#                     on_change= on_change_function,
#                     name= name_var,
#                     type= type_field,
#                     required= True,
#                 ),
#                 as_child= True,
#             ),
#         rx.form.message(
#             "El campo no puede ser nulo",
#             match= "valueMissing",
#             color= "red",
#         ),
#         direction= "column",
#         spacing= "2",
#         align= "stretch",
#         ),
#         name= name_var,
#         width= "30vw",
#     )

# def field_form_component_general(label: str, placeholder: str, name: str, message_validate: str, on_change_function, show) -> rx.Component:
#     return rx.form.field(
#         rx.flex(
#             rx.form.label(label),
#             rx.form.control(
#                 rx.input(
#                     placeholder= placeholder,
#                     on_change= on_change_function,
#                     name= name,
#                     required= True,
#                 ),
#                 as_child= True,
#             ),
#         rx.form.message(
#             message_validate,
#             name= name,
#             match= "valueMissing",
#             force_match= show,
#             color= "red",
#         ),
#         direction= "column",
#         spacing= "2",
#         align= "stretch",
#         ),
#         name= name,
#         width= "30vw",
