filename = input("Enter file name (with extension): ")



try:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    lines = text.splitlines()
    words = text.split()
    chars = len(text)

    print("\n📊 File Analysis")
    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", chars)

except FileNotFoundError:
    print("❌ No such file found! Please check the name or path.")
