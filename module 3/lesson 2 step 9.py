from selenium import webdriver

'''
Форматирование строк
https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat

F-strings
https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36


'''
# browser = webdriver.Chrome()

s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

#  assert "login" in browser.current_url, # сообщение об ошибке.


def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

