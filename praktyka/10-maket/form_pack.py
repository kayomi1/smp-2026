"""Робота 10: форма реєстрації через PACK.

Запуск:     python praktyka/10-maket/form_pack.py
Перевірка:  python praktyka/10-maket/perevir.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — pack")

# Що має бути у формі (README, крок 2):
#   заголовок «Реєстрація»;
#   чотири підписи з полями: Імʼя, Пошта, Телефон, Пароль — поле пароля з show="•";
#   прапорець «Погоджуюсь з умовами»;
#   кнопки «Зареєструватись» і «Скасувати» — внизу праворуч.
# Тут — ЛИШЕ pack. ryadok «підпис + поле» зручно зробити окремою tk.Frame, усередині — теж pack.

tk.Label(vikno, text="Реєстрація", font=("Consolas", 16)).pack(pady=15)

forma = tk.Frame(vikno)
forma.pack(padx=20, pady=5)

polya = [
    ("Імʼя:", False),
    ("Пошта:", False),
    ("Телефон:", False),
    ("Пароль:", True),
]

for pydpis, password in polya:
    ryadok = tk.Frame(forma)
    ryadok.pack(fill="x", padx=10,pady=2)

    tk.Label(ryadok, text=pydpis, width=10, anchor="w").pack(side="left")

    if password:
        tk.Entry(ryadok, width=25, show="•").pack(side="left")
    else:
        tk.Entry(ryadok, width=25).pack(side="left")

tk.Checkbutton(vikno, text="Погоджуюсь з умовами").pack(anchor="w", padx=20, pady=10)

buttons = tk.Frame(vikno)
buttons.pack(fill="x", padx=20, pady=10)
tk.Button(buttons, text="Зареєструватись").pack(side="left")
tk.Button(buttons, text="Скасувати", command=vikno.destroy).pack(side="right", padx=5)


vikno.mainloop()
