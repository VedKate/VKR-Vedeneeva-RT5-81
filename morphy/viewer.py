import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

from prepocessing import word_tokenizer
from sintaxAnalize import morphy_from_sentence


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Главное окно")
        self.geometry("400x300")

        self.sentence_button = tk.Button(self, text="Анализ предложения", command=self.open_sentence_analyzer, bd = 1)
        self.sentence_button.pack(pady=40)

        self.word_button = tk.Button(self, text="Анализ слова", command=self.open_word_analyzer, bd=1)
        self.word_button.pack(pady=40)

    def open_sentence_analyzer(self):
        SentenceAnalyzer(self)

    def open_word_analyzer(self):
        WordAnalyzer(self)


class SentenceAnalyzer(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Анализ предложения")
        self.geometry("500x400")

        self.sentences = []
        self.current_sentence_index = 0

        self.open_file_button = tk.Button(self, text="Открыть файл", command=self.load_file)
        self.open_file_button.pack(pady=10)

        self.sentence_text = tk.Text(self, height=10, width=50)
        self.sentence_text.pack(pady=10)

        self.prev_button = tk.Button(self, text="Предыдущее предложение", command=self.show_prev_sentence)
        self.prev_button.pack(pady=5)

        self.next_button = tk.Button(self, text="Следующее предложение", command=self.show_next_sentence)
        self.next_button.pack(pady=5)

    def load_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.sentences = content.split('.')
                self.current_sentence_index = 0
                self.show_next_sentence()

    def show_prev_sentence(self):
        if self.sentences and self.current_sentence_index > 0:
            self.current_sentence_index -= 1
            self.show_sentence()

    def show_next_sentence(self):
        if self.sentences and self.current_sentence_index < len(self.sentences) - 1:
            self.current_sentence_index += 1
            self.show_sentence()
        else:
            messagebox.showinfo("Информация", "Больше нет предложений.")

    def show_sentence(self):
        sentence = self.sentences[self.current_sentence_index].strip()
        self.sentence_text.delete(1.0, tk.END)
        self.sentence_text.insert(tk.END, sentence)

'''
class SentenceAnalyzer(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Анализ предложения")
        self.geometry("500x400")

        self.sentences = []
        self.current_sentence_index = 0

        self.open_file_button = tk.Button(self, text="Открыть файл", command=self.load_file)
        self.open_file_button.pack(pady=10)

        self.sentence_text = tk.Text(self, height=10, width=50)
        self.sentence_text.pack(pady=10)

        self.next_button = tk.Button(self, text="Следующее предложение", command=self.show_next_sentence)
        self.next_button.pack(pady=10)

        self.close_button = tk.Button(self, text="Закрыть", command=self.destroy)
        self.close_button.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.sentences = content.split('.')
                self.current_sentence_index = 0
                self.show_next_sentence()

    def show_next_sentence(self):
        if self.sentences and self.current_sentence_index < len(self.sentences):
            sentence = self.sentences[self.current_sentence_index].strip()
            self.sentence_text.delete(1.0, tk.END)
            self.sentence_text.insert(tk.END, sentence)
            self.current_sentence_index += 1
        else:
            messagebox.showinfo("Информация", "Больше нет предложений.")
'''
class WordAnalyzer(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Анализ слова")
        self.geometry("500x400")

        self.word_label = tk.Label(self, text="Введите слово:")
        self.word_label.pack(pady=10)

        self.word_entry = tk.Entry(self)
        self.word_entry.pack(pady=10)

        self.analyze_button = tk.Button(self, text="Анализировать", command=self.analyze_word, bd=1)
        self.analyze_button.pack(pady=10)

        self.result_tree = ttk.Treeview(self, columns=('item', 'value'), show='headings')
        self.result_tree.heading('item', text='Характеристика')
        self.result_tree.heading('value', text='Значение')
        self.result_tree.pack(pady=13)

    def analyze_word(self):
        word = self.word_entry.get()

        if word:
            t = word_tokenizer(word)
            res = morphy_from_sentence(t) # список гепотез

            for i in range(len(res)):
                self.result_tree.insert('', tk.END, values=('Вариант', i+1 ))
                for k, v in res[i].items():
                    self.result_tree.insert('', tk.END, values=(k,v))



