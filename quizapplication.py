import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("400x300")
        
        # Initialize the quiz data
        self.quiz_data = self._get_quiz_data()

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=('Arial', 14))
        self.question_label.pack(pady=20)

        self.var = tk.IntVar()
        
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.var, value=i, font=('Arial', 12))
            btn.pack(anchor='w')
            self.option_buttons.append(btn)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        self.update_question()

    def _get_quiz_data(self):
        """Encapsulated quiz data (not visible outside the class)."""
        return [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "answer": 0
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": 1
            },
            {
                "question": "What is the square root of 64?",
                "options": ["6", "7", "8", "9"],
                "answer": 2
            },
            {
                "question": "Who wrote 'Hamlet'?",
                "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "J.K. Rowling"],
                "answer": 2
            },
            {
                "question": "Which element has the chemical symbol 'O'?",
                "options": ["Oxygen", "Gold", "Silver", "Helium"],
                "answer": 0
            },
            {
                "question": "Who is the father of java? ",
                "options": ["James gosling", "thomas", "Rossum", "Elan helen"],
                "answer": 0
            },
            {
                "question": "what is the powerhouse of the cell ",
                "options": ["ribosome", "mitochondria", "Nucleus", "chloroplast"],
                "answer": 1
            },
            {
                "question": "what is the boiling point of water at sea level?",
                "options": ["50 degree celcius", "10 degree celcius", "100 degree celcius", "200 degree celcius"],
                "answer": 2

            },
            {
                "question": "if 3x=81,what is the value of x? ",
                "options": ["23", "27", "30", "9"],
                "answer": 3
            },
            {
                "question": "which country is known as land of the rising sun ",
                "options": ["south korea", "china", "thailand", "japan"],
                "answer": 3
            }      

        ]

    def update_question(self):
      
        current_q_data = self.quiz_data[self.current_question]
        self.question_label.config(text=current_q_data['question'])
        for i, option in enumerate(current_q_data['options']):
            self.option_buttons[i].config(text=option)
        self.var.set(-1)  
    def next_question(self):
        selected_option = self.var.get()
        if selected_option == -1:
            messagebox.showwarning("No option selected", "Please select an option before moving to the next question.")
            return

        if selected_option == self.quiz_data[self.current_question]['answer']:
            self.score += 1

        self.current_question += 1

        if self.current_question == len(self.quiz_data):
            self.show_result()
        else:
            self.update_question()

    def show_result(self):
        messagebox.showinfo("Quiz Complete", f"Your score is {self.score}/{len(self.quiz_data)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


