import os
import sys

from shiny import render, ui
from shiny.express import input

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import shared

ui.panel_title("Application Two!!")

@render.text
def shared_code():
    return shared.something()
