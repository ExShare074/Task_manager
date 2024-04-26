# будем писать программу-приложение для управления задачами
import tkinter as tk

def add_task():  #ФУНКЦИЯ ДЛЯ ДОБАВЛЕНИЯ задач
    task = task_entry.get()  #ПОЛУЧЕНИЕ ЗНАЧЕНИЯ ИЗ ОКНА ВВОДА
    if task:  #ПРОВЕРКА НЕ ПУСТОГО ОКНА ВВОДА
        task_listbox.insert(tk.END, task)  #ДОБАВЛЕНИЕ ЗАДАЧИ В СПИСОК
        task_entry.delete(0, tk.END)  #с этой функцией задаем от куда и до куда удаляем, (0 начало, END конец)

def delete_task():  #ФУНКЦИЯ ДЛЯ УДАЛЕНИЯ задач
    selected_task = task_listbox.curselection()  #ПОЛУЧЕНИЕ ЗНАЧЕНИЯ ИЗ ОКНА СПИСКА
    if selected_task:  #ПРОВЕРКА НЕ ПУСТОГО ОКНА СПИСКА
        task_listbox.delete(selected_task)  #УДАЛЕНИЕ ЗАДАЧИ ИЗ СПИСКА

def mark_task():  #ФУНКЦИЯ ДЛЯ ОТМЕТКИ выполненной задачи
    selected_task = task_listbox.curselection()  #ПОЛУЧЕНИЕ ЗНАЧЕНИЯ ИЗ ОКНА СПИСКА
    if selected_task:  #ПРОВЕРКА НЕ ПУСТОГО ОКНА СПИСКА
        task_listbox.itemconfig(selected_task, bg="lightgreen")  #МЕНЯЕМ ЦВЕТ ЗАДАЧИ НА ЛЮБОЙ


root = tk.Tk()
root.title("Управление задачами")  #ЗАГОЛОВОК
root.configure(background="DarkSeaGreen2")  #ТУТ МЕНЯЕМ ЦВЕТ ФОНА


text1 = tk.Label(root, text="Задачи:", font=("gilroy", 14, "bold"), fg="black", bg="DarkSeaGreen4")  #ТИПО МЕТКА
text1.pack(pady=5)  #ЧЕРЕЗ PACK УПАКОВКА ВИДЖЕТА


task_entry = tk.Entry(root, width=30, bg="gainsboro")  #ОКНО ВВОДА ДАННЫХ
task_entry.pack(pady=10)


add_task_button = tk.Button(root, text="добавить задачу", command=add_task)  #КНОПКА ДЛЯ ДОБАВЛЕНИЯ ЗАДАЧИ
add_task_button.pack(padx=10, pady=10)  


delete_task_button = tk.Button(root, text="удалить задачу", command=delete_task)  #КНОПКА ДЛЯ УДАЛЕНИЯ ЗАДАЧИ
delete_task_button.pack(padx=10, pady=10)


mark_task_button = tk.Button(root, text="отметить выполненную задачу", command=mark_task)  #КНОПКА ДЛЯ ОТМЕТКИ ЗАДАЧИ
mark_task_button.pack(padx=10, pady=10)


text2 = tk.Label(root, text="Список задач:", font=("gilroy", 14, "bold"), bg="DarkSeaGreen4")  #МЕТКА СПИСКА ЗАДАЧ
text2.pack(pady=10)


task_listbox = tk.Listbox(root,height=10, width=50, bg="grey46")  #СПИСОК ЗАДАЧ
task_listbox.pack(padx=10, pady=10)



root.mainloop()  #ГЛАВНЫЙ ЦИКЛ ОБРАБОТКИ СОБЫТИЙ
