"""
Script for building all buttons
"""
from kivy.uix.button import Button

class Navigation(Button):
    """
    Buttons for navigation (prev, next, menu, etc.)
    """
    def __init__(self, text: str=None, size_hint: tuple=(1, 1), size: tuple=(10, 10)):
        super().__init__()
        self.bind(on_press=self.callback)
        # self.text_size = self.size
        self.text = text
        self.size = size
        self.size_hint = size_hint

    def callback(self, *args) -> None:
        """Event to play on button click"""
        s2p = f"{self.text}"
        print(s2p) # temporary
        return
    
# Build individual buttons to import later
PrevBtn = Navigation(text="Previous")
NextBtn = Navigation(text="Next")
MenuBtn = Navigation(text="Menu")

if __name__ == "__main__":
    pass