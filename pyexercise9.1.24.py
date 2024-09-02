Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> variable1 = hello
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    variable1 = hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>> variable1 = 'hello'
>>> variable2 = 'world
SyntaxError: unterminated string literal (detected at line 1)
>>> variable2 = 'world'
>>> message = f'{variable1} {variable2}
SyntaxError: unterminated f-string literal (detected at line 1)
>>> message = f'{variable1} {variable2}
SyntaxError: unterminated f-string literal (detected at line 1)
>>> wizard_list = 'spider legs, toe of frog, bat wing, slug butter, snake dandruff'
>>> print(wizard_list)
spider legs, toe of frog, bat wing, slug butter, snake dandruff
>>> wizard_list = ['spider legs', 'toe of frog', 'bat wing', 'slug butter', 'snake danddruff']
>>> print(wizard_listt)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(wizard_listt)
NameError: name 'wizard_listt' is not defined. Did you mean: 'wizard_list'?
>>> print(wizard_list)
['spider legs', 'toe of frog', 'bat wing', 'slug butter', 'snake danddruff']
>>> variable1 = hello
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    variable1 = hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>> variable1 = 'hello'
>>> variable2 = 'world'
>>> print(f'{variable1} {variable2}')
hello world
>>> variable1 = 'this is liam'\s'
SyntaxError: unexpected character after line continuation character
>>> variable1 = "this is Liam's"
>>> variable2 = "world"
>>> print(f'{variable1} {variable2}')
this is Liam's world
