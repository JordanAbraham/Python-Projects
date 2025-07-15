import tkinter as tk
from tkinter import messagebox
import random
import json
import time

# Full question bank
question_bank = {
    "General Knowledge": [
        {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
        {"question": "Which country invented tea?", "options": ["India", "England", "China", "Japan"], "answer": "China"},
        {"question": "What is the largest ocean?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
        {"question": "Which year did World War II end?", "options": ["1945", "1944", "1939", "1950"], "answer": "1945"},
        {"question": "What is the tallest mountain?", "options": ["K2", "Everest", "Kangchenjunga", "Makalu"], "answer": "Everest"},
        {"question": "Currency of Japan?", "options": ["Yen", "Won", "Dollar", "Ruble"], "answer": "Yen"},
        {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7"},
        {"question": "Smallest country in the world?", "options": ["Monaco", "Vatican", "Nauru", "Malta"], "answer": "Vatican"},
        {"question": "Bird known for mimicry?", "options": ["Parrot", "Crow", "Peacock", "Sparrow"], "answer": "Parrot"},
        {"question": "First man on the Moon?", "options": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Alan Shepard"], "answer": "Neil Armstrong"}
    ],
    "Science": [
        {"question": "What is H2O?", "options": ["Hydrogen", "Oxygen", "Water", "Acid"], "answer": "Water"},
        {"question": "Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
        {"question": "Gas absorbed by plants?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
        {"question": "Speed of light?", "options": ["300,000 km/s", "150,000 km/s", "100,000 km/s", "250,000 km/s"], "answer": "300,000 km/s"},
        {"question": "Vitamin from sunlight?", "options": ["A", "B", "C", "D"], "answer": "D"},
        {"question": "Smallest unit of life?", "options": ["Tissue", "Organ", "Cell", "Organism"], "answer": "Cell"},
        {"question": "Organ that controls the body?", "options": ["Heart", "Lungs", "Liver", "Brain"], "answer": "Brain"},
        {"question": "Symbol of gold?", "options": ["Au", "Ag", "Go", "Gd"], "answer": "Au"},
        {"question": "Planet with rings?", "options": ["Earth", "Mars", "Saturn", "Venus"], "answer": "Saturn"},
        {"question": "Boiling point of water?", "options": ["90°C", "80°C", "100°C", "120°C"], "answer": "100°C"}
    ],
    "Math": [
        {"question": "5 + 7 =", "options": ["10", "11", "12", "13"], "answer": "12"},
        {"question": "9 x 3 =", "options": ["27", "28", "26", "30"], "answer": "27"},
        {"question": "√49?", "options": ["6", "7", "8", "9"], "answer": "7"},
        {"question": "Value of π?", "options": ["3.14", "2.17", "4.21", "1.61"], "answer": "3.14"},
        {"question": "20 ÷ 4 =", "options": ["6", "5", "4", "3"], "answer": "5"},
        {"question": "10^2 =", "options": ["10", "20", "100", "200"], "answer": "100"},
        {"question": "25% of 100?", "options": ["10", "20", "25", "50"], "answer": "25"},
        {"question": "12 ÷ 3 =", "options": ["2", "3", "4", "6"], "answer": "4"},
        {"question": "Factor of 15?", "options": ["2", "3", "6", "8"], "answer": "3"},
        {"question": "Odd number?", "options": ["4", "6", "8", "7"], "answer": "7"}
    ],
    "History": [
        {"question": "Who discovered America?", "options": ["Columbus", "Magellan", "Cook", "Da Gama"], "answer": "Columbus"},
        {"question": "First US President?", "options": ["Lincoln", "Jefferson", "Washington", "Roosevelt"], "answer": "Washington"},
        {"question": "US Independence Day?", "options": ["July 4", "Jan 26", "Oct 2", "Aug 15"], "answer": "July 4"},
        {"question": "Great Wall is in?", "options": ["India", "China", "Japan", "Korea"], "answer": "China"},
        {"question": "Who was Napoleon?", "options": ["King", "Warrior", "General", "President"], "answer": "General"},
        {"question": "WWI started in?", "options": ["1914", "1939", "1945", "1920"], "answer": "1914"},
        {"question": "Mahatma Gandhi led?", "options": ["US", "India", "Africa", "UK"], "answer": "India"},
        {"question": "Taj Mahal built by?", "options": ["Shah Jahan", "Akbar", "Babur", "Aurangzeb"], "answer": "Shah Jahan"},
        {"question": "Fall of Roman Empire?", "options": ["400 AD", "476 AD", "500 AD", "600 AD"], "answer": "476 AD"},
        {"question": "First human in space?", "options": ["Armstrong", "Gagarin", "Glenn", "Collins"], "answer": "Gagarin"}
    ],
    "Technology": [
        {"question": "Founder of Microsoft?", "options": ["Jobs", "Musk", "Gates", "Zuckerberg"], "answer": "Gates"},
        {"question": "What is RAM?", "options": ["Storage", "Memory", "Input", "Output"], "answer": "Memory"},
        {"question": "Language for web?", "options": ["Python", "C++", "HTML", "Java"], "answer": "HTML"},
        {"question": "iPhone launched in?", "options": ["2005", "2006", "2007", "2008"], "answer": "2007"},
        {"question": "Android is owned by?", "options": ["Apple", "Samsung", "Microsoft", "Google"], "answer": "Google"},
        {"question": "Full form of CPU?", "options": ["Core Processing Unit", "Central Processing Unit", "Computer Power Unit", "Central Power Unit"], "answer": "Central Processing Unit"},
        {"question": "Google Chrome is a?", "options": ["OS", "App", "Browser", "Compiler"], "answer": "Browser"},
        {"question": "Programming language?", "options": ["HTML", "CSS", "Python", "SQL"], "answer": "Python"},
        {"question": "Tesla owned by?", "options": ["Bezos", "Musk", "Cook", "Zuckerberg"], "answer": "Musk"},
        {"question": "macOS made by?", "options": ["Microsoft", "Google", "Apple", "IBM"], "answer": "Apple"}
    ]
}

SCORE_FILE = "high_scores.json"

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.center_window(700, 450)

        self.username = tk.StringVar()
        self.category = tk.StringVar()
        self.score = 0
        self.q_index = 0
        self.questions = []
        self.user_answers = []
        self.timer_seconds = 15
        self.timer_id = None
        self.dark_mode = False

        self.show_splash_screen()

    def center_window(self, w, h):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (w // 2)
        y = (screen_height // 2) - (h // 2)
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    def show_splash_screen(self):
        self.root.withdraw()
        splash = tk.Toplevel()
        splash.overrideredirect(True)
        splash.configure(bg="white")

        sw, sh = splash.winfo_screenwidth(), splash.winfo_screenheight()
        x, y = (sw - 400) // 2, (sh - 250) // 2
        splash.geometry(f"400x250+{x}+{y}")

        tk.Label(splash, text="🧠 Quiz Game", font=("Arial", 22, "bold"), bg="white").pack(pady=30)
        tk.Label(splash, text="Loading, please wait...", font=("Arial", 12), bg="white").pack(pady=10)
        tk.Label(splash, text="Made by Jordan", font=("Arial", 10), bg="white").pack(side="bottom", pady=10)

        self.root.after(2500, lambda: [splash.destroy(), self.root.deiconify(), self.ask_username()])

    def ask_username(self):
        self.clear_window()
        self.set_theme()
        tk.Label(self.root, text="Enter Your Name", font=("Arial", 16)).pack(pady=30)
        tk.Entry(self.root, textvariable=self.username, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Continue", command=self.show_category_selection, font=("Arial", 14)).pack(pady=20)

    def show_category_selection(self):
        if not self.username.get():
            messagebox.showwarning("Warning", "Please enter your name.")
            return

        self.clear_window()
        self.set_theme()
        tk.Label(self.root, text=f"Hello {self.username.get()}!\nSelect Category", font=("Arial", 18)).pack(pady=20)
        for cat in question_bank.keys():
            tk.Radiobutton(self.root, text=cat, variable=self.category, value=cat, font=("Arial", 14)).pack(anchor="w", padx=100)

        tk.Button(self.root, text="Start Quiz", command=self.start_quiz, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Toggle Dark Mode", command=self.toggle_theme, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="View Analytics", command=self.show_analytics, font=("Arial", 12)).pack(pady=5)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.set_theme()
        self.show_category_selection()

    def set_theme(self):
        bg = "#1e1e1e" if self.dark_mode else "SystemButtonFace"
        fg = "white" if self.dark_mode else "black"

        self.root.configure(bg=bg)

        def apply_theme(widget):
            try:
                widget.configure(bg=bg, fg=fg)
            except:
                pass
            for child in widget.winfo_children():
                apply_theme(child)

        apply_theme(self.root)

    def start_quiz(self):
        if not self.category.get():
            messagebox.showwarning("Warning", "Please select a category.")
            return
        self.questions = random.sample(question_bank[self.category.get()], 10)
        self.score = 0
        self.q_index = 0
        self.user_answers = []
        self.show_question()

    def show_question(self):
        self.clear_window()

        if self.q_index >= len(self.questions):
            self.end_quiz()
            return

        self.timer_seconds = 15
        q_data = self.questions[self.q_index]
        tk.Label(self.root, text=f"Q{self.q_index + 1}. {q_data['question']}", font=("Arial", 16), wraplength=600,
                 justify="left").pack(pady=20)

        self.selected_option = tk.StringVar()

        select_color = "#444444" if self.dark_mode else "SystemButtonFace"
        for opt in q_data["options"]:
            tk.Radiobutton(
                self.root,
                text=opt,
                variable=self.selected_option,
                value=opt,
                font=("Arial", 14),
                selectcolor=select_color,
                bg="#1e1e1e" if self.dark_mode else "SystemButtonFace",
                fg="white" if self.dark_mode else "black",
                activebackground="#1e1e1e" if self.dark_mode else "SystemButtonFace",
                activeforeground="white" if self.dark_mode else "black"
            ).pack(anchor="w", padx=80)

        self.timer_label = tk.Label(self.root, text=f"Time left: {self.timer_seconds}s", font=("Arial", 12))
        self.timer_label.pack(pady=10)
        self.countdown()

        tk.Button(self.root, text="Submit", command=self.submit_answer, font=("Arial", 12)).pack(side="left", padx=60,
                                                                                                 pady=20)
        tk.Button(self.root, text="Skip", command=self.skip_question, font=("Arial", 12)).pack(side="right", padx=60,
                                                                                               pady=20)

        self.set_theme()

    def countdown(self):
        self.timer_label.config(text=f"Time left: {self.timer_seconds}s")
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.timer_id = self.root.after(1000, self.countdown)
        else:
            self.submit_answer(auto=True)

    def submit_answer(self, auto=False):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        selected = self.selected_option.get() if not auto else "Skipped"
        self.user_answers.append(selected)

        correct_answer = self.questions[self.q_index]["answer"]
        if selected == correct_answer:
            self.score += 1

        self.q_index += 1
        self.show_question()

    def skip_question(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.user_answers.append("Skipped")
        self.q_index += 1
        self.show_question()

    def end_quiz(self):
        self.clear_window()
        self.set_theme()
        tk.Label(self.root, text="Quiz Finished!", font=("Arial", 20)).pack(pady=20)
        tk.Label(self.root, text=f"{self.username.get()}, your score: {self.score}/10", font=("Arial", 16)).pack(pady=10)

        self.save_score()

        tk.Button(self.root, text="Review Answers", command=self.review_answers, font=("Arial", 12)).pack(pady=5)
        tk.Button(self.root, text="Leaderboard", command=self.show_leaderboard, font=("Arial", 12)).pack(pady=5)
        tk.Button(self.root, text="Play Again", command=self.ask_username, font=("Arial", 12)).pack(pady=5)

    def show_leaderboard(self):
        self.clear_window()
        self.set_theme()
        tk.Label(self.root, text="Leaderboard (Top 5)", font=("Arial", 18)).pack(pady=10)

        try:
            with open(SCORE_FILE, "r") as file:
                scores = json.load(file)
        except:
            scores = []

        top_scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:5]

        for i, entry in enumerate(top_scores):
            username = entry.get("username", "Unknown")
            score = entry.get("score", 0)
            category = entry.get("category", "N/A")
            text = f"{i + 1}. {username} - {score} ({category})"
            tk.Label(self.root, text=text, font=("Arial", 12)).pack()

        tk.Button(self.root, text="Back to Menu", command=self.show_category_selection, font=("Arial", 12)).pack(pady=10)

    def review_answers(self):
        self.clear_window()
        self.set_theme()

        canvas = tk.Canvas(self.root, width=680, height=370)
        frame = tk.Frame(canvas)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        tk.Label(frame, text="Review Answers", font=("Arial", 18)).pack(pady=10)

        for i, q in enumerate(self.questions):
            correct = q["answer"]
            user = self.user_answers[i]
            color = "green" if user == correct else "red" if user != "Skipped" else "orange"

            text = f"{i+1}. {q['question']}\nYour Answer: {user}\nCorrect Answer: {correct}"
            tk.Label(frame, text=text, fg=color, font=("Arial", 12), wraplength=640, justify="left").pack(pady=10, anchor="w")

        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        tk.Button(self.root, text="Back to Menu", command=self.show_category_selection, font=("Arial", 12)).pack(pady=10)

    def show_analytics(self):
        self.clear_window()
        self.set_theme()
        tk.Label(self.root, text="Quiz Analytics", font=("Arial", 18)).pack(pady=10)

        try:
            with open(SCORE_FILE, "r") as file:
                scores = json.load(file)
        except:
            scores = []

        user_scores = [s for s in scores if s.get('username') == self.username.get()]
        avg_score = sum([s['score'] for s in user_scores]) / len(user_scores) if user_scores else 0
        most_played = {}
        for s in user_scores:
            cat = s['category']
            most_played[cat] = most_played.get(cat, 0) + 1
        most_played_category = max(most_played, key=most_played.get) if most_played else "N/A"

        tk.Label(self.root, text=f"Total Attempts: {len(user_scores)}", font=("Arial", 12)).pack()
        tk.Label(self.root, text=f"Average Score: {avg_score:.2f}", font=("Arial", 12)).pack()
        tk.Label(self.root, text=f"Most Played Category: {most_played_category}", font=("Arial", 12)).pack()

        tk.Button(self.root, text="Back to Menu", command=self.show_category_selection, font=("Arial", 12)).pack(pady=10)

    def save_score(self):
        try:
            with open(SCORE_FILE, "r") as file:
                scores = json.load(file)
        except:
            scores = []

        scores.append({"username": self.username.get(), "category": self.category.get(), "score": self.score, "timestamp": time.ctime()})

        with open(SCORE_FILE, "w") as file:
            json.dump(scores, file, indent=4)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
