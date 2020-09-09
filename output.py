Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 25 / 5
5.0
>>> 10 / 3

3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is Ties')
Mijn naam is Ties
>>> naam = 'Ties'
>>> print(naam)
Ties
>>> print(naam.upper())
TIES
>>> print(naam[0:2])
Ti
>>> print(naam[::-1])
seiT
>>> leeftijd = 16
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar? ')
Hallo Ties ben je al 16 jaar? 
>>> leeftijd = leeftijd + 1
>>> leeftijd
17
>>> leeftijd -=1
>>> leeftijd
16
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
	elif leeftijd > 18:
		
SyntaxError: invalid syntax
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
    elif leeftijd > 18:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    
Over 2 jaar wordt je 18
>>> from random import randint
>>> randint (0,1000)
647
>>> willekeurig_getal
print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal)
      
SyntaxError: multiple statements found while compiling a single statement
>>> willekeurig_getal
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    willekeurig_getal
NameError: name 'willekeurig_getal' is not defined
>>> willekeurig_getal = randint(0,1000)
willekeurig_getal
print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
SyntaxError: multiple statements found while compiling a single statement
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
459
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 459
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-09 12:12:34.606723
>>> datum.strftime('%A %d %B %Y')
'Wednesday 09 September 2020'
>>> import locale
locale.setlocale(locale.LC_TIME, 'nl_NL')
datum.strftime('%A %d %B %Y')
locale.setlocale(locale.LC_TIME, 'it_IT')
datum.strftime('%A %d %B %Y')
SyntaxError: multiple statements found while compiling a single statement
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL ')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    locale.setlocale(locale.LC_TIME, 'nl_NL ')
  File "C:\Users\tiesh\AppData\Local\Programs\Python\Python37\lib\locale.py", line 608, in setlocale
    return _setlocale(category, locale)
locale.Error: unsupported locale setting
>>> 
KeyboardInterrupt
>>> locale.sethome (locale.LC_TIME, 'nl_NL')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    locale.sethome (locale.LC_TIME, 'nl_NL')
AttributeError: module 'locale' has no attribute 'sethome'
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 09 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A &d &B &Y')
'mercoledì &d &B &Y'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 09 settembre 2020'
>>> 