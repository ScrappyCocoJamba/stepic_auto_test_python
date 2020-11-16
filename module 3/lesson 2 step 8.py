
'''
Форматирование строк
https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat

F-strings
https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36


'''

# Функция сравнения ожидаемого результата с фактическим
def test_input_text(expected_result, actual_result):

    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

