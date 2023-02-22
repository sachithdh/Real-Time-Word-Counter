import customtkinter as ctk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class WordCounter:

    def __init__(self) :

        # system settings
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")
        
        # framework
        self.root = ctk.CTk()
        self.root.geometry("720x650")
        self.root.title("Word Counter")

        # text input field
        self.text = ScrolledText(self.root, font=("times", 12), bg="gray22", fg="white", width=90, height=25)
        self.text.bind("<KeyRelease>", self.count)
        self.text.pack(padx=10, pady=10)

        # show word count
        self.showCount = ctk.CTkLabel(self.root, text="0 word")
        self.showCount.pack()

        # appearance
        self.appearance_mode_label = ctk.CTkLabel(self.root, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.pack(padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.root, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.pack(padx=20, pady=(10, 10))

        self.root.mainloop()

    def count(self, event):

        # read input text
        content = self.text.get("1.0", tk.END)

        # calculate the word count
        wordList = [i for i in content.split(" ")]

        if wordList[len(wordList)-1] == "\n":
            count = len(wordList) - 1
        else:
            count = len(wordList)

        for word in wordList:
            if word == '':
                count -=1
        
        self.showCount.configure(text = str(count) + " Words")
 
    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
        
        if new_appearance_mode == "Dark":
            self.text.configure(bg="gray22", fg="white")
        elif new_appearance_mode == "Light":
            self.text.configure(bg="white", fg="black")

WordCounter()
