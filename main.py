import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("My Application")
        self.root.geometry("400x300")  # Set window size

        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create button frame at bottom
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.grid(row=1, column=0, pady=10, sticky=(tk.E, tk.W))

        # Create buttons
        self.button1 = ttk.Button(self.button_frame, text="Button 1", command=self.button1_click)
        self.button1.grid(row=0, column=0, padx=5)

        self.button2 = ttk.Button(self.button_frame, text="Button 2", command=self.button2_click)
        self.button2.grid(row=0, column=1, padx=5)

    def button1_click(self):
        print("Button 1 clicked!")

    def button2_click(self):
        print("Button 2 clicked!")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main() 