from sys import prefix

import pygtrie

class LongestCommonWord(pygtrie.Trie):
    def __init__(self):
        super().__init__()

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise TypeError('strings must be a list of strings')

        if not strings:
            return ""

        self.clear()

        for i, word in enumerate(strings):
            self[word] = i

        prefix = ""
        node = self._root
        current = ""
        while True:
            if len(node.children) != 1:
                break
            char, next_node = next(iter(node.children.iteritems()))
            current += char

            if not self.has_subtrie(current) or len(self.keys(prefix=current)) < len(strings):
                break
            prefix = current
            node = next_node
        return prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""

    print("✅ All tests passed!")
