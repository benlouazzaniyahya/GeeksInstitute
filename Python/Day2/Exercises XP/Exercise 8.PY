# ex8_star_wars_quiz.py
def run_quiz(data):
    """
    Ask questions to the user, track correct/incorrect answers.
    Return tuple (correct_count, wrong_count, wrong_answers_list)
    where wrong_answers_list contains tuples (question, user_answer, correct_answer).
    """
    correct = 0
    wrong = 0
    wrong_answers = []
    for item in data:
        q = item["question"]
        a = item["answer"]
        user_ans = input(q + " ").strip()
        if user_ans.lower() == a.lower():
            print("Correct!\n")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is: {a}\n")
            wrong += 1
            wrong_answers.append((q, user_ans, a))
    return correct, wrong, wrong_answers

def show_results(correct, wrong, wrong_answers):
    """Print the quiz summary and list wrong answers if any."""
    print("=== Quiz Results ===")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {wrong}")
    if wrong_answers:
        print("\nQuestions you got wrong:")
        for q, user, correct_ans in wrong_answers:
            print(f"Q: {q}")
            print(f"Your answer: {user or '(no answer)'}")
            print(f"Correct answer: {correct_ans}")
            print("-" * 20)

if __name__ == "__main__":
    data = [
        {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
        {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
        {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
        {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
        {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
        {"question": "What species is Chewbacca?", "answer": "Wookiee"},
    ]

    while True:
        correct, wrong, wrong_answers = run_quiz(data)
        show_results(correct, wrong, wrong_answers)

        if wrong > 3:
            again = input("\nYou had more than 3 wrong answers. Do you want to play again? (y/n): ").strip().lower()
            if again == "y":
                print("\nStarting a new quiz!\n")
                continue
        break

    print("\nThanks for playing the Star Wars Quiz!")
