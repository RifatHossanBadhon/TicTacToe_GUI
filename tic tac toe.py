import tkinter
import random


def next_turn(row, column):
    global player

    if "" == buttons[row][column]["text"] and check_winner() is False:

        if player == players[0]:
            buttons[row][column]["text"] = player
            buttons[row][column].config(fg="light green")

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"), )

            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            if player == players[1]:
                buttons[row][column]["text"] = player
                buttons[row][column].config(fg="red")

                if check_winner() is False:
                    player = players[0]
                    label.config(text=(players[0] + " turn"))

                elif check_winner() is True:
                    label.config(text=(players[1] + " wins"))

                elif check_winner() == "Tie":
                    label.config(text="Tie!")


def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            win_color = "orange" if buttons[row][0]["text"] == "o" else "green"
            buttons[row][0].config(bg=win_color)
            buttons[row][1].config(bg=win_color)
            buttons[row][2].config(bg=win_color)
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            win_color = "orange" if buttons[row][0]["text"] == "o" else "green"
            buttons[0][column].config(bg=win_color)
            buttons[1][column].config(bg=win_color)
            buttons[2][column].config(bg=win_color)
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        win_color = "orange" if buttons[row][0]["text"] == "o" else "green"
        buttons[0][0].config(bg=win_color)
        buttons[1][1].config(bg=win_color)
        buttons[2][2].config(bg=win_color)
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        win_color = "orange" if buttons[row][0]["text"] == "o" else "green"
        buttons[0][2].config(bg=win_color)
        buttons[1][1].config(bg=win_color)
        buttons[2][0].config(bg=win_color)
        return True
    elif empty_square() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='yellow')
        return "Tie"
    else:
        return False


def empty_square():
    space = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                space -= 1

    if space != 0:
        return True
    else:
        return False


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + ' turn')

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="lavender")


window = tkinter.Tk()
window.title("Tic-Tac-Toe ")
players = ["x", "o"]
player = random.choice(players)
buttons = [[None, None, None],
           [None, None, None],
           [None, None, None]]

label = tkinter.Label(text=player + " turn", font=("colas", 40), )
label.pack(side="top")

reset_button = tkinter.Button(text="Restart", font=("colas", 25), command=new_game, bg="red")
reset_button.pack(side="top")

window.overrideredirect(True)
window.geometry("+1000+200")

frame = tkinter.Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column] = tkinter.Button(frame, text="", font=("consolas", 40), width=5, height=2,
                                              command=lambda row=row, column=column: next_turn(row, column), bg="aqua")
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
