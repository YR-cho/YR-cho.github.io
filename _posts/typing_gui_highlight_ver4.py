import tkinter as tk
from tkinter import messagebox, ttk
import os
import random

# ===== 문장 불러오기 =====
def load_sentences(filename):
    sentence_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '|' in line:
                korean, english = line.strip().split('|', 1)
                sentence_list.append((korean.strip(), english.strip()))
    return sentence_list

# ===== 주요 GUI 로직 =====
class TypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("영어 타자 연습기 (GUI)")

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

        self.setup_selection_screen()

    def setup_selection_screen(self):
        self.select_frame = tk.Frame(self.root)
        self.select_frame.pack(pady=20)

        # 라이브러리 선택
        tk.Label(self.select_frame, text="라이브러리 선택:").pack()
        self.library_combo = ttk.Combobox(self.select_frame, state="readonly")
        lib_path = "lib"
        self.files = [f for f in os.listdir(lib_path) if f.endswith('.txt')]
        if not self.files:
            messagebox.showerror("오류", "lib 폴더에 .txt 파일이 없습니다.")
            self.root.destroy()
            return
        self.library_combo['values'] = self.files
        self.library_combo.current(0)
        self.library_combo.pack(pady=5)

        # 모드 선택
        tk.Label(self.select_frame, text="연습 모드:").pack()
        self.mode_var = tk.StringVar(value="random")
        tk.Radiobutton(self.select_frame, text="랜덤(Random)", variable=self.mode_var, value="random").pack()
        tk.Radiobutton(self.select_frame, text="순서대로(Sequential)", variable=self.mode_var, value="sequential").pack()

        # 학습 문장 수 입력 (랜덤일 때만 적용)
        tk.Label(self.select_frame, text="학습할 문장 수 (랜덤 모드에서만):").pack()
        self.num_entry = tk.Entry(self.select_frame)
        self.num_entry.insert(0, "10")
        self.num_entry.pack(pady=5)

        # 오답 복습 옵션
        tk.Checkbutton(self.select_frame, text="오답 문장 복습 모드 활성화", variable=self.review_mode).pack(pady=5)

        tk.Button(self.select_frame, text="시작", command=self.start_typing).pack(pady=10)

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

        self.korean_label = tk.Label(self.root, text="뜻: ", font=("Arial", 14))
        self.korean_label.pack(pady=5)

        self.english_label = tk.Label(self.root, text="영어: ", font=("Arial", 14))
        self.english_label.pack(pady=5)

        self.text_input = tk.Text(self.root, height=2, font=("Courier", 14), wrap="word")
        self.text_input.pack(padx=10, pady=10)
        self.text_input.bind("<KeyRelease-Return>", self.on_enter)
        self.text_input.bind("<KeyRelease>", self.on_type)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=5)

        self.favorite_button = tk.Button(self.button_frame, text="★ 즐겨찾기", command=self.mark_favorite)
        self.favorite_button.grid(row=0, column=0, padx=5)

        self.next_button = tk.Button(self.button_frame, text="다음 문장", command=self.next_sentence)
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
                messagebox.showinfo("복습 시작", "오답 문장 복습을 시작합니다!")
                self.next_sentence()
                return
            self.show_statistics()
            self.root.destroy()
            return

        self.korean, self.english = self.sentence_pool[self.current_index]
        self.korean_label.config(text=f"뜻: {self.korean}")
        self.english_label.config(text=f"영어: {self.english}")
        self.progress_label.config(text=f"문장 {self.current_index + 1} / {self.total_sentences}")
        self.text_input.delete("1.0", tk.END)
        self.text_input.tag_configure("wrong", foreground="red")

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
            self.correct_count += 1
        else:
            self.wrong_count += 1
            self.wrong_sentences.append((self.korean, self.english))
            messagebox.showwarning("오답", "정확히 입력되지 않았습니다. 다시 확인해주세요.")

        self.current_index += 1
        self.next_sentence()

    def mark_favorite(self):
        self.favorite_sentences.append((self.korean, self.english))
        messagebox.showinfo("즐겨찾기 추가됨", "현재 문장이 즐겨찾기에 추가되었습니다.")

    def show_statistics(self):
        stats = f"총 문장 수: {self.total_sentences}\n정답 수: {self.correct_count}\n오답 수: {self.wrong_count}"
        if self.favorite_sentences:
            fav_lines = "\n\n★ 즐겨찾기 문장 ★\n" + "\n".join([f"{k} | {e}" for k, e in self.favorite_sentences])
            stats += fav_lines
        messagebox.showinfo("학습 완료 통계", stats)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    root.mainloop()
