import tkinter as tk
from tkinter import ttk
import x  # Import the x module
import yt  # Import the yt module

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Content Engagement Machine")
        self.root.geometry("600x600")  # Set window size

        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create button frame at bottom
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.grid(row=1, column=0, pady=10, sticky=(tk.E, tk.W))

        # Create buttons
        self.button1 = ttk.Button(self.button_frame, text="X", command=self.show_x_menu)
        self.button1.grid(row=0, column=0, padx=5)

        self.button2 = ttk.Button(self.button_frame, text="YT Shorts", command=self.show_yt_menu)
        self.button2.grid(row=0, column=1, padx=5)

        # Create frames for X and YT menus
        self.x_frame = x.create_menu_frame(self.root, self.show_main_menu)
        self.yt_frame = yt.create_menu_frame(self.root, self.show_main_menu)

    def show_x_menu(self):
        self.main_frame.grid_forget()  # Hide the main frame
        self.x_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))  # Show X menu frame

    def show_yt_menu(self):
        self.main_frame.grid_forget()  # Hide the main frame
        self.yt_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))  # Show YT menu frame

    def show_main_menu(self):
        self.x_frame.grid_forget()  # Hide X menu frame
        self.yt_frame.grid_forget()  # Hide YT menu frame
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))  # Show main frame

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main() 