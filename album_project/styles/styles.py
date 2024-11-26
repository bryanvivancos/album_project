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
    ZERO= "0px !important"
    XSMALL= "0.2em"
    SMALL= "0.5 em"
    MEDIUM= "0.8em"
    DEFAULT= "1em"  ##antes 1em
    XBIG= "1.5em"
    SUPERBIG= "10em"

#STYLES

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weigth": FontWeight.LIGHT.value,
    "font_size": Size.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    rx.accordion.root:{
        "background_color": Color.PRIMARY.value,
    },
    rx.accordion.item: {
        "background_color": Color.PRIMARY.value,
    },
    rx.accordion.trigger: {
        "background_color": Color.PRIMARY.value,
        "_hover": {
            "background_color": Color.BACKGROUND.value,
        },
    },
    rx.button: {
        "background_color": Color.PRIMARY.value,
    },
    rx.text: {
        "color": TextColor.BODY.value,
    },
}

title_style= dict(
    width="100%",
    font_size=Size.DEFAULT.value,
    font_weigth=FontWeight.BOLD.value,
),

link_style= dict(
    text_decoration= "none",
    _hover= {},
)

item_data_style= dict(
    background_color= Color.PRIMARY.value,
    border_radius= Size.DEFAULT.value,
    _hover= {"background_color": Color.BACKGROUND.value},
)

#### STYLES DE ACCORDION COMPONENT

accordion_style= dict(
    background_color= Color.BACKGROUND.value,
)

accordion_trigger_style= dict(
    _hover= {"background_color": Color.SECONDARY.value},
)


#### STYLES DE BOTONES 

submit_button_style= dict(
    background_color= Color.BACKGROUND.value,
    _hover= {"color": Color.SECONDARY.value},
)

confirm_button_style= dict(
    _hover= {"color": Color.SECONDARY.value},
)

denied_button_style= dict(
    _hover= {"color": "red"}, 
)

trash_button_style= dict(
    background_color="transparent",
    justify_content= "right",
    padding= Size.ZERO.value,
    _hover= {
        "color": "red"}, 
)

edit_button_style= dict(
    background_color="transparent",
    justify_content= "right",
    padding= Size.ZERO.value,
    _hover= {
        "color": Color.SECONDARY.value}, 
)
