import tkinter as tk
from tkinter import messagebox
import random

# Riddle and answers with hints
riddles = [
    ("I speak without a mouth and hear without ears. I have nobody, but I come alive with the wind. What am I?", "echo", "It bounces back."),
    ("The more of me you take, the more you leave behind. What am I?", "footsteps", "Think about walking."),
    ("I’m tall when I’m young, and I’m short when I’m old. What am I?", "candle", "It burns down."),
    ("I’m always in front of you but can’t be seen. What am I?", "future", "It hasn’t happened yet."),
    ("I have keys but no locks. I have space but no rooms. You can enter but can’t go outside. What am I?", "keyboard", "You are using it right now!"),
]

class RiddleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Riddle Challenge Game 🧩")
        self.root.geometry("550x350")
        self.root.configure(bg="#f0f0f0")

        self.score = 0
        self.high_score = 0
        self.current_riddle = None
        self.timer = 15
        self.timer_id = None

        self.label = tk.Label(root, text="Welcome to the Riddle Challenge!", font=("Arial", 14), bg="#f0f0f0", wraplength=500)
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 12), width=40)
        self.entry.pack(pady=10)

        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack()

        self.check_button = tk.Button(button_frame, text="Check Answer", font=("Arial", 12), command=self.check_answer)
        self.check_button.grid(row=0, column=0, padx=5)

        self.next_button = tk.Button(button_frame, text="Next Riddle", font=("Arial", 12), command=self.next_riddle)
        self.next_button.grid(row=0, column=1, padx=5)

        self.hint_button = tk.Button(button_frame, text="Hint 💡", font=("Arial", 12), command=self.show_hint)
        self.hint_button.grid(row=0, column=2, padx=5)

        self.score_label = tk.Label(root, text="Score: 0 | High Score: 0", font=("Arial", 12), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        self.timer_label = tk.Label(root, text="Time left: 15s", font=("Arial", 12, "bold"), fg="red", bg="#f0f0f0")
        self.timer_label.pack(pady=5)

        self.next_riddle()

    def next_riddle(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        self.entry.delete(0, tk.END)
        self.current_riddle = random.choice(riddles)
        self.label.config(text=self.current_riddle[0])
        self.timer = 15
        self.update_timer()

    def check_answer(self):
        answer = self.entry.get().strip().lower()
        if answer == self.current_riddle[1]:
            self.score += 1
            messagebox.showinfo("Correct!", "🎉 That's right!")
        else:
            messagebox.showerror("Wrong!", f"❌ The correct answer was: {self.current_riddle[1]}")
        self.update_score()
        self.next_riddle()

    def show_hint(self):
        messagebox.showinfo("Hint 💡", self.current_riddle[2])
        self.score = max(0, self.score - 1)  # Deduct points for hint
        self.update_score()

    def update_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score_label.config(text=f"Score: {self.score} | High Score: {self.high_score}")

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.timer}s")
        if self.timer > 0:
            self.timer -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            messagebox.showwarning("Time's up!", f"⏰ The correct answer was: {self.current_riddle[1]}")
            self.next_riddle()

# Run the game
root = tk.Tk()
app = RiddleGame(root)
root.mainloop()
