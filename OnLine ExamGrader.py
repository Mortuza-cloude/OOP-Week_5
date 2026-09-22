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
class TrueFalseQuestion(Question):
    def check_answer(self, student_answere):
        student_bool = student_answere.strip().lower() in ("true", "t", "yes")
        correct_bool = self.correct_answere.strip() . lower() in ("true", "t", "yes")
        return student_bool == correct_bool
def main():
    questions = []

    while True:
        q_type = input("Question type(mcq/tf, or 'done' to finish):")
        if q_type == "done":
            break
        text = input ("Question text:")
        correct = input("Correct answere")
        student = input("Student aswere")

        if q_type == "mcq":
            q = MCQQuestion(text,correct)
        elif q_type == "tf":
            q =TrueFalseQuestion(text,correct)
        else:
            print ("Unknown question type, skipping")
            continue
        q._student_answere = student
        questions.append(q)
    score = 0
    for i ,q in enumerate(questions,start =1):
        if q.check_answere(q._student_answere):
            print(f"Q{i}: Correct!")
            score+=1
        else:
            print(f"Q{i}: Incorrect.Correct answere: {q.correct_answere}")
    print (f"Final Score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()

