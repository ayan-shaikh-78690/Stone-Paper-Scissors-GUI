import tkinter as tk
import random

# --- Game Setup ---
choices = {1: "Stone", 0: "Paper", -1: "Scissors"}

score = {"win": 0, "lose": 0, "draw": 0}
rounds_played = 0
max_rounds = 5

# --- Colors ---
BG_MAIN = "#f7f7ff"       # Soft off-white
BG_CARD = "#e4ecf1"       # Light pastel blue-gray
BTN_COLOR = "#7f5af0"     # Soft purple
BTN_HOVER = "#6b4cd6"     # Darker purple on hover
RESULT_WIN = "#4caf50"    # Green
RESULT_LOSE = "#e63946"   # Red
RESULT_DRAW = "#ffb703"   # Yellow-orange
TEXT_COLOR = "#2b2d42"    # Dark gray

# --- Functions ---
def play(user_choice):
    global rounds_played
    if rounds_played >= max_rounds:
        result_label.config(text="Game over! Click Restart.", fg=RESULT_DRAW)
        return

    user = user_choice
    computer = random.choice([1, 0, -1])

    user_label.config(text=f"You chose: {choices[user]}")
    computer_label.config(text=f"Computer chose: {choices[computer]}")

    if user == computer:
        result = "🤝 It's a draw!"
        score["draw"] += 1
        result_label.config(fg=RESULT_DRAW)
    else:
        if (user - computer) % 3 == 2:
            result = "🎉 You win!"
            score["win"] += 1
            result_label.config(fg=RESULT_WIN)
        else:
            result = "😢 You lose!"
            score["lose"] += 1
            result_label.config(fg=RESULT_LOSE)

    result_label.config(text=result)
    rounds_played += 1
    update_score()

    if rounds_played == max_rounds:
        if score["win"] > score["lose"]:
            final_result.config(text="🏆 You WON the game!", fg=RESULT_WIN)
        elif score["win"] < score["lose"]:
            final_result.config(text="💀 You LOST the game!", fg=RESULT_LOSE)
        else:
            final_result.config(text="🤝 It's a TIE!", fg=RESULT_DRAW)

def update_score():
    score_label.config(
        text=f"✅ Wins: {score['win']}   ❌ Losses: {score['lose']}   ⚖️ Draws: {score['draw']}"
    )

def reset_game():
    global rounds_played, score
    score = {"win": 0, "lose": 0, "draw": 0}
    rounds_played = 0
    user_label.config(text="")
    computer_label.config(text="")
    result_label.config(text="")
    final_result.config(text="")
    update_score()

def on_enter(e):
    e.widget.config(bg=BTN_HOVER)

def on_leave(e):
    e.widget.config(bg=BTN_COLOR)

# --- GUI Setup ---
window = tk.Tk()
window.title("🎮 Stone Paper Scissors")
window.geometry("420x520")
window.configure(bg=BG_MAIN)

# Heading
tk.Label(
    window, text="Stone 🪨  Paper 📄  Scissors ✂️",
    font=("Helvetica", 20, "bold"),
    bg=BG_MAIN, fg=TEXT_COLOR
).pack(pady=10)

# Buttons frame with card-like background (fill x so buttons can expand)
button_frame = tk.Frame(window, bg=BG_CARD, bd=0, relief="ridge")
button_frame.pack(pady=15, padx=20, fill="x")

# Make all 3 columns share available width equally
for i in range(3):
    button_frame.columnconfigure(i, weight=1, uniform="col")

# Button style: removed fixed width so grid/sticky controls sizing
btn_style = {
    "font": ("Arial", 12, "bold"),
    "bg": BTN_COLOR,
    "fg": "white",
    "bd": 0,
    "relief": "flat",
    "activebackground": BTN_HOVER,
    "padx": 8,
    "pady": 8,
}

stone_btn = tk.Button(button_frame, text="🪨 Stone", command=lambda: play(1), **btn_style)
paper_btn = tk.Button(button_frame, text="📄 Paper", command=lambda: play(0), **btn_style)
scissors_btn = tk.Button(button_frame, text="✂️ Scissors", command=lambda: play(-1), **btn_style)

# Use sticky='ew' so buttons expand to fill their grid cell
stone_btn.grid(row=0, column=0, padx=6, pady=10, sticky="ew")
paper_btn.grid(row=0, column=1, padx=6, pady=10, sticky="ew")
scissors_btn.grid(row=0, column=2, padx=6, pady=10, sticky="ew")

# Hover effect
for btn in (stone_btn, paper_btn, scissors_btn):
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Labels
user_label = tk.Label(window, text="", font=("Arial", 12), bg=BG_MAIN, fg=TEXT_COLOR)
user_label.pack()

computer_label = tk.Label(window, text="", font=("Arial", 12), bg=BG_MAIN, fg=TEXT_COLOR)
computer_label.pack()

result_label = tk.Label(window, text="", font=("Arial", 15, "bold"), bg=BG_MAIN)
result_label.pack(pady=10)

# Scoreboard
score_label = tk.Label(window, text="", font=("Arial", 12, "bold"), bg=BG_MAIN, fg="#0077b6")
score_label.pack()

final_result = tk.Label(window, text="", font=("Arial", 15, "bold"), bg=BG_MAIN)
final_result.pack(pady=10)

# Restart Button
restart_btn = tk.Button(window, text="🔁 Restart Game", font=("Arial", 12, "bold"),
                        bg="#ff7b00", fg="white", bd=0, relief="flat", command=reset_game)
restart_btn.pack(pady=15)
restart_btn.bind("<Enter>", lambda e: restart_btn.config(bg="#e76f00"))
restart_btn.bind("<Leave>", lambda e: restart_btn.config(bg="#ff7b00"))

# Initialize score display
update_score()

# Run
window.mainloop()
