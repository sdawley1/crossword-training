"""
Driver script to build app interface
"""
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class CrosswordGame(Widget):
    """
    Main widget for game
    """
    def __init__(self):
        super().__init__()
        # LabelBase.register(name="orphans", fn_regular="/System/Library/Fonts/dream_orphans/'Dream Orphans.otf'")
        

# class tempButton(Button):
#     def __init__(self, text: str):
#         super().__init__()
#         with self.canvas.before:
#             # Color(1,1,1,0.5)
#             self.rect = Rectangle(pos=self.pos, size=self.size)
#         self.bind(size=self.update_rect)

#     def update_rect(self, instance, value):
#         self.rect.pos = self.pos
#         self.rect.size = self.size


class CrosswordApp(App):
    """
    Builds and runs app
    """
    def build(self):
        # Initialize game
        root = CrosswordGame()
        root.size_hint = (1, 1) # Fix root widget to take up entire window

        # # Container where all other layouts will be held
        # title_slide = BoxLayout(orientation="vertical", pos=(root.width, root.height), size_hint=(1,1))

        # # Make some fun containers
        # header = BoxLayout(orientation="horizontal", spacing=100, size_hint=(1,1))
        # buttons = BoxLayout(orientation="vertical", spacing=100, size_hint=(1,1))
        # citation = BoxLayout(orientation="horizontal", spacing=100, size_hint=(1,1))

        # # Make some fun labels
        # title = Label(text="Title")
        # author = Label(text="Author")

        # # Make some fun buttons
        # play = Button(text="Play")

        # # Add all those fun buttons and labels we just made
        # header.add_widget(title)
        # buttons.add_widget(play)
        # citation.add_widget(author)

        # # Add all those fun layouts we just made
        # title_slide.add_widget(header)
        # title_slide.add_widget(buttons)
        # title_slide.add_widget(citation)

        # # Add that layout to the game
        # root.add_widget(title_slide)

        return root # Return the root Widget()

if __name__ == "__main__":
    CrosswordApp().run()