from question_model import Question
import json
from quiz_brain import QuizBrain


def start_quiz():
    question_bank = []
    data_file = open('data.json')
    question_data = json.load(data_file)

    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz.")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    start_quiz()
