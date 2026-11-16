"""Робота 10: форма з опису (YAML) через GRID.

Запуск:     python praktyka/10-maket/forma_z_opysu.py
            python praktyka/10-maket/forma_z_opysu.py forma.yaml
"""
import sys
import tkinter as tk
import yaml

# Файл з описом форми: за замовчуванням forma.yaml
shliakh = sys.argv[1] if len(sys.argv) > 1 else "praktyka/10-maket/forma.yaml"

with open(shliakh, encoding="utf-8") as f:
    opys = yaml.safe_load(f)

vikno = tk.Tk()
vikno.title(opys["zaholovok"])
vikno.minsize(320, 200)

vikno.columnconfigure(0, weight=0)
vikno.columnconfigure(1, weight=1)

tk.Label(vikno, text=opys["zaholovok"], font=("Consolas", 16)).grid(row=0, column=0, columnspan=2, pady=10)

# Поля
rjadok = 1
for pole in opys.get("polia", []):
    tk.Label(vikno, text=pole["pidpys"] + ":").grid(row=rjadok, column=0, sticky="e", padx=6, pady=5)
    typ = pole.get("typ", "tekst")
    if typ == "parol":
        vidzhet = tk.Entry(vikno, show="•")
    elif typ == "chyslo":
        vidzhet = tk.Spinbox(vikno, from_=0, to=9999)
    else:
        vidzhet = tk.Entry(vikno)
    vidzhet.grid(row=rjadok, column=1, sticky="ew", padx=6)
    rjadok += 1

# Прапорці
for praporets in opys.get("praporci", []):
    tk.Checkbutton(vikno, text=praporets).grid(row=rjadok, column=0, columnspan=2, sticky="w", padx=6, pady=5)
    rjadok += 1

# Кнопки внизу
panel = tk.Frame(vikno)
panel.grid(row=rjadok, column=0, columnspan=2, sticky="e", padx=6, pady=10)
for knopka in opys.get("knopky", []):
    komanda = vikno.destroy if knopka == "Скасувати" else None
    tk.Button(panel, text=knopka, command=komanda).pack(side="left", padx=5)

vikno.mainloop()