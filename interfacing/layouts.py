"""
Script for building layouts
"""
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
# Custom imports
from buttons import Navigation
    
class PuzzleLayout(AnchorLayout):
    """
    Control display of puzzles
    """
    pass

class NavigationLayout(AnchorLayout):
    """
    Control display of navigational buttons
    """
    def __init__(self, anchor_x: str="left", anchor_y: str="top"):
        super().__init__()
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y

    # def add_nav_button(self, btn: Button) -> None:
    #     """Add navigational buttons to layout"""
    #     butt = Factory.Navigation(text=btn.text)
    #     self.ids.anchor.add_widget(butt)
    #     return
    
NavPrev = NavigationLayout(anchor_x="center", anchor_y="center")
NavNext = NavigationLayout(anchor_x="right", anchor_y="top")
NavMenu = NavigationLayout(anchor_x="left", anchor_y="top")

if __name__ == "__main__":
    pass