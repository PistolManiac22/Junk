import tkinter as tk
from tkinter import ttk
import random

global WhoMoves, choice2, choice3, choice4
WhoMoves = True
choice2 = "option 1 out of 5"
choice3 = "option 1 out of 5"
choice4 = "option 1 out of 5"

def main():
    # robot_is_first = not prompt_user_if_he_wants_start() todo use after debug
    # motivation_level = prompt_user_for_interaction_level("motivation")
    # recommended_move_level = prompt_user_for_interaction_level("recommended next moves for you")
    # own_move_level = prompt_user_for_interaction_level("it's moves")
    robot_is_first = WhoMoves
    print(robot_is_first)
    motivation_level = choice2
    print(motivation_level)
    recommended_move_level = choice3
    print(recommended_move_level)
    own_move_level = choice4
    print(own_move_level)

def UI():
    def CenterWindowToDisplay(Screen: tk.Tk, width: int, height: int, scale_factor: float = 1.0):
        """Centers the window to the main display/monitor"""
        screen_width = Screen.winfo_screenwidth()
        screen_height = Screen.winfo_screenheight()
        x = int(((screen_width / 2) - (width / 2)) * scale_factor)
        y = int(((screen_height / 2) - (height / 1.5)) * scale_factor)
        return f"{width}x{height}+{x}+{y}"

    def update_choice(choice, variable_name):
        global WhoMoves, choice2, choice3, choice4
        if variable_name == "WhoMoves":
            if choice == "Blue (Robot First)":
                WhoMoves = True
            elif choice == "Red (You are First)":
                WhoMoves = False
            elif choice == "Random":
                WhoMoves = random.choice([True, False])
        elif variable_name == "choice2":
            choice2 = choice
        elif variable_name == "choice3":
            choice3 = choice
        elif variable_name == "choice4":
            choice4 = choice

    app = tk.Tk()
    app.geometry(CenterWindowToDisplay(app, 900, 500, 1.0))
    app.title("Let's Play Checker!")

    title = tk.Label(app, text="Let's Play Checker!", font=('Arial', 30, 'bold'))
    title.pack(pady=10)

    text1 = tk.Label(app, text="Who moves first", font=('Arial', 15))
    text1.pack(pady=10)
    optionmenu_var1 = tk.StringVar(value="Blue (Robot First)")
    optionmenu1 = ttk.OptionMenu(app, optionmenu_var1, "Blue (Robot First)", "Blue (Robot First)", "Red (You are First)", "Random", 
                                  command=lambda choice: update_choice(choice, "WhoMoves"))
    optionmenu1.pack(pady=10)

    text2 = tk.Label(app, text="Choice 2", font=('Arial', 15))
    text2.pack(pady=10)
    optionmenu_var2 = tk.StringVar(value="option 1 out of 5")
    optionmenu2 = ttk.OptionMenu(app, optionmenu_var2, "option 1 out of 5", "option 1 out of 5", "option 2", "option 3", "option 4", "option 5",
                                  command=lambda choice: update_choice(choice, "choice2"))
    optionmenu2.pack(pady=10)

    text3 = tk.Label(app, text="Choice 3", font=('Arial', 15))
    text3.pack(pady=10)
    optionmenu_var3 = tk.StringVar(value="option 1 out of 5")
    optionmenu3 = ttk.OptionMenu(app, optionmenu_var3, "option 1 out of 5", "option 1 out of 5", "option 2", "option 3", "option 4", "option 5",
                                  command=lambda choice: update_choice(choice, "choice3"))
    optionmenu3.pack(pady=10)

    text4 = tk.Label(app, text="Choice 4", font=('Arial', 15))
    text4.pack(pady=10)
    optionmenu_var4 = tk.StringVar(value="option 1 out of 5")
    optionmenu4 = ttk.OptionMenu(app, optionmenu_var4, "option 1 out of 5", "option 1 out of 5", "option 2", "option 3", "option 4", "option 5",
                                  command=lambda choice: update_choice(choice, "choice4"))
    optionmenu4.pack(pady=10)

    startbutton = tk.Button(app, text="Start Game", command=app.quit, bg="red", fg="white", font=('Arial', 15, 'bold'))
    startbutton.pack(pady=10)

    app.mainloop()
    main()

if __name__ == "__main__":
    UI()
# print(f"First turn: {WhoMoves}")
# print(f"Choice 2: {choice2}")
# print(f"Choice 3: {choice3}")
# print(f"Choice 4: {choice4}")
