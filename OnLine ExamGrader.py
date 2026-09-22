from abc import ABC, abstractmethod

class Question (ABC):
    def __init__ (self,text,correct_answere):
        self.text = text
        self.correct_answere =  correct_answere

    @abstractmethod
    def check_answer(self, student_answere):
        pass

class MCQQuestion(Question):
    def check_answer(self, student_answere):
        return student_answere.strip().lower() == self.correct_answere.strip().lower()
    

