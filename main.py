from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    #window.after_cancel(timer_text)
    canvas.itemconfig(timer_text, text=f"00:00")
    check_label.config(text="")
    welcome_label.config(text="Timer")
    reps = 1


    #title_lable Timer


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    if reps % 2 != 0:
        timer = WORK_MIN * 60
        welcome_label.config(text="Work", fg=GREEN)
        reps += 1
    elif reps % 2 == 0 and reps <= 4:
        timer = SHORT_BREAK_MIN * 60
        welcome_label.config(text="Short Break", fg=PINK)
        reps += 1
    elif reps == 8:
        timer = LONG_BREAK_MIN * 60
        welcome_label.config(text="Long Break", fg=RED)
        reps = 0

    count_down(timer)
    # count_down(15)
    # Hello World


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec <= 9:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps == 2:
            check_label.config(text="✔")
        elif reps == 4:
            check_label.config(text="✔✔")
        elif reps == 6:
            check_label.config(text="✔✔✔")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

welcome_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Courier", 40, "bold"))
welcome_label.grid(row=0, column=1)

check_label = Label(text="", bg=YELLOW, fg=GREEN, font=("Courier", 15, "normal"))
check_label.grid(row=3, column=1)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
