import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1#25
SHORT_BREAK_MIN = 1#5
LONG_BREAK_MIN = 20
TOMATO_IMAGE = "Bootcamp - Python/Day 28 - TKinter, Dynamic Typing and the Pomodoro GUI Application/Pomodoro Project/tomato.png"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_txt.config(text='Timer')
    checks.config(text='')
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps > 7: # 20min Break | Reset reps.
        reps = 0
        title_txt.config(text='Break', fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0: # 5min Break | Reps +1.
        title_txt.config(text='Break', fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else: # 25min Work | Reps +1
        title_txt.config(text='Work', fg=GREEN)
        countdown(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f'0{sec}'
    canvas.itemconfig(timer_text, text=f'{min}:{sec}')
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        checks.config(text='✔' * math.floor(reps/2))
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label | Title
title_txt = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40), bg=YELLOW, highlightthickness=0)
title_txt.grid(column=1, row=0)

# Canvas | Tomato
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file=TOMATO_IMAGE)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill='white', font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Button | Start
start = tk.Button(text='Start', command=start_timer, highlightthickness=0)
start.grid(column=0, row=2)

# Button | Reset
reset = tk.Button(text='Reset', command=reset_timer, highlightthickness=0)
reset.grid(column=2, row=2)

# Label | Checks ✔
checks = tk.Label(text='', fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 40, "bold"))
checks.grid(column=1, row=3)

window.mainloop()