import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


class HuffmanTree:
    def __init__(self, string):
        self.string = string
        self.root = None
        self.code = {}

    def build_tree(self):
        heap = []
        for ch, freq in Counter(self.string).items():
            heap.append((freq, len(heap), Leaf(ch)))
        heapq.heapify(heap)
        count = len(heap)

        while len(heap) > 1:
            freq1, count1, left = heapq.heappop(heap)
            freq2, count2, right = heapq.heappop(heap)
            heapq.heappush(heap, (freq1 + freq2, count, Node(left, right)))
            count += 1

        if heap:
            [(_freq, _count, self.root)] = heap
            self._generate_codes(self.root, self.code, "")

    def _generate_codes(self, node, code, acc):
        """Защищённый метод для генерации кодов символов."""
        if isinstance(node, Leaf):
            code[node.char] = acc or "0"
        else:
            node.walk(code, acc)

    def get_codes(self):
        return self.code

    def print_codes(self):
        print("Символы и их коды:")
        for char, code in sorted(self.code.items()):
            print(f"'{char}': {code}")


class HuffmanCoder:
    def __init__(self, huffman_tree):
        self.huffman_tree = huffman_tree

    def encode(self):
        self.huffman_tree.build_tree()
        encoded = "".join(self.huffman_tree.get_codes()[ch] for ch in self.huffman_tree.string)
        return encoded

    def decode(self, encoded):
        decoded = []
        node = self.huffman_tree.root
        for bit in encoded:
            if len(encoded) == 1:
                decoded.append(node.char)
                break
            node = node.left if bit == '0' else node.right

            if isinstance(node, Leaf):
                decoded.append(node.char)
                node = self.huffman_tree.root

        return ''.join(decoded)


#input_string = input("Введите строку, чтобы закодировать ее алгоритмом Хаффмана: ")
input_string = "привет"
huffman_tree = HuffmanTree(input_string)
huffman_coder = HuffmanCoder(huffman_tree)

encoded = huffman_coder.encode()
print("Закодированная строка: " + encoded)

huffman_tree.print_codes()

decoded_string = huffman_coder.decode(encoded)
print(f"Декодированная строка: " + decoded_string)
