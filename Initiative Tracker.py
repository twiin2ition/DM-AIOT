import tkinter as tk
from tkinter import ttk

class InitiativeTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("D&D Initiative Tracker")

        self.initiative_list = []

        self.initiative_frame = ttk.Frame(master)
        self.initiative_frame.pack(padx=10, pady=10)

        self.player_label = ttk.Label(self.initiative_frame, text="Player Name:")
        self.player_label.grid(row=0, column=0, padx=5, pady=5)

        self.player_entry = ttk.Entry(self.initiative_frame)
        self.player_entry.grid(row=0, column=1, padx=5, pady=5)

        self.roll_label = ttk.Label(self.initiative_frame, text="Roll:")
        self.roll_label.grid(row=0, column=2, padx=5, pady=5)

        self.roll_entry = ttk.Entry(self.initiative_frame)
        self.roll_entry.grid(row=0, column=3, padx=5, pady=5)

        self.add_button = ttk.Button(self.initiative_frame, text="Add", command=self.add_initiative)
        self.add_button.grid(row=0, column=4, padx=5, pady=5)

        self.clear_button = ttk.Button(self.initiative_frame, text="Clear", command=self.clear_initiative)
        self.clear_button.grid(row=0, column=5, padx=5, pady=5)

        self.initiative_display = tk.Text(self.initiative_frame, height=10, width=40)
        self.initiative_display.grid(row=1, columnspan=6, padx=5, pady=5)

        # Bind Enter key to add_initiative
        self.player_entry.bind("<Return>", lambda event: self.roll_entry.focus())
        self.roll_entry.bind("<Return>", lambda event: self.add_initiative())

    def add_initiative(self):
        name = self.player_entry.get()
        roll = int(self.roll_entry.get())
        self.initiative_list.append((name, roll))
        self.initiative_list.sort(key=lambda x: x[1], reverse=True)
        self.display_initiative()
        self.player_entry.delete(0, tk.END)
        self.roll_entry.delete(0, tk.END)
        self.player_entry.focus()

    def clear_initiative(self):
        self.initiative_list = []
        self.display_initiative()

    def display_initiative(self):
        self.initiative_display.delete(1.0, tk.END)
        for i, (name, roll) in enumerate(self.initiative_list, start=1):
            self.initiative_display.insert(tk.END, f"{i}. {name}: Roll {roll}\n")


def main():
    root = tk.Tk()
    app = InitiativeTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
