import tkinter as tk
from tkinter import ttk
import x  # Import the x module
import yt  # Import the yt module

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Content Engagement Machine")
        self.root.geometry("600x600")
        
        # Configure dark theme
        self.root.configure(bg='#1e1e1e')  # Dark background
        
        # Create and configure style
        self.style = ttk.Style()
        self.style.theme_use('default')
        
        # Configure colors
        self.style.configure('TFrame', background='#1e1e1e')
        self.style.configure('TButton',
            background='#2d2d2d',
            foreground='#ffffff',
            padding=10,
            font=('Arial', 10, 'bold'))
        self.style.map('TButton',
            background=[('active', '#3d3d3d')],
            foreground=[('active', '#ffffff')])
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights to enable centering
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # Add welcome text
        welcome_label = ttk.Label(
            self.main_frame,
            text="Welcome to Content Engagement Machine\nSelect your platform:",
            font=('Arial', 14, 'bold'),
            foreground='#ffffff',
            background='#1e1e1e',
            justify='center'
        )
        welcome_label.grid(row=0, column=0, pady=(0, 20))

        # Create button frame in the middle
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.grid(row=1, column=0)

        # Create buttons with larger size
        button_style = {'width': 15, 'padding': 10}
        self.button1 = ttk.Button(
            self.button_frame,
            text="X",
            command=self.show_x_menu,
            **button_style
        )
        self.button1.grid(row=0, column=0, padx=10, pady=5)

        self.button2 = ttk.Button(
            self.button_frame,
            text="YT Shorts",
            command=self.show_yt_menu,
            **button_style
        )
        self.button2.grid(row=1, column=0, padx=10, pady=5)

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