import tkinter as tk
from tkinter import filedialog


class ViewerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Просмотр предложений")

        self.sentences = []
        self.current_sentence_index = tk.IntVar(value=0)
        self.current_sentence_words = []

        # Создаем элементы интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Создаем кнопку для выбора файла
        self.select_file_button = tk.Button(self.master, text="Выбрать файл", command=self.load_file)
        self.select_file_button.pack(pady=10)

        # Создаем метку для отображения предложения
        self.sentence_label = tk.Label(self.master, text="")
        self.sentence_label.pack(pady=10)

        # Создаем таблицу для отображения слов и их номеров в предложении
        self.table_frame = tk.Frame(self.master)
        self.table_frame.pack()

        self.word_table = tk.Text(self.table_frame, width=30, height=10)
        self.word_table.grid(row=0, column=0, padx=5)

        self.number_table = tk.Text(self.table_frame, width=10, height=10)
        self.number_table.grid(row=0, column=1, padx=5)

        # Создаем кнопки для навигации по предложениям
        self.navigation_frame = tk.Frame(self.master)
        self.navigation_frame.pack(pady=10)

        self.prev_button = tk.Button(self.navigation_frame, text="Предыдущее", command=self.show_previous_sentence)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.next_button = tk.Button(self.navigation_frame, text="Следующее", command=self.show_next_sentence)
        self.next_button.grid(row=0, column=1, padx=5)

    def load_file(self):
        # Открываем диалоговое окно для выбора файла
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            # Читаем текст из файла и разбиваем на предложения
            with open(file_path, "r", encoding="utf-8") as file:
                self.sentences = file.read().split(".")
                # Удаляем пустые строки
                self.sentences = [sentence.strip() for sentence in self.sentences if sentence.strip()]

            # Показываем первое предложение
            self.show_sentence(0)

    def show_sentence(self, index):
        if index < 0 or index >= len(self.sentences):
            self.sentence_label.config(text="Предложения с данным номером не существует")
            self.word_table.delete("1.0", tk.END)
            self.number_table.delete("1.0", tk.END)
        else:
            self.current_sentence_index.set(index)
            sentence = self.sentences[index]
            self.sentence_label.config(text=sentence)
            words = sentence.split()
            self.current_sentence_words = words
            self.show_words_and_numbers(words)

    def show_words_and_numbers(self, words):
        self.word_table.delete("1.0", tk.END)
        self.number_table.delete("1.0", tk.END)
        for i, word in enumerate(words, start=1):
            self.word_table.insert(tk.END, word + "\n")
            self.number_table.insert(tk.END, str(i) + "\n")

    def show_previous_sentence(self):
        self.show_sentence(self.current_sentence_index.get() - 1)

    def show_next_sentence(self):
        self.show_sentence(self.current_sentence_index.get() + 1)


# Создаем главное окно приложения


'''
    root = tk.Tk()
    app = ViewerApp(root)
    root.mainloop()

'''