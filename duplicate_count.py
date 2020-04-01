def duplicate_count(text):
    seen = set()
    return len({char for char in text.upper().lower() if char in seen or seen.add(char) is not None})
