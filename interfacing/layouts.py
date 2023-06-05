"""
Script for building layouts
"""
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
# Custom imports
from buttons import Navigation
    
class HomeLayout(AnchorLayout):
    """
    Control display of puzzles
    """
    def __init__(self, anchor_x: str="center", anchor_y: str="center", **kwargs):
        super().__init__(**kwargs)
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        self.add_widget(Navigation(text="Difficulty")) # This is wrong but I'm too tired to fix it

class NavigationLayout(AnchorLayout):
    """
    Control display of navigational buttons
    """
    def __init__(self, anchor_x: str="center", anchor_y: str="center", **kwargs):
        super().__init__(**kwargs)
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        self.add_widget(Navigation(text="Previous"))
        self.add_widget(Navigation(text="Next"))
        self.add_widget(Navigation(text="Menu"))

    # def add_nav_button(self, btn: Button) -> None:
    #     """Add navigational buttons to layout"""
    #     butt = Factory.Navigation(text=btn.text)
    #     self.ids.anchor.add_widget(butt)
    #     return
    
HomeMenu = HomeLayout()

NavPrev = NavigationLayout(anchor_x="center", anchor_y="center")
NavNext = NavigationLayout(anchor_x="center", anchor_y="center")
NavMenu = NavigationLayout(anchor_x="center", anchor_y="center")

if __name__ == "__main__":
    pass