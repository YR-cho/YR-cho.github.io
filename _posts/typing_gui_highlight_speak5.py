import tkinter as tk
from tkinter import messagebox, ttk
import os
import random
import matplotlib.pyplot as plt
import time
import threading
import pyttsx3

def load_sentences(filename):
    sentence_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '|' in line:
                korean, english = line.strip().split('|', 1)
                sentence_list.append((korean.strip(), english.strip()))
    return sentence_list

class TypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Practice with Speech")

        self.sentence_pool = []
        self.current_index = 0
        self.korean = ""
        self.english = ""
        self.mode = "random"
        self.filename = None
        self.total_sentences = 0

        self.wrong_sentences = []
        self.favorite_sentences = []

        self.review_mode = tk.BooleanVar(value=False)
        self.correct_count = 0
        self.wrong_count = 0
        self.start_time = None
        self.sentence_times = []

        self.setup_selection_screen()

    def setup_selection_screen(self):
        self.select_frame = tk.Frame(self.root)
        self.select_frame.pack(pady=20)

        tk.Label(self.select_frame, text="Select Library:").pack()
        self.library_combo = ttk.Combobox(self.select_frame, state="readonly")
        lib_path = "lib"
        self.files = [f for f in os.listdir(lib_path) if f.endswith('.txt')]
        if not self.files:
            messagebox.showerror("Error", "No .txt files found in 'lib' folder.")
            self.root.destroy()
            return
        self.library_combo['values'] = self.files
        self.library_combo.current(0)
        self.library_combo.pack(pady=5)

        tk.Label(self.select_frame, text="Practice Mode:").pack()
        self.mode_var = tk.StringVar(value="random")
        tk.Radiobutton(self.select_frame, text="Random", variable=self.mode_var, value="random").pack()
        tk.Radiobutton(self.select_frame, text="Sequential", variable=self.mode_var, value="sequential").pack()

        tk.Label(self.select_frame, text="Number of sentences (only for Random):").pack()
        self.num_entry = tk.Entry(self.select_frame)
        self.num_entry.insert(0, "10")
        self.num_entry.pack(pady=5)

        tk.Checkbutton(self.select_frame, text="Enable wrong sentence review mode", variable=self.review_mode).pack(pady=5)

        tk.Button(self.select_frame, text="Start", command=self.start_typing).pack(pady=10)

    def start_typing(self):
        self.filename = os.path.join("lib", self.library_combo.get())
        self.mode = self.mode_var.get()
        try:
            self.total_sentences = int(self.num_entry.get())
        except ValueError:
            self.total_sentences = 10

        self.select_frame.destroy()
        self.setup_typing_screen()
        self.load_sentences_gui()
        self.next_sentence()

    def setup_typing_screen(self):
        self.progress_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.progress_label.pack(pady=2)

        self.korean_label = tk.Label(self.root, text="Meaning: ", font=("Arial", 14))
        self.korean_label.pack(pady=5)

        self.english_label = tk.Label(self.root, text="English: ", font=("Arial", 14))
        self.english_label.pack(pady=5)

        self.text_input = tk.Text(self.root, height=2, font=("Courier", 14), wrap="word")
        self.text_input.pack(padx=10, pady=10)
        self.text_input.bind("<KeyRelease-Return>", self.on_enter)
        self.text_input.bind("<KeyRelease>", self.on_type)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=5)

        self.favorite_button = tk.Button(self.button_frame, text="★ Favorite", command=self.mark_favorite)
        self.favorite_button.grid(row=0, column=0, padx=5)

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.next_sentence)
        self.next_button.grid(row=0, column=1, padx=5)

    def load_sentences_gui(self):
        all_sentences = load_sentences(self.filename)
        if self.mode == "random":
            self.sentence_pool = random.sample(all_sentences, min(self.total_sentences, len(all_sentences)))
        else:
            self.sentence_pool = all_sentences
        self.total_sentences = len(self.sentence_pool)

    def next_sentence(self):
        if self.current_index >= len(self.sentence_pool):
            if self.review_mode.get() and self.wrong_sentences:
                self.sentence_pool = self.wrong_sentences
                self.total_sentences = len(self.sentence_pool)
                self.current_index = 0
                self.wrong_sentences = []
                messagebox.showinfo("Review", "Starting review for wrong sentences!")
                self.next_sentence()
                return
            self.show_statistics()
            return

        self.korean, self.english = self.sentence_pool[self.current_index]
        self.korean_label.config(text=f"Meaning: {self.korean}")
        self.english_label.config(text=f"English: {self.english}")
        self.progress_label.config(text=f"Sentence {self.current_index + 1} / {self.total_sentences}")
        self.text_input.delete("1.0", tk.END)
        self.text_input.tag_configure("wrong", foreground="red")
        self.text_input.focus_set()
        self.start_time = time.time()

        threading.Thread(target=self.speak_sentence, args=(self.english,), daemon=True).start()

    def speak_sentence(self, sentence):
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
            engine.say(sentence)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print("Speech error:", e)

    def on_type(self, event=None):
        typed = self.text_input.get("1.0", tk.END).rstrip("\n")
        self.text_input.tag_remove("wrong", "1.0", tk.END)

        for i in range(len(typed)):
            if i >= len(self.english):
                self.text_input.tag_add("wrong", f"1.{i}", f"1.{i+1}")
            elif typed[i] != self.english[i]:
                self.text_input.tag_add("wrong", f"1.{i}", f"1.{i+1}")

    def on_enter(self, event=None):
        typed = self.text_input.get("1.0", tk.END).strip()
        if typed == self.english:
            elapsed = time.time() - self.start_time
            self.sentence_times.append(elapsed)
            self.correct_count += 1
            self.current_index += 1
            self.next_sentence()
        else:
            self.wrong_count += 1
            self.wrong_sentences.append((self.korean, self.english))
            messagebox.showwarning("Incorrect", "Typed sentence is not correct.")

    def mark_favorite(self):
        self.favorite_sentences.append((self.korean, self.english))
        messagebox.showinfo("Saved", "This sentence has been added to favorites.")

    def show_statistics(self):
        avg_time = sum(self.sentence_times)/len(self.sentence_times) if self.sentence_times else 0
        accuracy = (self.correct_count / self.total_sentences) * 100 if self.total_sentences > 0 else 0

        stats = (
            f"Total sentences: {self.total_sentences}\n"
            f"Correct: {self.correct_count}\n"
            f"Wrong: {self.wrong_count}\n"
            f"Accuracy: {accuracy:.2f}%\n"
            f"Average time: {avg_time:.2f} sec"
        )
        if self.favorite_sentences:
            fav_lines = "\n\n★ Favorite Sentences ★\n" + "\n".join([f"{k} | {e}" for k, e in self.favorite_sentences])
            stats += fav_lines
        messagebox.showinfo("Result", stats)
        self.plot_graph()

    def plot_graph(self):
        if not self.sentence_times:
            return
        plt.figure(figsize=(6, 4))
        plt.plot(range(1, len(self.sentence_times)+1), self.sentence_times, marker='o')
        plt.title('Typing Speed per Sentence')
        plt.xlabel('Sentence #')
        plt.ylabel('Time (s)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    root.mainloop()
