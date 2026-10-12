import re
from collections import Counter

shablon = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)'
    r'.*?'
    r'\[(?P<chas>[^\]]+)\]'
    r' "(?P<metod>\w+) (?P<shlyah>\S+)[^"]*"'
    r' (?P<kod>\d{3})'
)

rozibrano = 0
propusheno = 0
ip = Counter()
kody = Counter()
pomylky_5xx = []

with open("data/access.log", encoding="utf-8") as f:
    for ryadok in f:
        m = shablon.search(ryadok)
        if not m:
            propusheno += 1
            continue
        rozibrano += 1
        ip[m["ip"]] += 1
        kody[m["kod"]] += 1
        if m["kod"].startswith("5"):
            pomylky_5xx.append((m["chas"], m["shlyah"]))

print(f"1. Розібрано: {rozibrano}, пропущено: {propusheno}")

print("\n2. Топ-5 IP:")
for adresa, kilkist in ip.most_common(5):
    print(f"   {kilkist}: {adresa}")

print("\n3. Запити за кодами:")
for kod, kilkist in sorted(kody.items()):
    print(f"   {kod}: {kilkist}")

print(f"\n4. Помилки 5xx ({len(pomylky_5xx)}):")
for chas, shlyah in pomylky_5xx:
    print(f"   {chas}  {shlyah}")