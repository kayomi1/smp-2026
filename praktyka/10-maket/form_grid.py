"""Робота 10: форма реєстрації через GRID.

Запуск:     python praktyka/10-maket/form_grid.py
Перевірка:  python praktyka/10-maket/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — grid")

# Що має бути у формі (README, крок 2):
#   заголовок «Реєстрація»;
#   чотири підписи з полями: Імʼя, Пошта, Телефон, Пароль — поле пароля з show="•";
#   прапорець «Погоджуюсь з умовами»;
#   кнопки «Зареєструватись» і «Скасувати» — внизу праворуч.
# Тут — grid для заголовка, підписів, полів і прапорця. Кнопки можна зібрати у tk.Frame (усередині — будь-який менеджер).

tk.Label(vikno, text="Реєстрація", font=("Consolas", 16)).grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(vikno, text="Імʼя:").grid(row=1, column=0, sticky="e", padx=6, pady=5)
tk.Entry(vikno).grid(row=1, column=1, sticky="ew", padx=6)
tk.Label(vikno, text="Пошта:").grid(row=2, column=0, sticky="e", padx=6, pady=5)
tk.Entry(vikno).grid(row=2, column=1, sticky="ew", padx=6)
tk.Label(vikno, text="Телефон:").grid(row=3, column=0, sticky="e", padx=6, pady=5)
tk.Entry(vikno).grid(row=3, column=1, sticky="ew", padx=6)
tk.Label(vikno, text="Пароль:").grid(row=4, column= 0, sticky="e", padx=6, pady=5)
tk.Entry(vikno, show="•").grid(row=4, column=1, sticky="ew", padx=6)
tk.Checkbutton(vikno, text="Погоджуюсь з умовами").grid(row=5, column=0, columnspan=2, pady=10)

frame = tk.Frame(vikno)
frame.grid(row=6, column=0, columnspan=2, sticky="e")
tk.Button(frame, text="Зареєструватись").pack(side="right")
tk.Button(frame, text="Скасувати", command=vikno.destroy).pack(side="right")

vikno.mainloop()
