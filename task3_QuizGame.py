import tkinter as tk
from tkinter import messagebox
from random import shuffle

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.questions = [
            {
                "question": "Which is the most sensitive organ in our body?",
                "options": ["Heart", "Eyes", "Skin", "Ears"],
                "answer": "Skin"
            },
            {
                "question": "What is the capital of France?",
                "options": ["London", "Paris", "Berlin", "Madrid"],
                "answer": "Paris"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Jupiter", "Mars", "Saturn"],
                "answer": "Jupiter"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
                "answer": "Leonardo da Vinci"
            },
            {
                "question": "What is the powerhouse of the cell?",
                "options": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic reticulum"],
                "answer": "Mitochondria"
            },
            {
                "question": "Which ocean is the largest?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"],
                "answer": "William Shakespeare"
            },
            {
                "question": "What is the national animal of India?",
                "options": ["Tiger", "Elephant", "Lion", "Leopard"],
                "answer": "Tiger"
            },
            {
                "question": "Which country is known as the Land of the Rising Sun?",
                "options": ["China", "Japan", "India", "Australia"],
                "answer": "Japan"
            },
            {
                "question": "What is the currency of Brazil?",
                "options": ["Peso", "Euro", "Dollar", "Real"],
                "answer": "Real"
            }
        ]

        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(self.root, text="", font=('Arial', 14), wraplength=400)
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=('Arial', 14), width=30, command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.score_label = tk.Label(self.root, text="Score: 0", font=('Arial', 12))
        self.score_label.pack(pady=20)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            options = question["options"]
            shuffle(options)

            for i in range(4):
                self.option_buttons[i].config(text=options[i])

            self.score_label.config(text="Score: {}".format(self.score))
        else:
            self.end_game()

    def check_answer(self, selected_option):
        question = self.questions[self.current_question]
        selected_answer = question["options"][selected_option]
        correct_answer = question["answer"]

        if selected_answer == correct_answer:
            self.score += 1

        self.current_question += 1
        self.next_question()

    def end_game(self):
        messagebox.showinfo("Game Over", "Quiz Ended\nYour Score: {}".format(self.score))
        self.root.destroy()


root = tk.Tk()


game = QuizGame(root)


root.mainloop()
