import reflex as rx 
from enum import Enum
from album_project.styles.fonts import Font,FontWeight
from album_project.styles.colors import Color,TextColor

MAX_WIDTH = "768px"

#FONTS

STYLESHEETS= [
    "https://fonts.googleapis.com/css?family=Quicksand:wght@400;700&display=swap"
]

#SIZES
class Size(Enum):
    XSMALL= "0.2em"
    SMALL= "0.5 em"
    MEDIUM= "0.8em"
    DEFAULT= "1em"
    XBIG= "1.5em"
    SUPERBIG= "10em"

#STYLES

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weigth": FontWeight.LIGHT.value,
    "font_size": Size.DEFAULT.value,
    "font_color": TextColor.BODY.value,
    "background_color": Color.BACKGROUND.value,
    rx.accordion.item:{
        "background_color": Color.BACKGROUND.value,
        "hover_style":{
            "background_color": "#132D46",
        },
    },
    rx.accordion.trigger:{
        "hover_style":{
            "background_color": "#132D46",
        },
    },
    # rx.accordion.trigger:{
    #     ":hover": {
    #         "background_color:": Color.PRIMARY.value
    #     }
    # },
    rx.button: {
        "background_color": Color.PRIMARY.value,
        "_hover": {
            "background_color": Color.SECONDARY.value,
        }
    }
}

title_style = dict(
    width="100%",
    font_size=Size.DEFAULT.value,
    font_weigth=FontWeight.BOLD.value,
)



item_data_style = dict(
    background_color=Color.PRIMARY.value,
    border_radius= Size.DEFAULT.value,
)