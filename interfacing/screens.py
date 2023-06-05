"""
Driver script to build app interface
"""
from kivy.uix.layout import Layout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
#
from layouts import NavigationLayout, HomeLayout

class HomeScreen(Screen):
    def __init__(self, name: str="Home"):
        super().__init__()
        self.name = name

    def assign_layout(self, layout: Layout, label: str="label") -> None:
        self.layout = layout
        self.layout.add_widget(Label(text=label))
        self.add_widget(self.layout)
        return

class PuzzleScreen(Screen):
    def __init__(self, name: str="Puzzle"):
        super().__init__()
        self.name = name

    def assign_layout(self, layout: Layout, label: str="label") -> None:
        self.layout = layout
        self.layout.add_widget(Label(text=label))
        self.add_widget(self.layout)
        return

    # def assign_layout(self, layout: Layout) -> None:
    #     self.layout = layout
    #     self.label = Label(text="Puzzle Layout")
    #     self.layout.add_widget(self.label)
    #     self.add_widget(self.layout)
    #     return

if __name__ == "__main__":
    pass