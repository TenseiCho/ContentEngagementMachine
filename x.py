import tkinter as tk
from tkinter import ttk

def create_menu_frame(root, back_command):
    x_frame = ttk.Frame(root, style='Dark.TFrame')
    
    # Configure grid weights for centering
    x_frame.grid_rowconfigure(1, weight=1)
    x_frame.grid_columnconfigure(0, weight=1)
    
    # Create a label for the X menu
    label = tk.Label(x_frame, 
        text="X Content Manager",
        font=("Arial", 24, "bold"),
        background='#1e1e1e',
        foreground='#ffffff')
    label.grid(row=0, column=0, pady=(50, 20))
    
    # Create a frame for the content
    content_frame = ttk.Frame(x_frame, style='Dark.TFrame')
    content_frame.grid(row=1, column=0)
    
    # Add feature descriptions
    features = [
        "• Automate finding images, GIFs & videos",
        "• Automate text addition with custom formats",
        "• Schedule posts for specific days/hours",
        "• Combine media automatically"
    ]
    
    for i, feature in enumerate(features):
        feature_label = tk.Label(
            content_frame,
            text=feature,
            font=("Arial", 12),
            background='#1e1e1e',
            foreground='#ffffff',
            justify='left'
        )
        feature_label.grid(row=i, column=0, pady=5, sticky='w')
    
    # Add a button to go back to the main menu
    back_button = ttk.Button(x_frame, 
        text="Back to Main Menu",
        command=back_command,
        style='Dark.TButton')
    back_button.grid(row=2, column=0, pady=30)
    
    return x_frame
