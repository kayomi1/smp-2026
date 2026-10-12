with open("data/words.txt", encoding="utf-8") as f:
    for ryadok in f:
        print(ryadok.rstrip().upper())


total = 0.0
count = 0

with open("data/mbox-short.txt", encoding="utf-8") as f:
    for ryadok in f:
        ryadok = ryadok.strip()
        if ryadok.startswith("X-DSPAM-Confidence:"):
            value = float(ryadok.split(":")[1])
            total += value
            count += 1

print("Рядків:", count)
print("Середнє:", total / count)