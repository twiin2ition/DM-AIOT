import tkinter as tk

class Program1GUI:
    def __init__(self, master):
        self.master = master
        master.title("Program 1 GUI")

        # Define a dictionary to store the maximum value for each dice type
        self.max_values = {
            'd4': 4,
            'd6': 6,
            'd8': 8,
            'd10': 10,
            'd12': 12,
            'd20': 20,
            'd%': 100
        }

        # Define a dictionary to store the average values for each dice type
        self.average_values = {
            'd4': 2.5,
            'd6': 3.5,
            'd8': 4.5,
            'd10': 5.5,
            'd12': 6.5,
            'd20': 10.5,
            'd%': 50.5
        }

        # Create and place widgets in the main window
        self.entries_dict = {}
        row_index = 0
        for dice_type in self.max_values.keys():
            label = tk.Label(master, text=f"{dice_type}:")
            label.grid(row=row_index, column=0, padx=5, pady=5, sticky="e")
            entries = []
            for i in range(20):  # Create 20 entry fields for each dice type
                entry = tk.Entry(master, width=5)
                entry.grid(row=row_index, column=i+1, padx=2, pady=5)
                entries.append(entry)
            self.entries_dict[dice_type] = entries
            row_index += 1

        self.result_text = tk.Text(master, width=50, height=10)
        self.result_text.grid(row=row_index, column=0, columnspan=21, padx=5, pady=5)

        track_button = tk.Button(master, text="Track Rolls", command=self.track_rolls)
        track_button.grid(row=row_index+1, column=0, columnspan=21, padx=5, pady=5)

        clear_button = tk.Button(master, text="Clear", command=self.clear_text)
        clear_button.grid(row=row_index+2, column=0, columnspan=21, padx=5, pady=5)

        # Button to return to main GUI
        return_button = tk.Button(master, text="Return to Home", command=self.return_to_home)
        return_button.grid(row=row_index+3, column=0, columnspan=21, padx=5, pady=5)

        # Bind <Return> event to track_rolls method
        master.bind("<Return>", lambda event: self.track_rolls())

    def return_to_home(self):
        self.master.destroy()  # Close the program GUI
        root.deiconify()  # Show the main GUI

    # Define a function to calculate the average of the rolls and compare it with the expected average
    def compare_averages(self, rolls_dict):
        result_message = ""
        for dice_type, rolls in rolls_dict.items():
            expected_average = self.average_values[dice_type]
            rolls = [roll for roll in rolls if roll is not None]  # Filter out None values
            if not rolls:
                result_message += f"\nDice Type: {dice_type}\nNo rolls provided.\n"
                continue
            rolls_sum = sum(rolls)
            rolls_count = len(rolls)
            actual_average = rolls_sum / rolls_count

            result_message += f"\nDice Type: {dice_type}\n"
            result_message += f"Average: {actual_average}\n"

            if actual_average >= 1.5 * expected_average:
                result_message += "God-Tier\n"
            elif actual_average >= expected_average and actual_average < 1.5 * expected_average:
                result_message += "Safe\n"
            elif actual_average <= expected_average and actual_average >= 0.5 * expected_average:
                result_message += "Jail\n"
            elif actual_average < 0.5 * expected_average:
                result_message += "Might want to throw this one away\n"

        # Clear previous content and insert new result
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result_message)

    # Define a function to handle the button click event
    def track_rolls(self, event=None):
        rolls_dict = {}
        for dice_type, entry_list in self.entries_dict.items():
            rolls = []
            for entry in entry_list:
                roll_str = entry.get()
                if roll_str == "":
                    roll_value = None  # Treat empty cells as None
                else:
                    try:
                        roll_value = int(roll_str)
                        if roll_value > self.max_values[dice_type]:
                            self.result_text.delete("1.0", tk.END)
                            self.result_text.insert(tk.END, f"Value {roll_value} is higher than {dice_type}.")
                            return
                    except ValueError:
                        self.result_text.delete("1.0", tk.END)
                        self.result_text.insert(tk.END, f"Invalid input: {roll_str}. Please enter integers.")
                        return
                rolls.append(roll_value)
            rolls_dict[dice_type] = rolls

        self.compare_averages(rolls_dict)

    def clear_text(self):
        for entry_list in self.entries_dict.values():
            for entry in entry_list:
                entry.delete(0, tk.END)
        self.result_text.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Dice Roll Tracker")

# Open Program 1 GUI directly
program1_window = tk.Toplevel(root)
app = Program1GUI(program1_window)

# Hide the main window
root.withdraw()

# Run the application
root.mainloop()
