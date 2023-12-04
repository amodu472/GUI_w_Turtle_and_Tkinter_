from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Create an empty list 'bank' of questions
question_bank = []

# populate the 'bank' with questions from the data file/module
for question in question_data:
    q, a = question["text"], question["answer"]
    new_question = Question(q, a)
    question_bank.append(new_question)

# Initialize our QuizBrain with the question bank which is a list of questions and their corresponding answers
quiz = QuizBrain(question_bank)

# Check if the quiz obj still has questions using the still_has_questions method
while quiz.still_has_questions():
    print(quiz.next_question())
    continue_ = input("Would you like to continue? 'y' or 'yes' ").lower()
    if continue_ == "y" or continue_ == "yes":
        continue
    else:
        break

# Print final score once the while loop exits (i.e. after the quiz has been completed)
print(f"Final score: You got {quiz.score}/{quiz.question_num} correct.")
