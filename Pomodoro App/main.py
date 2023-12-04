from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
checkmark = ""
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global rep, checkmark
    try:
        screen.after_cancel(timer)
    #   catches pressing the reset button before we've had a chance to re-assign timer
    except ValueError:
        pass
    # reset all configurations and constants that drives main functionality
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    rep = 0
    checkmark = ""
    completion_checkmark.config(text=checkmark)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
# timer function i.e everytime we press start, this func is triggered, which in turn triggers count down func
def start_timer():
    global rep
    rep += 1
    # Long breaks occur on every 8th iteration, short after most work sess and work every other time
    if rep % 8 == 0:
        time = LONG_BREAK_MIN
        timer_label.config(text="Long Break", fg=RED)
    elif rep % 2 == 0:
        time = SHORT_BREAK_MIN
        timer_label.config(text="Short Break", fg=PINK)
    else:
        time = WORK_MIN
        timer_label.config(text="Working")
    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global rep
    global timer
    global checkmark
    if count >= 0:
        time_min = count // 60
        time_secs = count % 60
        if time_secs < 10:
            time_secs = f"0{time_secs}"
        canvas.itemconfig(timer_text, text=f"{time_min}:{time_secs}")
        timer = screen.after(1000, count_down, count - 1)
    else:
        # Increase checkmark after every work session. After count down is complete
        if rep % 2 == 1:
            checkmark += "✅"
            completion_checkmark.config(text=checkmark)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro App")
screen.config(bg=YELLOW, padx=100, pady=50)

# let's set up the canvas as follows
photo_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=photo_img)
timer_text = canvas.create_text(112, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)

# timer label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold italic"))
timer_label.grid(column=1, row=0)
# start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
# reset button
reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(column=2, row=2)
# completion checkmark
completion_checkmark = Label(fg=GREEN, bg=YELLOW)
completion_checkmark.grid(column=1, row=3)

screen.mainloop()
