import unittest
import pytest
from main import HuffmanTree, HuffmanCoder

class TestAttest:
    @pytest.fixture
    def huffman_coder(self):
        input_string = "aabbcc"
        huffman_tree = HuffmanTree(input_string)
        coder = HuffmanCoder(huffman_tree)
        coder.encode()
        return coder

    def test_huffman_tree_building(self, huffman_coder):
        """Проверяем, что дерево Хаффмана строится корректно."""
        codes = huffman_coder.huffman_tree.get_codes()
        assert len(codes) == 3
        assert 'a' in codes
        assert 'b' in codes
        assert 'c' in codes

    def test_huffman_encoding(self, huffman_coder):
        """Проверяем, что строка кодируется корректно."""
        encoded = huffman_coder.encode()
        assert isinstance(encoded, str)
        assert len(encoded) > 0

    def test_huffman_decoding(self, huffman_coder):
        """Проверяем, что закодированная строка декодируется обратно в исходную."""
        original_string = "aabbcc"
        encoded = huffman_coder.encode()
        decoded = huffman_coder.decode(encoded)
        assert decoded == original_string

    def test_huffman_code_length(self, huffman_coder):
        """Проверяем длину кодов символов."""
        codes = huffman_coder.huffman_tree.get_codes()
        for code in codes.values():
            assert len(code) > 0

    def test_single_character_encoding(self):
        """Проверяем кодирование строки из одного символа."""
        input_string = "a"
        huffman_tree = HuffmanTree(input_string)
        huffman_coder = HuffmanCoder(huffman_tree)

        encoded = huffman_coder.encode()
        decoded = huffman_coder.decode(encoded)

        assert encoded == "0"
        assert decoded == input_string

    def test_empty_string_encoding(self):
        """Проверяем кодирование пустой строки."""
        input_string = ""
        huffman_tree = HuffmanTree(input_string)
        huffman_coder = HuffmanCoder(huffman_tree)

        encoded = huffman_coder.encode()
        decoded = huffman_coder.decode(encoded)

        assert encoded == ""
        assert decoded == input_string

class TestBlock:

    def test_encode(self):
        """Тестирование кодирования"""
        test_string = "hello_world"
        encoded_string = "11101111101011000000111001010011"
        huffman_tree = HuffmanTree(test_string)
        huffman_coder = HuffmanCoder(huffman_tree)

        assert encoded_string == huffman_coder.encode()

    def test_encode_single_character(self):
        original_string = 'a'
        expected_encode = '0'
        huffman_tree = HuffmanTree(original_string)
        huffman_coder = HuffmanCoder(huffman_tree)
        assert expected_encode == huffman_coder.encode()

    def test_encode_empty_string(self):
        original_string = ''
        expected_encode = ''
        huffman_tree = HuffmanTree(original_string)
        huffman_coder = HuffmanCoder(huffman_tree)
        assert expected_encode == huffman_coder.encode()

    def test_huffman_tree_special_characters(self):
        """Проверка обработки строки со специальными символами."""
        input_string = "!@#$%^&*()"
        huffman_tree = HuffmanTree(input_string)
        huffman_coder = HuffmanCoder(huffman_tree)

        encoded = huffman_coder.encode()

        # Проверяем, что кодирование не дает ошибки
        assert isinstance(encoded, str)

        decoded_string = huffman_coder.decode(encoded)

        # Декодирование должно вернуть исходную строку
        assert decoded_string == input_string


class TestIntegration:
    @pytest.mark.parametrize("original_string", [
        "hello_world",
        "hello huffman",
        "a",
        ""
    ])
    def test_encode_decode(self, original_string):
        """Тестирование кодирования и декодирования."""
        huffman_tree = HuffmanTree(original_string)
        huffman_coder = HuffmanCoder(huffman_tree)

        encoded_string = huffman_coder.encode()
        decoded_string = huffman_coder.decode(encoded_string)

        assert original_string == decoded_string

    @pytest.mark.parametrize("check_code_len", ["sunny", "abracadabra"])
    def test_codes_length(self, check_code_len):
        """Тестирование длины кодов: коды не должны быть длиннее 1/2 длины строки."""
        huffman_tree = HuffmanTree(check_code_len)
        huffman_tree.build_tree()
        codes = huffman_tree.get_codes()

        assert all(len(code) <= len(check_code_len) // 2 for code in codes.values())

    def test_huffman_tree_root(self):
        """Проверка структуры дерева Хаффмана."""
        test_string = "data compression"

        huffman_tree = HuffmanTree(test_string)
        huffman_tree.build_tree()

        assert huffman_tree.root is not None

    def test_type_codes(self):
        test_string = "data compression"

        huffman_tree = HuffmanTree(test_string)
        huffman_tree.build_tree()
        codes = huffman_tree.get_codes()
        assert isinstance(codes, dict)
