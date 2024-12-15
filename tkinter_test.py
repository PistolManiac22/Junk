import tkinter as tk
from tkinter import ttk
import random

global WhoMoves, MotLevel, RecLevel, OwnMoveLevel
WhoMoves = True
MotLevel = 1
RecLevel = 1
OwnMoveLevel = 1

def altmain(args=None):
    # robot_is_first = not prompt_user_if_he_wants_start() todo use after debug
    # motivation_level = prompt_user_for_interaction_level("motivation")
    # recommended_move_level = prompt_user_for_interaction_level("recommended next moves for you")
    # own_move_level = prompt_user_for_interaction_level("it's moves")
    robot_is_first = WhoMoves
    print(robot_is_first)
    motivation_level = MotLevel
    print(motivation_level)
    recommended_move_level = RecLevel
    print(recommended_move_level)
    own_move_level = OwnMoveLevel
    print(own_move_level)

def main():
    def CenterWindowToDisplay(Screen: tk.Tk, width: int, height: int, scale_factor: float = 1.0):
        """Centers the window to the main display/monitor"""
        screen_width = Screen.winfo_screenwidth()
        screen_height = Screen.winfo_screenheight()
        x = int(((screen_width / 2) - (width / 2)) * scale_factor)
        y = int(((screen_height / 2) - (height / 1.5)) * scale_factor)
        return f"{width}x{height}+{x}+{y}"

    def update_choice(choice, variable_name):
        global WhoMoves, MotLevel, RecLevel, OwnMoveLevel
        if variable_name == "WhoMoves":
            if choice == "Blue (Robot First)":
                WhoMoves = True
            elif choice == "Red (You are First)":
                WhoMoves = False
            elif choice == "Random":
                WhoMoves = random.choice([True, False])
        elif variable_name == "MotLevel":
            MotLevel = choice
        elif variable_name == "RecLevel":
            RecLevel = choice
        elif variable_name == "OwnMoveLevel":
            OwnMoveLevel = choice

    app = tk.Tk()
    app.geometry(CenterWindowToDisplay(app, 900, 600, 1.0))
    app.title("Let's Play Checker!")
    app.configure(bg="#00008b")

    # Add a frame for better grouping and design
    main_frame = tk.Frame(app, bg="#00008b", padx=20, pady=20, relief="groove", bd=5)
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    title = tk.Label(main_frame, text="Let's Play Checker!", font=('Arial', 36, 'bold'), fg="#1e90ff", bg="#00008b")
    title.pack(pady=20)

    text1 = tk.Label(main_frame, text="Who do you play as", font=('Arial', 16), bg="#00008b", fg="white")
    text1.pack(pady=10)
    optionmenu_var1 = tk.StringVar(value="Blue (Robot First)")
    optionmenu1 = ttk.OptionMenu(main_frame, optionmenu_var1, "Blue (Robot First)", "Blue (Robot First)", "Red (You are First)", "Random",
                                  command=lambda choice: update_choice(choice, "WhoMoves"))
    optionmenu1.pack(pady=5)

    text2 = tk.Label(main_frame, text="Motivation Level", font=('Arial', 16), bg="#00008b", fg="white")
    text2.pack(pady=10)
    optionmenu_var2 = tk.StringVar(value="1")
    optionmenu2 = ttk.OptionMenu(main_frame, optionmenu_var2, 1, 1, 2, 3,
                                  command=lambda choice: update_choice(choice, "MotLevel"))
    optionmenu2.pack(pady=5)

    text3 = tk.Label(main_frame, text="Recommended Move Level", font=('Arial', 16), bg="#00008b", fg="white")
    text3.pack(pady=10)
    optionmenu_var3 = tk.StringVar(value=1)
    optionmenu3 = ttk.OptionMenu(main_frame, optionmenu_var3, 1, 1, 2, 3,
                                  command=lambda choice: update_choice(choice, "RecLevel"))
    optionmenu3.pack(pady=5)

    text4 = tk.Label(main_frame, text="Own Move Level", font=('Arial', 16), bg="#00008b", fg="white")
    text4.pack(pady=10)
    optionmenu_var4 = tk.StringVar(value=1)
    optionmenu4 = ttk.OptionMenu(main_frame, optionmenu_var4, 1, 1, 2, 3,
                                  command=lambda choice: update_choice(choice, "OwnMoveLevel"))
    optionmenu4.pack(pady=5)

    startbutton = tk.Button(main_frame, text="Start Game", command=app.destroy, bg="#ff4500", fg="white", font=('Arial', 16, 'bold'), relief="raised")
    startbutton.pack(pady=20)

    # Add a footer
    footer = tk.Label(app, text="Enjoy your game!", font=('Arial', 12), bg="#00008b", fg="white")
    footer.pack(side="bottom", pady=10)

    app.mainloop()
    altmain()

if __name__ == "__main__":
    main()
