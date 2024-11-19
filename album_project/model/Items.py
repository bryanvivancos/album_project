import reflex as rx

class Items(rx.Base):
    id: str | None
    title: str
    description: str