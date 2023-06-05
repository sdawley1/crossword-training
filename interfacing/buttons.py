"""
Script for building all buttons
"""
from kivy.uix.button import Button

class Navigation(Button):
    """
    Buttons for navigation (prev, next, menu, etc.)
    """
    def __init__(self, text: str=None, color: tuple=(0,0,0,1), size_hint: tuple=(0.25, 0.25)):
        super().__init__()
        self.bind(on_press=self.callback)
        self.text = text
        # self.size = size
        self.size_hint = size_hint
        self.background_color = color

    def callback(self, *args) -> None:
        """Event to play on button click"""
        s2p = f"{self.text}"
        print(s2p) # temporary
        return
    
# Build individual buttons to import later
PrevBtn = Navigation(text="Previous", color=(1, 0, 0, 1))
NextBtn = Navigation(text="Next", color=(0, 1, 0, 1))
MenuBtn = Navigation(text="Menu", color=(0, 0, 1, 1))

if __name__ == "__main__":
    pass