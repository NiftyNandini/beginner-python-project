import tkinter as tk
from tkinter import messagebox

# Sample questions for demonstration purposes
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Hemingway", "Austen", "Dickens"], "answer": "Shakespeare"},
    {"question": "What is the largest planet in our Solar System?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Jupiter"},
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personalized Quiz Game 🎮")
        self.root.geometry("500x400")
        self.root.config(bg='#2C2C2C')  # Matte dark background

        self.question_index = 0
        self.score = 0

        # GUI Elements
        self.question_label = tk.Label(root, text="", wraplength=450, font=("Arial", 14), bg='#2C2C2C', fg='#EAEAEA')
        self.question_label.pack(pady=20)

        self.option_var = tk.StringVar()

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.option_var, value="", font=("Arial", 12), bg='#2C2C2C', fg='#EAEAEA', selectcolor='#4A4A4A')
            rb.pack(anchor="w", pady=5)
            self.radio_buttons.append(rb)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 12), bg='#FF6F61', fg='#FFFFFF')
        self.submit_button.pack(pady=20)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 12), bg='#6FA3EF', fg='#FFFFFF')
        self.next_button.pack(pady=10)
        self.next_button.config(state=tk.DISABLED)

        self.load_question()

    def load_question(self):
        question = questions[self.question_index]
        self.question_label.config(text=question["question"])

        for i, option in enumerate(question["options"]):
            self.radio_buttons[i].config(text=option, value=option)

        self.option_var.set("")

    def check_answer(self):
        selected_option = self.option_var.get()
        if selected_option == questions[self.question_index]["answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", "Correct Answer!")
        else:
            messagebox.showinfo("Incorrect", f"Incorrect! The correct answer was: {questions[self.question_index]['answer']}")

        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.question_index += 1
        if self.question_index < len(questions):
            self.load_question()
            self.submit_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Quiz Completed", f"Your score is: {self.score}/{len(questions)}")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
