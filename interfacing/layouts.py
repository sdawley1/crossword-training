"""
Script for building layouts
"""
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
# Custom imports
from buttons import MenuButton
    
class HomeLayout(AnchorLayout):
    """
    Control display of puzzles
    """
    def __init__(self, anchor_x: str="center", anchor_y: str="center", **kwargs):
        super().__init__(**kwargs)
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y

class NavigationLayout(AnchorLayout):
    """
    Control display of navigational buttons
    """
    def __init__(self, anchor_x: str="center", anchor_y: str="center", **kwargs):
        super().__init__(**kwargs)
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y

if __name__ == "__main__":
    pass