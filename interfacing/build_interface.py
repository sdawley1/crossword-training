"""
Driver script to build app interface
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Canvas, Color
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
# Custom imports
from screens import PuzzleScreen, HomeScreen # Custom screens
from buttons import DifficultySlider, MenuButton # Custom buttons
from layouts import HomeLayout, NavigationLayout # Custom layouts for each button

class CrosswordGame(Widget):
    """
    Main widget for game
    """
    def __init__(self):
        super().__init__()
        # with self.canvas:
        #     Color(rgba=(1,0,0,1))

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

        # Menus
        HomeMenu = HomeLayout()

        # Build individual buttons for home screen
        DiffBtn = MenuButton("Difficulty", color=(1,0,0,1))
        dslider = HomeLayout(anchor_x="left", anchor_y="top")
        PrefBtn = MenuButton("Prefilled", color=(1,0,0,1))
        dslider = HomeLayout(anchor_x="left", anchor_y="center")
        difficulty = DifficultySlider()
        dslider = HomeLayout(anchor_x="left", anchor_y="top")

        dslider.add_widget(DiffBtn)
        dslider.add_widget(PrefBtn)
        dslider.add_widget(difficulty)

        # Build individual buttons for puzzle screen
        # PrevBtn = MenuButton(text="Previous", color=(1,0,0,1))
        # NextBtn = MenuButton(text="Next", color=(0,1,0,1))
        # MenuBtn = MenuButton(text="Menu", color=(0,0,1,1))

        # Create layouts to import in build_interface.py
        HomeMenu.add_widget(dslider)
        # NavPrev = NavigationLayout(anchor_x="left", anchor_y="top")
        # NavNext = NavigationLayout(anchor_x="right", anchor_y="top")
        # NavMenu = NavigationLayout(anchor_x="center", anchor_y="top")
        # NavPrev.add_widget(PrevBtn)
        # NavNext.add_widget(NextBtn)
        # NavMenu.add_widget(MenuBtn)

        # Build home screen
        # temp.add_widget(NavPrev)
        # temp.add_widget(NavNext)
        # temp.add_widget(NavMenu)

        hs.add_widget(HomeMenu)
        # ps.add_widget(temp)

        # Add completed screens
        # sm.add_widget(hs)
        # sm.add_widget(ps)
        # sm.switch_to(ps, direction="right", duration=2.0)

        # Add all screens to game
        # game.add_widget(sm)

        return hs

if __name__ == "__main__":
    CrosswordApp().run()