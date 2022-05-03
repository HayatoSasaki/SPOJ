from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = [Question(q['text'], q['answer']) for q in question_data]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the Quiz!\nYour final score was {quiz.score}/{quiz.question_number}.")