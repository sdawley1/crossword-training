"""
Script for randomly choosing and displaying a clue

TO-DO LIST:
-----------
- Fix relative path name in JSONParser.filter_questions() when opening .txt file
    - Right now it assumes we run script from HOME DIRECTORY
- Add more filters for choosing questions
- QUESTIONS DO NOT INCREMENT USING 'weekday' AND 'difficulty' METHODS
    - Fix this
- Think of better way to fill in letters based on prefilled difficulty
"""
import os
import json
import functools
import numpy as np

class Clue:
    def __init__(self, question: str, answer: str, alignment: int, author: str, weekday: str, date: str) -> None:
        self.question = question
        self.answer = answer
        self.align = alignment # binary 0 (horizontal), 1 (vertical)
        self.author = author
        self.day = weekday
        self.date = date
        return

class JSONParser: # Deprecated name because I'm not using .json files anymore. Who cares!
    def __init__(self, filename: str, method: str=None, day: str=None) -> None:
        self.filename = filename
        self.method = method
        self.weekday = day

    def _line2clue(self, line: str) -> Clue:
        """Convert (raw) line from txt file to Clue()"""
        question, answer, alignment, author, weekday, date = line.strip("\n").split("0x1F")
        print(f"({weekday}, {date}) {question} -> {answer}")
        return Clue(question, answer, alignment, author, weekday, date)
    
    def _prefill_answer(self, line: str, prefilled: str) -> int:
        """Convert prefilled difficulty to integer"""
        _, answer, _, _, _, _ = line.strip("\n").split("0x1F")
        n = len(answer)
        partial_answer = ["_" for _ in range(n)]
        p2i = {"easy": np.floor(n/2), "medium": np.floor(n/3), "hard": np.floor(n/4)}[prefilled] # CHANGE THIS AT SOME POINT
        while p2i > 0:
            rc = np.random.randint(n-1)
            if partial_answer[rc] == "_":
                partial_answer[rc] = answer[rc]
                p2i -= 1
        return "".join(partial_answer)

    def _partial_answer(self, line: str, prefilled: str=None) -> str:
        """Return partially filled in answer (as if the crossword has been partially filled in)"""
        _, answer, _, _, _, _ = line.strip("\n").split("0x1F")
        partial_answer = "_"*len(answer)
        if prefilled:
            return self._prefill_answer(line, prefilled)
        else:
            return partial_answer
        
    def _pose_question(self, line: str, prefilled: str=None) -> Clue:
        """Convert (raw) line from txt file to Clue()"""
        question, answer, alignment, author, weekday, date = line.strip("\n").split("0x1F")
        partial_answer = self._partial_answer(line, prefilled)
        stdin = input(f"({weekday}, {date}) {question} = {partial_answer} ({len(answer)} letters) ", )
        if stdin.upper() == "EXIT":
            toggle = False
        elif stdin.upper() == answer.upper():
            print("Correct!")
            toggle = True
        else:
            print(f"Wrong! Answer is {answer}")
            toggle = True
        return toggle, Clue(question, answer, alignment, author, weekday, date)
    
    def update_method(self, method: str) -> None:
        """Changes method of filtering questions"""
        self.method = method
    
    def _question_filter(filter) -> str:
        """
        Filter questions (potentially randomly) to extract lines from clue_data.txt
        'filter' is a function which specifies how specifies how questions should be chosen
        Returns raw string from JSON file 
        """
        @functools.wraps(filter)
        def filter_wrap(self, *args) -> None:
            return filter(self, *args)
        return filter_wrap

    @_question_filter
    def qchoice_randomly(self, iostream, prefilled: str=None) -> Clue:
        """
        Choose clues randomly
        Note that calling doing anything with iostream before calling iostream.readlines() removes stream and leads to error later
        """
        spec = np.random.randint(100000) # Random int on [0 - approx. len(iostream)]
        return self._pose_question(iostream.readlines()[spec], prefilled)

    @_question_filter
    def qchoice_by_weekday(self, iostream, day: str, prefilled: str=None) -> Clue:
        """Choose clues based only on day of week they were published"""
        for line in iostream.readlines():
            if day.upper() in line.upper():
                return self._pose_question(line, prefilled)
    
    @_question_filter
    def qchoice_by_difficulty(self, iostream, difficulty: str, prefilled: str=None) -> Clue:
        """
        Choose clues based on relative difficulty (established from day of the week published)
        As it stands,
            EASY = Monday/Tuesday
            MEDIUM = Wednesday/Thursday
            HARD = Friday/Saturday
            EXPERT = Sunday
        """
        # Local function for converting difficulty to day(s) of the week
        diff2days = lambda diff: {
            "EASY": ["MONDAY", "TUESDAY"], "MEDIUM": ["WEDNESDAY", "THURSDAY"], "HARD": ["FRIDAY", "SATURDAY"], "EXPERT": ["SUNDAY"]
            }[diff] # returns a list of days
        days = diff2days(difficulty.upper())
        for line in iostream.readlines():
            if days[0] in line or days[-1] in line.upper():
                return self._pose_question(line, prefilled)

if __name__ == "__main__":
    parser = JSONParser("./web_scraping/clue_data.txt", method="weekday")
    with open(parser.filename, "r") as f:
        # parser.qchoice_randomly(f)
        # parser.qchoice_by_weekday(f, "tuesday")
        parser.qchoice_by_difficulty(f, "expert")