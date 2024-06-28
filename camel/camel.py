text = input("camelCase: ").strip()


if text.islower():
    None

else:
    for c in text:
        if c.isupper():
            text = text.replace(c, "_" + c.lower())

print("snake_case: " + text)
