import tkinter as tk

def create_menu_frame(root, back_command):
    yt_frame = tk.Frame(root)

    # Create a label for the YT Shorts menu
    label = tk.Label(yt_frame, text="This is the YT Shorts Menu", font=("Arial", 16))
    label.pack(pady=20)

    # Add a button to go back to the main menu
    back_button = tk.Button(yt_frame, text="Back to Main Menu", command=back_command)
    back_button.pack(pady=10)

    return yt_frame
