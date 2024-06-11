import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

class NoteTakerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Note Taker")
        
        self.tabs = ttk.Notebook(self.master)
        self.tabs.pack(fill=tk.BOTH, expand=True)
        
        self.add_tab_button = ttk.Button(self.master, text="New Tab", command=self.add_tab)
        self.add_tab_button.pack(side=tk.TOP, pady=5)
        
        self.add_tab()

    def add_tab(self):
        new_tab = ttk.Frame(self.tabs)
        self.tabs.add(new_tab, text="Tab {}".format(self.tabs.index("end")))
        
        text_area = tk.Text(new_tab)
        text_area.pack(fill=tk.BOTH, expand=True)
        
        button_frame = ttk.Frame(new_tab)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        new_tab_button = ttk.Button(button_frame, text="Rename", command=lambda: self.rename_tab(new_tab))
        new_tab_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        close_button = ttk.Button(button_frame, text="Close", command=lambda: self.close_tab(new_tab))
        close_button.pack(side=tk.LEFT, padx=5, pady=5)

    def rename_tab(self, tab):
        index = self.tabs.index(tab)
        new_name = tk.simpledialog.askstring("Rename Tab", "Enter new name for the tab:")
        if new_name:
            self.tabs.tab(index, text=new_name)

    def close_tab(self, tab):
        self.tabs.forget(tab)

def main():
    root = tk.Tk()
    app = NoteTakerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
