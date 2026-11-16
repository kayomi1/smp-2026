"""Робота 10: форма реєстрації через PLACE.

Запуск:     python praktyka/10-maket/form_place.py
Перевірка:  python praktyka/10-maket/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — place")
vikno.geometry("380x300")

# Що має бути у формі (README, крок 2):
#   заголовок «Реєстрація»;
#   чотири підписи з полями: Імʼя, Пошта, Телефон, Пароль — поле пароля з show="•";
#   прапорець «Погоджуюсь з умовами»;
#   кнопки «Зареєструватись» і «Скасувати» — внизу праворуч.
# Тут — ЛИШЕ place: x, y у пікселях (або relx, rely). Розмір вікна задайте явно, як нижче.

tk.Label(vikno, text="Реєстрація", font=("Consolas", 16)).place(x=125, y=12)

polya = [
    ("Імʼя:", False),
    ("Пошта:", False),
    ("Телефон:", False),
    ("Пароль:", True),
]

y = 55
for pydpis, password in polya:
    tk.Label(vikno, text=pydpis, anchor="w").place(x=20, y=y, width=90, height=24)
    if password:
        tk.Entry(vikno, show="•").place(x=120, y=y, width=240, height=24)
    else:
        tk.Entry(vikno).place(x=120, y=y, width=240, height=24)
    y += 35

tk.Checkbutton(vikno, text="Погоджуюсь з умовами").place(x=20, y=200)

tk.Button(vikno, text="Зареєструватись").place(x=140, y=250, width=90, height=30)
tk.Button(vikno, text="Скасувати", command=vikno.destroy).place(x=240, y=250, width=120, height=30)


vikno.mainloop()
