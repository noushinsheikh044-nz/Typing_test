import tkinter as tk
import random
import time

# Sample sentences
sentences = [
    "Python is a powerful programming language",
    "Typing speed improves with practice",
    "Artificial intelligence is the future",
    "Cyber security is very important today",
    "Practice daily to improve your skills"
]

start_time = 0

def start_test():
    global start_time
    start_time = time.time()
    text_entry.delete(0, tk.END)
    random_sentence.set(random.choice(sentences))
    result_label.config(text="")

def check_result():
    end_time = time.time()
    total_time = end_time - start_time
    
    typed_text = text_entry.get()
    original_text = random_sentence.get()

    # Words per minute
    words = len(typed_text.split())
    wpm = round((words / total_time) * 60)

    # Accuracy
    correct_chars = sum(1 for i, j in zip(typed_text, original_text) if i == j)
    accuracy = round((correct_chars / len(original_text)) * 100)

    result_label.config(text=f"WPM: {wpm} | Accuracy: {accuracy}%")

# GUI Setup
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("500x300")

random_sentence = tk.StringVar()

# Display sentence
sentence_label = tk.Label(root, textvariable=random_sentence, wraplength=400, font=("Arial", 12))
sentence_label.pack(pady=20)

# Input box
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=10)

# Buttons
start_button = tk.Button(root, text="Start", command=start_test)
start_button.pack(pady=5)

check_button = tk.Button(root, text="Check Result", command=check_result)
check_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()