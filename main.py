from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")
current_card={}
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front)
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()
window=Tk()
window.title("Flash cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)
canvas=Canvas(height=525,width=800)
card_front=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front)
card_title=canvas.create_text(400,150,font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,font=("Arial",55,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_img=PhotoImage(file="images/wrong.png")
yes_button=Button(image=cross_img,highlightthickness=0,command=next_card)
yes_button.grid(row=1,column=0)

tick_img=PhotoImage(file="images/right.png")
no_button=Button(image=tick_img,highlightthickness=0,command=is_known)
no_button.grid(row=1,column=1)

next_card()
window.mainloop()
