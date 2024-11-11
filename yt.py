import tkinter as tk
from tkinter import ttk

def create_menu_frame(root, back_command):
    yt_frame = ttk.Frame(root, style='Dark.TFrame')
    
    # Configure grid weights for centering
    yt_frame.grid_rowconfigure(1, weight=1)
    yt_frame.grid_columnconfigure(0, weight=1)
    
    # Create a label for the YT Shorts menu
    label = tk.Label(yt_frame,
        text="YouTube Shorts Manager",
        font=("Arial", 24, "bold"),
        background='#1e1e1e',
        foreground='#ffffff')
    label.grid(row=0, column=0, pady=(50, 20))
    
    # Create a frame for the content
    content_frame = ttk.Frame(yt_frame, style='Dark.TFrame')
    content_frame.grid(row=1, column=0)
    
    # Add feature descriptions
    features = [
        "• Automate anime downloading",
        "• Create 30-second clips using OBS settings",
        "• Automatic YouTube uploads",
        "• Smart scheduling and metadata management"
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
    back_button = ttk.Button(yt_frame,
        text="Back to Main Menu",
        command=back_command,
        style='Dark.TButton')
    back_button.grid(row=2, column=0, pady=30)
    
    return yt_frame
