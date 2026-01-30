def starts_with(text, char):
    if not text:        # handles empty string safely
        return False
    return text[0] == char

word = "Python"
print(f"Starts with 'P': {starts_with(word, 'P')}")
print(f"Starts with 'J': {starts_with('', 'J')}")

