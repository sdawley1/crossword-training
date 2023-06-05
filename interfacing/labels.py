"""
Driver script to build app interface
"""
import numpy as np
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
# Custom imports
from buttons import Navigation # Import custom buttons
from layouts import NavigationLayout

class PuzzleLabel(Label):
    """
    Labels individual puzzles
    """
    pass

class PuzzleText(TextInput):
    """
    Controls input for individual puzzles
    """
    pass

if __name__ == "__main__":
    pass