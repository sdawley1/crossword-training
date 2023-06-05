"""
Driver script to build app interface
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
# Custom imports
from screens import PuzzleScreen, HomeScreen # Custom screens
from buttons import PrevBtn, NextBtn, MenuBtn # Custom buttons
from layouts import NavPrev, NavNext, NavMenu # Custom layouts for each button

class PuzzleScreen(Screen):
    def __init__(self):
        super().__init__()

class CrosswordGame(Widget):
    """
    Main widget for game
    """
    pass

class CrosswordApp(App):
    """
    Builds and runs app
    """
    def build(self):
        # Initialize game
        game = CrosswordGame()
        
        # Initialize screens and screen manager
        sm = ScreenManager()
        hs = HomeScreen()
        # ps = PuzzleScreen()

        # Build navigation buttons and add to existing layout then append to unique screen
        for layout, btn in zip([NavPrev, NavNext, NavMenu], [PrevBtn, NextBtn, MenuBtn]):
            layout.add_widget(btn)
            hs.assign_layout(layout)

        # Add completed screens
        sm.add_widget(hs)
        # sm.add_widget(ps)

        # Add all screens to game
        game.add_widget(sm)

        return game

if __name__ == "__main__":
    CrosswordApp().run()