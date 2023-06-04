"""
Driver script for crossword trainer
"""
import numpy as np
from clue_manips.find_clue import JSONParser

def main() -> None:
    parser = JSONParser("./web_scraping/clue_data.txt")
    test = True
    while test:
        with open(parser.filename, "r") as f:
            test, clue = parser.qchoice_randomly(f)
    return

if __name__ == "__main__":
    main()