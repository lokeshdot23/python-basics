Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"year":2026,"month":5}
a
{'year': 2026, 'month': 5}
type(a)
<class 'dict'>
b={"year","month"}
type(b)
<class 'set'>
a.keys()
dict_keys(['year', 'month'])
a.values()
dict_values([2026, 5])
a.items()
dict_items([('year', 2026), ('month', 5)])
#update
a={"name":"loki","age":24,"mailid":"loki@gmail.com","mobile":8989898989}
a.update({"2nd no":8999899989})
a
{'name': 'loki', 'age': 24, 'mailid': 'loki@gmail.com', 'mobile': 8989898989, '2nd no': 8999899989}
a.update({"month":5},{"year":2026})#gives error args
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.update({"month":5},{"year":2026})#gives error args
TypeError: update expected at most 1 argument, got 2
a.update({"month":5,"year":2016})
a
{'name': 'loki', 'age': 24, 'mailid': 'loki@gmail.com', 'mobile': 8989898989, '2nd no': 8999899989, 'month': 5, 'year': 2016}
a.setdefault("date",2)
2
a
{'name': 'loki', 'age': 24, 'mailid': 'loki@gmail.com', 'mobile': 8989898989, '2nd no': 8999899989, 'month': 5, 'year': 2016, 'date': 2}
a.pop()#typeerror atleast one arg
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.pop()#typeerror atleast one arg
TypeError: pop expected at least 1 argument, got 0
a.pop("year")
2016
a
{'name': 'loki', 'age': 24, 'mailid': 'loki@gmail.com', 'mobile': 8989898989, '2nd no': 8999899989, 'month': 5, 'date': 2}
a.popitem()# no arg required
('date', 2)
a
{'name': 'loki', 'age': 24, 'mailid': 'loki@gmail.com', 'mobile': 8989898989, '2nd no': 8999899989, 'month': 5}
>>> 
>>> #copy
>>> a.copy()
{'name': 'loki', 'age': 24, 'mailid': 'loki@gmail.com', 'mobile': 8989898989, '2nd no': 8999899989, 'month': 5}
>>> a["name"]
'loki'
>>> a.get("age")
24
>>> #get()
>>> a.clear()
>>> a
{}
>>> a.update({"course":"python"})
>>> a
{'course': 'python'}
>>> a={"name":"loki","city":"vja","name":"loki",}
>>> a
{'name': 'loki', 'city': 'vja'}
>>> #no duplicates
>>> a={"name":"loki","city":"vja","name":"lokesh",}#updates name to ,lokesh and ignores ist name and do not allow duplicates
>>> a
{'name': 'lokesh', 'city': 'vja'}
>>> a={"name1":"loki","city":"vja","name2":"loki",}
>>> a
{'name1': 'loki', 'city': 'vja', 'name2': 'loki'}
>>> #no of valuses in single key
>>> details={"idnos":[10,20,30],"names":["lokesh","pranu","chinnari"],"marks
...          
SyntaxError: unterminated string literal (detected at line 1)
>>> details={"idnos":[10,20,30],"names":["lokesh","pranu","chinnari"],"marks":[70,80,90]}
...          
>>> details
...          
{'idnos': [10, 20, 30], 'names': ['lokesh', 'pranu', 'chinnari'], 'marks': [70, 80, 90]}
>>> details.keys()
...          
dict_keys(['idnos', 'names', 'marks'])
>>> details.values()
...          
dict_values([[10, 20, 30], ['lokesh', 'pranu', 'chinnari'], [70, 80, 90]])
>>> details.items()
...          
dict_items([('idnos', [10, 20, 30]), ('names', ['lokesh', 'pranu', 'chinnari']), ('marks', [70, 80, 90])])
>>> details.copy()
...          
{'idnos': [10, 20, 30], 'names': ['lokesh', 'pranu', 'chinnari'], 'marks': [70, 80, 90]}
