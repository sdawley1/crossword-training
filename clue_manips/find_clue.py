"""
Script for randomly choosing and displaying a clue

TO-DO LIST:
-----------
- Fix relative path name in JSONParser.filter_questions() when opening .txt file
    - Right now it assumes we run script from HOME DIRECTORY
- Add more filters for choosing questions
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
    
    def _pose_question(self, line: str) -> Clue:
        """Convert (raw) line from txt file to Clue()"""
        question, answer, alignment, author, weekday, date = line.strip("\n").split("0x1F")
        stdin = input(f"({weekday}, {date}) {question} = {'_'*len(answer)} ({len(answer)} letters) ", )
        if stdin.upper() == answer.upper():
            print("Great!")
        elif stdin.upper() == "EXIT":
            toggle = False
        else:
            print(f"Wrong! Answer is {answer}")
            toggle = True

        return toggle, Clue(question, answer, alignment, author, weekday, date)
    
    def update_method(self, method: str) -> None:
        "Changes method of filtering questions"
        self.method = method
    
    def _question_filter(filter) -> str:
        """
        Filter questions (potentially randomly) to extract
        'filter' is a function which specifies how specifies how questions should be chosen
        Returns raw string from JSON file 
        """
        @functools.wraps(filter)
        def filter_wrap(self, *args) -> None:
            return filter(self, *args)
        return filter_wrap

    @_question_filter
    def qchoice_randomly(self, iostream) -> Clue:
        """Choose clues randomly"""
        for line in iostream.readlines():
            if np.random.random() > 0.99:
                return self._pose_question(line)

    @_question_filter
    def qchoice_by_weekday(self, iostream, day: str) -> Clue:
        """Choose clues based only on day of week they were published"""
        for line in iostream.readlines():
            if day.upper() in line.upper():
                return self._line2clue(line)
    
    @_question_filter
    def qchoice_by_difficulty(self, iostream, difficulty: str) -> Clue:
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
                return self._line2clue(line)


if __name__ == "__main__":
    parser = JSONParser("./web_scraping/clue_data.txt", method="weekday")
    with open(parser.filename, "r") as f:
        # parser.qchoice_randomly(f)
        # parser.qchoice_by_weekday(f, "tuesday")
        parser.qchoice_by_difficulty(f, "expert")