from question_model import Questing
from data import question_data
from quiz_brain import Quiz_Brain

question_bank: list[Questing] = []
for question_set in question_data:
    question_bank.append( Questing(question_set["question"], question_set["correct_answer"]))


quiz = Quiz_Brain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")