"""
Driver script for crossword trainer
"""
import sys
from clue_manips.find_clue import JSONParser
# from interfacing.build_interface import CrosswordApp

def main(method: str=None, day: str="monday", diff: str="easy") -> None:
    parser = JSONParser("./web_scraping/clue_data.txt", method=method, day=day, diff=diff)
    onoffswitch = True
    while onoffswitch:
        if not parser.method:
            with open(parser.filename, "r") as f:
                onoffswitch, _ = parser.qchoice_randomly(f, "hard")
        else:
            gen = parser._generate_clues() # Generator for lines in text file
            for clue in gen:
                if parser.method.upper() == "DAY" and parser.day.upper() == clue.day.upper():
                    onoffswitch, _ = parser.qchoice(clue, prefilled=parser.difficulty)
                elif parser.method.upper() == "DIFF" and parser.difficulty.upper() in clue.difficulty.upper():
                    onoffswitch, _ = parser.qchoice(clue, prefilled=parser.difficulty)
                if not onoffswitch:
                    break
                    
    return

if __name__ == "__main__":
    # CrosswordApp().run()
    main(*sys.argv[1:])