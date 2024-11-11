import reflex as rx 
from enum import Enum
from album_project.styles.fonts import Font,FontWeight
from album_project.styles.colors import Color

MAX_WIDTH = "720px"

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
    "background_color": Color.BACKGROUND.value,
    "font_size": Size.DEFAULT.value,
}

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.XBIG.value
)