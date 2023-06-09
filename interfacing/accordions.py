"""
Script for building all buttons
"""
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.accordion import Accordion, AccordionItem

class AccordionLayout(Accordion):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _generate_children(self):
        """Yield children"""
        for child in self.children:
            yield child

    def detect_child_update(self):
        """Detect change in accordion item children"""
        for child in self._generate_children():
            if child.background_color[-1] == 0.5:
                print(child.background_color)

    def append_widgets(self, *args) -> None:
        """Append list of widgets to root"""
        for w in args:
            self.add_widget(w)

    def update(self):
        """On-click event"""
        self.detect_child_update()
    
class PlayAccordionItem(AccordionItem):
    def __init__(self, title: str, font_name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.font_name = font_name
    
    def configure_accordion(self, buttons: AccordionLayout, diff: list, descrip: list) -> None:
        """Configure AccordionItem to contain options"""
        for df, ds in zip(diff, descrip):
            item, btn = PlayAccordionItem(title=df, font_name=self.font_name), FancyLabel(text=ds, font_name=self.font_name)
            item.add_widget(btn)
            buttons.append_widgets(item)
        self.add_widget(buttons)
        return
    
class FancyLabel(Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font_size = 48
        self.font_name = "../fonts/Dream-Orphans.otf"
        self.background_color = (0,0,1,0.5)
    
class StartButton(Button):
    def __init__(self, sm: ScreenManager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font_size = 48
        self.font_name = "../fonts/Dream-Orphans.otf"
        self.background_color = (0,0,1,0.5)
        self.sm = sm
        self.on_press = self.navigate_on_click

    def color_update(self, color: tuple=(0,0,1,.75)) -> None:
        """Update background_color on button when clicked"""
        self.background_color = color
        return True
    
    def navigate_on_click(self) -> None:
        """Navigate to another page on click"""
        self.root.current = "Puzzle"
        return




if __name__ == "__main__":
    pass