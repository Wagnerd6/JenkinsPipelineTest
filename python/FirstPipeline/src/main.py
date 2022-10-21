def select_anagrams(words: list[str]) -> list[str]:
    return [word for word in words if check_anagram(word)]


def check_anagram(word: str) -> bool:
    return word.lower() == word[::-1].lower()
