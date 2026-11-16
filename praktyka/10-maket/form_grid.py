"""Робота 10: форма реєстрації через GRID.

Запуск:     python praktyka/10-maket/form_grid.py
Перевірка:  python praktyka/10-maket/perevir.py
"""
import tkinter as tk

PIDPYSY = {
    "uk": {
        "vikno": "Реєстрація — grid",
        "zagolovok": "Реєстрація",
        "imia": "Імʼя:",
        "poshta": "Пошта:",
        "telefon": "Телефон:",
        "parol": "Пароль:",
        "umovy": "Погоджуюсь з умовами",
        "skasuvaty": "Скасувати",
        "zareiestruvatys": "Зареєструватись",
    },
    "de": {
        "vikno": "Registrierung — grid",
        "zagolovok": "Registrierung",
        "imia": "Name:",
        "poshta": "E-Mail-Adresse:",
        "telefon": "Telefonnummer:",
        "parol": "Passwort:",
        "umovy": "Ich stimme den Bedingungen zu",
        "skasuvaty": "Abbrechen",
        "zareiestruvatys": "Registrieren",
    },
}

MOVA = "de"  # або "uk"
t = PIDPYSY[MOVA]

vikno = tk.Tk()
vikno.title(t["vikno"])

# Що має бути у формі (README, крок 2):
#   заголовок «Реєстрація»;
#   чотири підписи з полями: Імʼя, Пошта, Телефон, Пароль — поле пароля з show="•";
#   прапорець «Погоджуюсь з умовами»;
#   кнопки «Зареєструватись» і «Скасувати» — внизу праворуч.
# Тут — grid для заголовка, підписів, полів і прапорця. Кнопки можна зібрати у tk.Frame (усередині — будь-який менеджер).

vikno.columnconfigure(0, weight=0)
vikno.columnconfigure(1, weight=1)

tk.Label(vikno, text=t["zagolovok"], font=("Consolas", 16)).grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(vikno, text=t["imia"]).grid(row=1, column=0, sticky="e", padx=6, pady=5)
tk.Entry(vikno).grid(row=1, column=1, sticky="ew", padx=6)
tk.Label(vikno, text=t["poshta"]).grid(row=2, column=0, sticky="e", padx=6, pady=5)
tk.Entry(vikno).grid(row=2, column=1, sticky="ew", padx=6)
tk.Label(vikno, text=t["telefon"]).grid(row=3, column=0, sticky="e", padx=6, pady=5)
tk.Entry(vikno).grid(row=3, column=1, sticky="ew", padx=6)
tk.Label(vikno, text=t["parol"]).grid(row=4, column=0, sticky="e", padx=6, pady=5)
tk.Entry(vikno, show="•").grid(row=4, column=1, sticky="ew", padx=6)
tk.Checkbutton(vikno, text=t["umovy"]).grid(row=5, column=0, columnspan=2, pady=10)

frame = tk.Frame(vikno)
frame.grid(row=6, column=0, columnspan=2, sticky="e")
tk.Button(frame, text=t["zareiestruvatys"]).pack(side="left")
tk.Button(frame, text=t["skasuvaty"], command=vikno.destroy).pack(side="right")

vikno.mainloop()
