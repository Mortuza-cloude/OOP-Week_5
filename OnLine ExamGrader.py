from abc import ABC, abstractmethod

class Question (ABC):
    def __init__ (self,text,correct_answere):
        self.text = text
        self.correct_answere =  correct_answere
        

