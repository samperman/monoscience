import os
import sys

from shiny import render, ui
from shiny.express import input

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import shared

ui.panel_title("Application One!!")
ui.input_slider("n", "N", 0, 100, 20)

@render.text
def txt():
    return f"n*2 is {input.n() * 2}"

@render.text
def shared_code():
    return shared.something()
