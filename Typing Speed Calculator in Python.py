#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
import time
from tkinter import messagebox

class TypingSpeedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Calculator")
        self.sample_text = ("The quick brown fox jumps over the lazy dog. "
                            "This sentence contains every letter of the alphabet.")
        self.start_time = None

        self.label = tk.Label(root, text="Type the following text as quickly and accurately as you can:")
        self.label.pack(pady=10)

        self.text_display = tk.Label(root, text=self.sample_text, wraplength=400, justify="left")
        self.text_display.pack(pady=10)

        self.text_entry = tk.Text(root, height=5, width=50)
        self.text_entry.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Typing", command=self.start_typing)
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def start_typing(self):
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.text_entry.focus()
        self.root.bind('<Return>', self.calculate_speed)

    def calculate_speed(self, event=None):
        end_time = time.time()
        typed_text = self.text_entry.get("1.0", tk.END).strip()
        elapsed_time = end_time - self.start_time
        words_typed = len(typed_text.split())
        wpm = words_typed / (elapsed_time / 60)

        correct_words = 0
        for typed_word, sample_word in zip(typed_text.split(), self.sample_text.split()):
            if typed_word == sample_word:
                correct_words += 1
        accuracy = (correct_words / len(self.sample_text.split())) * 100

        self.result_label.config(text=f"Time: {elapsed_time:.2f} seconds\nWPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%")
        self.start_button.config(state=tk.NORMAL)
        self.root.unbind('<Return>')

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedCalculator(root)
    root.mainloop()


# In[ ]:




