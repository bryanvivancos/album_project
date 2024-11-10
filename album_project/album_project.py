"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from album_project.pages.index import index



# class State(rx.State):
#     """The app state."""

#     ...





app = rx.App()
app.add_page(index)
