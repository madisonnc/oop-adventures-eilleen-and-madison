
import random

class TriviaGame:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "Who wrote 'Romeo and Juliet'?", "answer": "Shakespeare"},
            {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
            {"question": "Which animal is known as the 'King of the Jungle'?", "answer": "Lion"},
            {"question": "What is the chemical symbol for gold?", "answer": "Au"},
            {"question": "What is the name of the longest river in the world?", "answer": "Nile"},
            {"question": "Which ocean is the largest?", "answer": "Pacific"},
            {"question": "What is the largest desert in the world?", "answer": "Sahara"},
            {"question": "What is the national flower of Japan?", "answer": "cherry blossom"},
            {"question": "Which country is known as the Land of the Rising Sun?", "answer": "Japan"}
        ]
        self.score = 0 

    def ask_question(self, question):
        user_answer = input(question["question"] + " ").lower()  
        if user_answer.lower() == question["answer"].lower():
            print("correct!")
            self.score += 1 
        else:
            print(f"Wrong! The correct answer is {question['answer']}.")

    def play(self):
        selected_questions = random.sample(self.questions, 1)

        for question in selected_questions:
            self.ask_question(question)


if __name__ == "__main__":
    game = TriviaGame() 
    game.play()  
