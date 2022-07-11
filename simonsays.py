n = int(input())

for i in range(n):
    text = input()
    if "Simon says" in text:
        text = text.replace("Simon says ", "")
        print(text)