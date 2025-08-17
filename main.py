import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

win = tk.Tk()
win.title("Rock Paper Scissors")
win.geometry("1000x800")
win.config(bg="black")

gestures = ["rock", "paper", "scissors"]

my_score = 0
opp_score = 0

paper_img = Image.open("paper.PNG")
paper_img = paper_img.resize((120, 120))
paper_photo = ImageTk.PhotoImage(paper_img)

rock_img = Image.open("rock.PNG")
rock_img = rock_img.resize((120, 120))
rock_photo = ImageTk.PhotoImage(rock_img)

scissors_img = Image.open("scissors.PNG")
scissors_img = scissors_img.resize((120, 120))
scissors_photo = ImageTk.PhotoImage(scissors_img)

def show_scores():

    opp_points = Label(text=f"Opponent's  score: {opp_score}", font=("Helvetica", 28), bg="black", fg="white", pady=10)
    opp_points.pack(side=BOTTOM)

    my_points = Label(text=f"My score: {my_score}", font=("Helvetica", 28) , bg="black", fg="white", pady=10)
    my_points.pack(side=BOTTOM)

def to_play():
    play_button = Button(height=2, text="Click to play", font=("Helvetica", 13) , bg="black", fg="white", command=user_options)
    play_button.pack(side= TOP)

def clear_and_add_new():
    for widget in win.winfo_children():
        widget.destroy()

def user_options():
    clear_and_add_new()
    choose_prompt = Label(text="Choose wisely: Rock, Paper, or Scissors!", font=("Helvetica", 28) , bg="black", fg="white", pady=50)
    choose_prompt.pack(side=TOP)

    rock_button = Button(image=rock_photo, height=120, width=120, padx=120, command=rock_choice)
    rock_button.pack(side=TOP)

    paper_button = Button(image=paper_photo, height=120, width=120, padx=120, command=paper_choice)
    paper_button.pack(side=TOP)

    scissors_button = Button(image=scissors_photo, height=120, width=120, padx=120, command=scissors_choice)
    scissors_button.pack(side=TOP)

def computer_choice():
    random_num = random.randint(0,2)
    return random_num

def vs_prompt():
    versus_prompt = Label(text="VS.", font=("Helvetica", 30), bg="black", fg="white", pady=20)
    versus_prompt.pack(side=TOP)

def rock_choice():
    clear_and_add_new()
    global opp_score,my_score

    rock_prompt = Label(text="You chose Rock.", font=("Helvetica", 28), bg="black",fg="white", pady=20)
    rock_prompt.pack(side=TOP)
    opp_choice = computer_choice()

    show_rock = Label(image=rock_photo, height=120, width=120)
    show_rock.pack(side=TOP)

    vs_prompt()

    opponent_prompt = Label(text=f"Opponent chose {gestures[opp_choice]}.", font=("Helvetica", 28), bg="black",fg="white", pady=20)
    opponent_prompt.pack(side=TOP)

    if opp_choice == 0:

        show_opponent = Label(image=rock_photo, height=120, width=120)
        show_opponent.pack(side=TOP)

        winner_is =  Label(text="It's a tie.", font=("Helvetica", 28), bg="black",fg="white", pady=20)
        winner_is.pack(side=TOP)
    elif opp_choice == 1:

        show_opponent = Label(image=paper_photo, height=120, width=120)
        show_opponent.pack(side=TOP)

        winner_is = Label(text="Paper beats rock. You Lose!.", font=("Helvetica", 28), bg="black", fg="white", pady=20)
        winner_is.pack(side=TOP)
        opp_score += 1

    else:

        show_opponent = Label(image=scissors_photo, height=120, width=120)
        show_opponent.pack(side=TOP)

        winner_is = Label(text="Rock beats scissors. You Win!.", font=("Helvetica", 28), bg="black", fg="white", pady=20)
        winner_is.pack(side=TOP)

        my_score += 1

    show_scores()

    to_play()

def paper_choice():
    clear_and_add_new()
    global my_score,opp_score

    paper_prompt = Label(text="You chose paper.", font=("Helvetica", 28), bg="black",fg="white", pady=20)
    paper_prompt.pack(side=TOP)
    opp_choice = computer_choice()

    show_paper = Label(image=paper_photo, height=120, width=120)
    show_paper.pack(side=TOP)

    vs_prompt()

    opponent_prompt = Label(text=f"Opponent chose {gestures[opp_choice]}.", font=("Helvetica", 28), bg="black",fg="white", pady=20)
    opponent_prompt.pack(side=TOP)

    if opp_choice == 0:

        show_opponent = Label(image=rock_photo, height=120, width=120)
        show_opponent.pack(side=TOP)

        winner_is = Label(text="Paper beats rock. You Win!.", font=("Helvetica", 28), bg="black", fg="white", pady=20)
        winner_is.pack(side=TOP)

        my_score += 1

    elif opp_choice == 1:

        show_opponent = Label(image=paper_photo, height=120, width=120)
        show_opponent.pack(side=TOP)

        winner_is = Label(text="It's a tie!.", font=("Helvetica", 28), bg="black", fg="white", pady=20)
        winner_is.pack(side=TOP)
    else:

        show_opponent = Label(image=scissors_photo, height=120, width=120)
        show_opponent.pack(side=TOP)

        winner_is = Label(text="Scissors beats paper. You Lose!.", font=("Helvetica", 28), bg="black", fg="white", pady=20)
        winner_is.pack(side=TOP)
        opp_score += 1
    show_scores()

    to_play()

def scissors_choice():

    clear_and_add_new()
    global my_score,opp_score


    scissors_prompt = Label(text="You chose scissors.", font=("Helvetica", 28), bg="black",fg="white", pady=20)
    scissors_prompt.pack(side=TOP)
    opp_choice = computer_choice()

    show_scissors = Label(image=scissors_photo, height=120, width=120)
    show_scissors.pack(side=TOP)

    vs_prompt()

    opponent_prompt = Label(text=f"Opponent chose {gestures[opp_choice]}.", font=("Helvetica", 28), bg="black",fg="white", pady=20)
    opponent_prompt.pack(side=TOP)

    if opp_choice == 0:

        show_opponent = Label(image=rock_photo, height=120, width=120)
        show_opponent.pack(side=TOP)

        winner_is = Label(text="Rock beats scissors. You Lose!.", font=("Helvetica", 28), bg="black", fg="white", pady=20)
        winner_is.pack(side=TOP)

        opp_score += 1


    elif opp_choice == 1:

        show_opponent = Label(image=paper_photo, height=120, width=120)
        show_opponent.pack(side=TOP)

        winner_is = Label(text="Scissors beats paper. You Win", font=("Helvetica", 28), bg="black", fg="white", pady=20)
        winner_is.pack(side=TOP)


        my_score += 1
    else:

        show_opponent = Label(image=scissors_photo, height=120, width=120)
        show_opponent.pack(side=TOP)

        winner_is = Label(text="It's a tie.", font=("Helvetica", 28), bg="black", fg="white", pady=20)
        winner_is.pack(side=TOP)

    to_play()
    show_scores()

welcome_title = Label(text="Rock, Paper, Scissors", font=("Helvetica", 40) , bg="black", fg="white", pady=50)
welcome_title.pack(side=TOP)
to_play()

win.mainloop()



