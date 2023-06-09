"""
Driver script to build app interface
TO-DO LIST
----------
- Change color of accordion titles
- Make the play button look nicer
"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
#
from accordions import PlayAccordionItem, AccordionLayout, StartButton, FancyLabel
    
class CrosswordGame(Widget):
    """
    Main widget for game
    """
    pass


class NewBoxLayout(BoxLayout):
    """
    Main widget for game
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def append_widgets(self, *args) -> None:
        """Add widgets to root"""
        for w in args:
            self.add_widget(w)

class CrosswordApp(App):
    """
    Builds and runs app
    """
    def build(self):
        big_font = 96
        font = "../fonts/Dream-Orphans.otf"
        Window.clearcolor = (0, 0, 1, 0.8) # set background
        sm = ScreenManager()
        title_screen = Screen(name="Home")
        puzzle_screen = Screen(name="Puzzle")

        # Initialize the ancestor layout
        root = NewBoxLayout(size_hint=(1,1), orientation="vertical")

        # Title and author labels
        title_label = Label(text="NYT Crossword Puzzler\na game by Me", font_size=big_font, font_name=font)
        
        # Container to hold all navigational buttons (sorting, difficulty, aid)
        button_container = AccordionLayout(orientation="vertical")

        # Sorting Option
        sorting = PlayAccordionItem(title="Sorting", font_name=font)
        sorting_buttons = AccordionLayout(orientation="horizontal")
        method = ["Random", "Day", "Difficulty"]
        descrip = ["Roll the dice and choose questions randomly", "Restrict questions to a particular day", "Restrict questions to a particular difficulty"]
        sorting.configure_accordion(sorting_buttons, method, descrip)

        # Difficulty Option
        difficulty = PlayAccordionItem(title="Difficulty", font_name=font)
        difficulty_buttons = AccordionLayout(orientation="horizontal")
        diff = ["Easy", "Medium", "Hard", "Expert"]
        descrip = ["Takin' it Easy", "Something funny", "Something funnny", "There's no God here except for you"]
        difficulty.configure_accordion(difficulty_buttons, diff, descrip)

        # Completeness Option
        aid = PlayAccordionItem("Completeness", font_name=font)
        aid_buttons = AccordionLayout(orientation="horizontal")
        descrip = ["1/2 of the answer is provided", "1/3 of the answer is provided", "1/4 of the answer is provided", "No help (like Pompeii)"]
        aid.configure_accordion(aid_buttons, diff, descrip)

        # Add sorting, difficulty, and completeness options to button container
        button_container.append_widgets(sorting, difficulty, aid)

        start_button = StartButton(sm=sm, text="Play")
        start_button.background_color = (0,0,1,1)

        # Add layouts to root in specific order
        root.append_widgets(title_label, button_container, start_button)
        title_screen.add_widget(root)

        sm.add_widget(title_screen)
        sm.add_widget(puzzle_screen)
        
        return sm # Return the root Widget()

if __name__ == "__main__":
    CrosswordApp().run()