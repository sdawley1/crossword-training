"""
Driver script to build app interface
"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.stacklayout import StackLayout

class CrosswordLayout(StackLayout):
    """
    Control display of puzzles
    Base class: https://kivy.org/doc/stable/api-kivy.uix.stacklayout.html
    """
    def __init__(self):
        super(StackLayout, self).__init__(**kwargs)

class PuzzleLabel(Label):
    """
    Labels individual puzzles
    Base class: https://kivy.org/doc/stable/api-kivy.uix.label.html
    """
    pass

class PuzzleText(TextInput):
    """
    Controls input for individual puzzles
    Base class: https://kivy.org/doc/stable/api-kivy.uix.textinput.html
    """
    pass

class CrosswordGame(Widget):
    """
    Base class: https://kivy.org/doc/stable/api-kivy.uix.widget.html
    """
    pass

class CrosswordApp(App):
    """
    Builds and runs app
    Base class: https://kivy.org/doc/stable/api-kivy.app.html
    """
    def build(self):
        return CrosswordGame()

if __name__ == "__main__":
    CrosswordApp().run()