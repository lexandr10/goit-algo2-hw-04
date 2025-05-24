from pygtrie import Trie

class Homework(Trie):
    def __init__(self):
        super().__init__()
        self._words = set()

    def put(self, key, value):
        if not isinstance(key, str):
            raise TypeError('key must be a string')
        self[key] = value
        self._words.add(key)

    def count_words_with_suffix(self, pattern)->int:
        if not isinstance(pattern, str):
            raise TypeError('pattern must be a string')
        count = sum(1 for word in self._words if word.endswith(pattern))
        return count

    def has_prefix(self, prefix)->bool:
        if not isinstance(prefix, str):
            raise TypeError('prefix must be a string')
        return self.has_subtrie(prefix)


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

    print("✅ All tests passed!")


