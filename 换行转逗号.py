with open("filename.txt", "r") as f:
    content = f.read()
text =""
text = text.replace("\n", ",")
print(text)