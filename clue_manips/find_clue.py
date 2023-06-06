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
        # Get clue difficulty based on day published
        if self.day.upper() == "MONDAY" or self.day.upper() == "TUESDAY":
            self.difficulty = "easy"
        elif self.day.upper() == "WEDNESDAY" or self.day.upper() == "THURSDAY":
            self.difficulty = "medium"
        elif self.day.upper() == "FRIDAY" or self.day.upper() == "SATURDAY":
            self.difficulty = "hard"
        else:
            self.difficulty = "expert"
    
    def clue2line(self) -> str:
        """Return raw format for line given a clue"""
        return f"{self.question}0x1F{self.answer}0x1F{self.align}0x1F{self.author}0x1F{self.day}0x1F{self.date}"

class JSONParser: # Deprecated name because I'm not using .json files anymore. Who cares!
    def __init__(self, filename: str, method: str=None, day: str=None, diff: str=None) -> None:
        self.filename = filename
        self.method = method
        # Clean this up eventually
        if not day:
            self.day = "monday"
        else:
            self.day = day
        if not diff:
            self.difficulty = "easy"
        else:
            self.difficulty = diff

    def _line2clue(self, line: str) -> Clue:
        """Convert (raw) line from txt file to Clue()"""
        question, answer, alignment, author, weekday, date = line.strip("\n").split("0x1F")
        return Clue(question, answer, alignment, author, weekday, date)

    def _generate_clues(self) -> Clue:
        """Generate next line (question, answer, etc.) from text file for use in posing question"""
        for line in open(self.filename, "r").readlines():
            question, answer, alignment, author, weekday, date = line.strip("\n").split("0x1F")
            yield Clue(question, answer, alignment, author, weekday, date)
    
    def _prefill_answer(self, clue: Clue, prefilled: str) -> int:
        """Convert prefilled difficulty to integer"""
        n = len(clue.answer)
        partial_answer = ["_" for _ in range(n)]
        p2i = {"easy": np.floor(n/2), "medium": np.floor(n/3), "hard": np.floor(n/4)}[prefilled] # CHANGE THIS AT SOME POINT (?)
        while p2i > 0:
            rc = np.random.randint(n-1)
            if partial_answer[rc] == "_":
                partial_answer[rc] = clue.answer[rc]
                p2i -= 1
        return "".join(partial_answer)

    def _partial_answer(self, clue: Clue, prefilled: str=None) -> str:
        """Return partially filled in answer (as if the crossword has been partially filled in)"""
        partial_answer = "_" * len(clue.answer)
        if prefilled:
            return self._prefill_answer(clue, prefilled)
        else:
            return partial_answer
        
    def _pose_question(self, clue: Clue, prefilled: str=None) -> tuple:
        """Convert (raw) line from txt file to Clue()"""
        partial_answer = self._partial_answer(clue, prefilled)
        stdin = input(f"({clue.day}, {clue.date}) {clue.question} = {partial_answer} ({len(clue.answer)} letters) ", ).strip()
        if stdin.upper() == "EXIT":
            toggle = False
        elif stdin.upper() == clue.answer.upper():
            print("Correct!")
            toggle = True
        else:
            print(f"Wrong! Answer is {clue.answer}")
            toggle = True
        return toggle, clue
    
    def update_method(self, method: str) -> None:
        """Changes method of filtering questions"""
        self.method = method
    
    def _question_filter(filter, *args, **kwargs) -> str:
        """
        Filter questions (potentially randomly) to extract lines from clue_data.txt
        'filter' is a function which specifies how specifies how questions should be chosen
        Returns raw string from JSON file 
        """
        @functools.wraps(filter)
        def filter_wrap(self, *args, **kwargs) -> None:
            return filter(self, *args, **kwargs)
        return filter_wrap

    @_question_filter
    def qchoice(self, clue: Clue, prefilled: str=None) -> tuple:
        return self._pose_question(clue, prefilled)

    @_question_filter
    def qchoice_randomly(self, iostream, prefilled: str=None) -> Clue:
        """
        Choose clues randomly
        Note that calling/doing anything with iostream before calling iostream.readlines() removes stream and leads to error
        """
        spec = np.random.randint(109656) # Random int on [0 - approx. len(iostream)] # change this at some point
        line = iostream.readlines()[spec] 
        return self._pose_question(self._line2clue(line), prefilled)

if __name__ == "__main__":
    pass