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
    # def __init__(self, pos_hint: dict={"x":0.1, "y":0.1}, size_hint: tuple=(0.1,0.1), color: tuple=(1,1,1,1), **kwargs):
    #     super().__init__(**kwargs)
    #     self.pos_hint = pos_hint
    #     self.size_hint = size_hint
    #     self.color = color
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
        # self.add_widget(MenuButton(text="Previous"))
        # self.add_widget(MenuButton(text="Next"))
        # self.add_widget(MenuButton(text="Menu"))

if __name__ == "__main__":
    pass