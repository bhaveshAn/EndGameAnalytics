class TrieNode(object):
    def __init__(self, char):

        self.char = char
        self.children = []
        self.word_finished = False


class StockSearch(object):
    def __init__(self):

        self.root = TrieNode("*")

    def insert(self, word):

        node = self.root

        for char in word:

            found_in_child = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node
        node.word_finished = True

    def search(self, word):

        node = self.root
        expected = ""
        if not self.root.children:
            return False, 0

        for char in word:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    expected += child.char
                    char_not_found = False
                    node = child
                    break

            if char_not_found:
                while node.children:
                    expected += node.children[0].char
                    node = node.children[0]
                return False, expected
        if not node.word_finished:
            while node.children:
                expected += node.children[0].char
                node = node.children[0]
            return False, expected
        return True, expected
