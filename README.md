[![CI/CD GitHub Actions](https://github.com/pollyaana/testingSoftware2/actions/workflows/testing.yml/badge.svg)](https://github.com/pollyaana/testingSoftware2/actions/workflows/testing.yml)
[![Coverage Status](https://coveralls.io/repos/github/pollyaana/testingSoftware2/badge.svg)](https://coveralls.io/github/pollyaana/testingSoftware2)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=pollyaana_testingSoftware2&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=pollyaana_testingSoftware2)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=pollyaana_testingSoftware2&metric=bugs)](https://sonarcloud.io/summary/new_code?id=pollyaana_testingSoftware2)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=pollyaana_testingSoftware2&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=pollyaana_testingSoftware2)

# Аттестационные тесты #
| Название                       | Описание                                                                                                     | Тип теста  | Входные данные          | Ожидаемый результат                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|--------------------------------------------------------------------------------------------------------------|------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_huffman_tree_building     | Проверяет, что дерево Хаффмана строится корректно.            | Позитивный | test_string="aabbcc"    | Длина словаря=3, a,b,c присутсвуют в словаре |
| test_huffman_encoding   | Проверяет, что строка кодируется корректно.            | Позитивный| test_string="aabbcc"        | Тип строка, длина больше нуля.
| test_single_character_encoding   | Проверяет кодирование строки из одного символа.             | Негативный | test_string="a"        | encoded="0", decoded=test_string
| test_huffman_code_length   | Проверяет, что длина строки больше нуля.            | Позитивный| test_string="aabbcc"        | Длина строки больше нуля.
| test_huffman_decoding   | Проверяет, что закодированная строка декодируется обратно в исходную          | Позитивный | encoded="1010111100"        | True
| test_empty_string_encoding   | Проверяет обработку пустой строки        | Негативный | test_string=""        | V

# Блочные тесты #
| Класс          | Название                              | Описание                                                                                                               | Тип теста     | Входные данные                                                                    | Ожидаемый результат                     |
|----------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------|-----------------------------------------------------------------------------------|-----------------------------------------|
| TestBlock  | test_huffman_tree_special_characters              | Проверяет как функция обрабатывает специальные символы                        | негативный    | input_string = "!@#$%^&*()"|True |
| TestBlock  | test_encode_single_character                     | Проверяет обработку строки из одного символа                                                | негативный    | test_string="a | True | 
| TestBlock  | test_encode_empty_string            | Проверяет обработку пустой строки                                      | негативный    |  test_string="" | True   |                     
| TestBlock  | test_encode            | Проверяет кодирование                                      | позитивный    |  test_string="hello_world" | True   |                     

# Интеграционные тесты #
| Название | Описание | Тип теста | Входные данные | Ожидаемый результат |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|-------------------------------------|-----------------------------------|
| test_encode_decode | Проверяет правильность кодирования и декодирования сообщений. | Позитивный | original_string ="hello_world", "hello huffman", "a", "" | True, переданное сообщение равно декодированной строке |
| test_codes_length | Проверяет, что длина кода не длиннее 1\2 длины строки. | Позитивный | check_code_len = "sunny", "abracadabra" | Полученный код меньше длины сообщения в два раза |
| test_incorrect_string | Проверяет обработку кодирования небуквенной строки. | Негативный | original_string ="1233" |TypeError |
| test_huffman_tree_root | Проверяет, что структура дерева Хаффмана построена верно. | Позитивный | string = "data compression" | huffman_tree.root не равно None |
| test_type_codes | Проверяет, что тип данных кодов - словарь. | Позитивный | string = "data compression" | huffman_tree.root тип равен dict |
| test_empty_string | Проверяет обработку кодирования пустой строки. | Негативный | original_string ="" | ValueError |
