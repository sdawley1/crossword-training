"""
Driver script to build app interface
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Canvas, Color
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
# Custom imports
from screens import PuzzleScreen, HomeScreen # Custom screens
from buttons import PrevBtn, NextBtn, MenuBtn # Custom buttons
from layouts import HomeMenu, NavPrev, NavNext, NavMenu # Custom layouts for each button

class CrosswordGame(Widget):
    """
    Main widget for game
    """
    def __init__(self):
        super().__init__()
        with self.canvas:
            Color(rgba=(1,0,0,1))
    pass

class CrosswordApp(App):
    """
    Builds and runs app
    """
    def build(self):
        # Initialize game
        game = CrosswordGame()
        
        # Initialize screens and screen manager
        sm = ScreenManager(transition=SwapTransition())
        hs = HomeScreen(name="Home")
        ps = PuzzleScreen(name="Puzzle")

        # Build home screen
        hs.assign_layout(HomeMenu)

        # Build puzzle screen(s)
        # Add navigation buttons on top of existing layout then append to unique puzzle screen
        for layout, btn in zip([NavPrev, NavNext, NavMenu], [PrevBtn, NextBtn, MenuBtn]):
            # layout.add_widget(btn)
            ps.assign_layout(layout)

        # Add completed screens
        sm.add_widget(hs)
        sm.add_widget(ps)
        sm.switch_to(ps, direction='right', duration=1.0)

        # Add all screens to game
        game.add_widget(sm)

        return game

if __name__ == "__main__":
    CrosswordApp().run()