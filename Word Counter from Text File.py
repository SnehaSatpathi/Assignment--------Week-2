with open("sample.txt", "r") as f:
    text = f.read()

words = text.split()
lines = text.split("\n")

print("Words:", len(words))
print("Lines:", len(lines))
print("Characters:", len(text))
