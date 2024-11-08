import tkinter as tk

def create_menu_frame(root, back_command):
    x_frame = tk.Frame(root)

    # Create a label for the X menu
    label = tk.Label(x_frame, text="This is the X Menu", font=("Arial", 16))
    label.pack(pady=20)

    # Add a button to go back to the main menu
    back_button = tk.Button(x_frame, text="Back to Main Menu", command=back_command)
    back_button.pack(pady=10)

    return x_frame
