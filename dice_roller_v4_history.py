import tkinter as tk
import random

class DiceRollerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Roller")

        self.roll_frame = tk.Frame(master)
        self.roll_frame.grid(row=0, column=0, padx=10, pady=10)

        self.num_dice_label = tk.Label(self.roll_frame, text="#")
        self.num_dice_label.grid(row=0, column=0)

        self.num_dice_entry = tk.Entry(self.roll_frame, width=5)
        self.num_dice_entry.grid(row=0, column=1)

        self.dice_type_label = tk.Label(self.roll_frame, text="d")
        self.dice_type_label.grid(row=0, column=2)

        self.dice_type_entry = tk.Entry(self.roll_frame, width=5)
        self.dice_type_entry.grid(row=0, column=3)

        self.modifier_label = tk.Label(self.roll_frame, text="+/-")
        self.modifier_label.grid(row=0, column=4)

        self.modifier_entry = tk.Entry(self.roll_frame, width=5)
        self.modifier_entry.grid(row=0, column=5)

        self.roll_button = tk.Button(self.roll_frame, text="Roll", command=self.roll_dice)
        self.roll_button.grid(row=0, column=6)
        # Bind <Return> key to roll_dice method
        self.master.bind('<Return>', self.roll_dice)

        self.reset_button = tk.Button(master, text="Reset History", command=self.reset_history)
        self.reset_button.grid(row=1, column=0, pady=5)

        self.history_label = tk.Label(master, text="History:")
        self.history_label.grid(row=2, column=0)

        self.history_text = tk.Text(master, height=10, width=30)
        self.history_text.grid(row=3, column=0)

        self.history = []

    def roll_dice(self, event=None):
        num_dice = int(self.num_dice_entry.get().strip())
        dice_type = self.dice_type_entry.get().strip()
        modifier = self.modifier_entry.get().strip()
        if modifier == "":
            modifier = "+0"

        try:
            num_sides = int(dice_type[1:]) if dice_type.startswith("d") else int(dice_type)
            rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
            total = sum(rolls) + eval(modifier)
            roll_str = ", ".join(map(str, rolls))
            result_str = f"{num_dice}d{dice_type} {modifier} = {roll_str} {modifier} [{total}]"
            if num_sides == 20:
                if max(rolls) == 20:
                    self.history_text.insert(tk.END, result_str + "\n", 'green')
                elif min(rolls) == 1:
                    self.history_text.insert(tk.END, result_str + "\n", 'red')
                else:
                    self.history_text.insert(tk.END, result_str + "\n")
            else:
                self.history_text.insert(tk.END, result_str + "\n")
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input. Please use the format '# d $ +/- *' where # is the number of dice, $ is the dice type, and * is the modifier.")

    def update_history(self):
        self.history_text.tag_configure('green', foreground='green')
        self.history_text.tag_configure('red', foreground='red')

    def reset_history(self):
        self.history_text.delete(1.0, tk.END)
        self.history = []

def main():
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
