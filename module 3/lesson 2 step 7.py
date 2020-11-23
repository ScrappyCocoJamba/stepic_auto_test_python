

'''
Форматирование строк
https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat

F-strings
https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36


'''

# .format()
print("{} Let's count together: {}, then goes {}, and then {}. Created by {} {}"
      .format(">>>>>>", "one", "two", "three", "ScrappyCoco", "<<<<<<"))


# f-strings.
str1 = "one"
str2 = "two"
str3 = "three"
str4 = "Created by ScrappyCoco"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}. {str4}")

actual_result = "abrakadabra"
fstr = f"Wrong text, got {actual_result}, something wrong"
print(fstr)

