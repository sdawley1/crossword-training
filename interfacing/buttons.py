"""
Script for building all buttons
"""
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

class MenuButton(Button):
    """Buttons for navigation (prev, next, menu, etc.)"""
    def __init__(self, text: str=None, color: tuple=(0,0,0,1), size_hint: tuple=(0.15, 0.15)):
        super().__init__()
        self.bind(on_press=self.callback)
        self.text = text
        self.color = (1,1,1,1) # text color
        # self.size = size
        self.size_hint = size_hint
        self.background_color = color

    def callback(self, *args) -> None:
        """Event to play on button click"""
        s2p = f"{self.text}"
        print(s2p) # temporary
        return
    
class DifficultySlider(Spinner):
    """Buttons controlling difficulty (easy, medium, hard, expert) and prefilled extent (easy, medium, hard)"""
    def __init__(self, text: str="Easy", values: tuple=("Easy", "Medium", "Hard", "Expert"), pos_hint: dict={"x":0.1, "y":0.1}, size_hint: tuple=(0.1, 0.1)):
        super().__init__()
        self.text = text
        self.values = values
        self.pos_hint = pos_hint
        self.size_hint = size_hint

if __name__ == "__main__":
    pass