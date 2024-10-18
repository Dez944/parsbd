import tkinter as tk
from tkinter import ttk
from strctr import cl

def on_test_selected(event):
    """Функция, вызываемая при выборе теста"""
    selected_item = tree.focus()  # Получаем выбранный элемент
    test_name = tree.item(selected_item)['text']  # Извлекаем текст названия теста

    if test_key in cl:
        # Очистка текстового поля перед добавлением новых данных
        log_text.delete(1.0, tk.END)
        # Формируем строки для отображения кортежей
        logs = "\n".join([f"({x[0]}, {x[1]})" for x in cl[test_key]])
        log_text.insert(tk.END, logs)


# Создаем основное окно
root = tk.Tk()
root.title("Log Viewer")

# Создаем фрейм для дерева и текста
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Дерево для тестов и логов
tree = ttk.Treeview(frame)
tree.pack(side="left", fill="both", expand=True)

# Скроллбар для дерева
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scrollbar.pack(side="left", fill="y")
tree.configure(yscroll=scrollbar.set)

# Добавляем названия тестов и логи в дерево
for test_key, logs in cl.items():
    # Добавляем родительский элемент (название теста)
    test_id = tree.insert("", "end", text=f"Test {test_key}")

    # Добавляем дочерние элементы (кортежи)
    for log in logs:
        tree.insert(test_id, "end", text=f"({log[0]}, {log[1]})")

# Текстовое поле для отображения логов
log_text = tk.Text(root, height=10, wrap="word")
log_text.pack(fill="both", expand=True)

# Привязка события выбора элемента в дереве
tree.bind("<<TreeviewSelect>>", on_test_selected)

# Запускаем главное окно
root.mainloop()