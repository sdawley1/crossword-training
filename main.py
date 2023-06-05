"""
Driver script for crossword trainer
"""
from clue_manips.find_clue import JSONParser
from interfacing.build_interface import CrosswordApp

def main() -> None:
    parser = JSONParser("./web_scraping/clue_data.txt", method="weekday")
    test = True
    while test:
        with open(parser.filename, "r") as f:
            test, clue = parser.qchoice_by_weekday(f, "wednesday", "medium")
    return

if __name__ == "__main__":
    # CrosswordApp().run()
    main()