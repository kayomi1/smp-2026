"""Робота 10: справжнє вікно з рамками.

Запуск:     python praktyka/10-maket/vikno_ramky.py
"""
import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — рамки")
vikno.minsize(560, 320)

smuga_stanu = tk.Label(vikno, text="Готово до заповнення", anchor="w", padx=8, relief="sunken")
smuga_stanu.pack(side="bottom", fill="x")

osnovna = tk.Frame(vikno)
osnovna.pack(side="top", fill="both", expand=True)

# Ліва рамка
forma = tk.Frame(osnovna, padx=12, pady=8)
forma.pack(side="left", fill="both", expand=True)

forma.columnconfigure(0, weight=0)
forma.columnconfigure(1, weight=1)

tk.Label(forma, text="Реєстрація", font=("Consolas", 16)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(forma, text="Імʼя:").grid(row=1, column=0, sticky="e", padx=6, pady=5)
tk.Entry(forma).grid(row=1, column=1, sticky="ew", padx=6)

tk.Label(forma, text="Пошта:").grid(row=2, column=0, sticky="e", padx=6, pady=5)
tk.Entry(forma).grid(row=2, column=1, sticky="ew", padx=6)

tk.Label(forma, text="Телефон:").grid(row=3, column=0, sticky="e", padx=6, pady=5)
tk.Entry(forma).grid(row=3, column=1, sticky="ew", padx=6)

tk.Label(forma, text="Пароль:").grid(row=4, column=0, sticky="e", padx=6, pady=5)
tk.Entry(forma, show="•").grid(row=4, column=1, sticky="ew", padx=6)

tk.Checkbutton(forma, text="Погоджуюсь з умовами").grid(row=5, column=0, columnspan=2, pady=10)

buttons = tk.Frame(forma)
buttons.grid(row=6, column=0, columnspan=2, sticky="e", pady=10)
tk.Button(buttons, text="Скасувати", command=vikno.destroy).pack(side="left", padx=5)
tk.Button(buttons, text="Зареєструватись").pack(side="left")

pidkazka = tk.LabelFrame(osnovna, text="Підказка", padx=10, pady=10, width=180)
pidkazka.pack(side="right", fill="y", padx=(0, 12), pady=8)
pidkazka.pack_propagate(False)

tk.Label(
    pidkazka,
    text="Пароль має містити щонайменше 8 символів. Пошта повинна мати символ @.",
    wraplength=150,
    justify="left",
    anchor="nw",
).pack(fill="both", expand=True)

vikno.mainloop()