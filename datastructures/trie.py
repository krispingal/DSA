class TrieNode:
    def __init__(self):
        self.children: list[TrieNode] = [None] * 26
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _get_char(self, c: str) -> int:
        return ord(c.lower()) - ord('a')
    
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            ic = self._get_char(c)
            if not cur.children[ic]:
                cur.children[ic] = TrieNode()
            cur = cur.children[ic]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            ic = self._get_char(c)
            if not cur.children[ic]:
                return False
            cur = cur.children[ic]
        return cur.is_end
    
    def prefixSearch(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            ic = self._get_char(c)
            if not cur.children[ic]:
                return False
            cur = cur.children[ic]
        return True

    def shortestRoot(self, pre: str) -> str:
        cur = self.root
        for i in range(len(pre)):
            ic = self._get_char(pre[i])
            if not cur.children[ic]:
                return pre[:i]
            cur = cur.children[ic]
            if cur.is_end:
                return pre[: i+1]
        return pre


if __name__ == '__main__':
    trie = Trie()
    words = ['apple', 'apply', 'Aptitude', 'amplitude', 'astute', 'arid', 'cat', 'cart', 'carp', 'car']
    for w in words:
        trie.insert(w)
    assert trie.search('Apply')
    assert not trie.search('apricot')
    assert trie.prefixSearch('ca')
    assert not trie.prefixSearch('ac')
    assert trie.shortestRoot('cartographer') == 'car'
    assert trie.shortestRoot('advent') == 'a'

