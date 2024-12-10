[![CI/CD GitHub Actions](https://github.com/pollyaana/testingSoftware2/actions/workflows/testing.yml/badge.svg)](https://github.com/pollyaana/testingSoftware2/actions/workflows/testing.yml)
[![Coverage Status](https://coveralls.io/repos/github/pollyaana/testingSoftware2/badge.svg)](https://coveralls.io/github/pollyaana/testingSoftware2)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=pollyaana_testingSoftware2&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=pollyaana_testingSoftware2)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=pollyaana_testingSoftware2&metric=bugs)](https://sonarcloud.io/summary/new_code?id=pollyaana_testingSoftware2)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=pollyaana_testingSoftware2&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=pollyaana_testingSoftware2)

# Аттестационные тесты #
| Название                       | Описание                                                                                                     | Тип теста  | Входные данные          | Ожидаемый результат                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|--------------------------------------------------------------------------------------------------------------|------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_huffman_tree_building     | Проверяет, что дерево Хаффмана строится корректно.            | Позитивный | test_string="aabbcc"    | True |
| test_huffman_encoding   | Проверяет, что строка кодируется корректно.            | Позитивный| test_string="aabbcc"        | True
| test_single_character_encoding   | Проверяет кодирование строки из одного символа.             | Негативный | test_string="a"        | True
| test_huffman_enoding   | Проверяет, что строка кодируется корректно.            | Позитивный| test_string="aabbcc"        | True
| test_huffman_decoding   | Проверяет длину кодов символов           | Позитивный | test_string="aabbcc"        | True
| test_empty_string_encoding   | Проверяет обработку пустой строки        | Негативный | test_string=""        | True

# Блочные тесты #
| Класс          | Название                              | Описание                                                                                                               | Тип теста     | Входные данные                                                                    | Ожидаемый результат                     |
|----------------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------|-----------------------------------------------------------------------------------|-----------------------------------------|
| TestBlock  | test_huffman_tree_special_characters              | Проверяет как функция обрабатывает специальные символы                        | негативный    | input_string = "!@#$%^&*()"|True |
| TestBlock  | test_encode_single_character                     | Проверяет обработку строки из одного символа                                                | негативный    | test_string="a | True | 
| TestBlock  | test_encode_empty_string            | Проверяет обработку пустой строки                                      | негативный    |  test_string="" | True   |                     
| TestBlock  | test_encode            | Проверяет кодирование                                      | позитивный    |  test_string="hello_world" | True   |                     
