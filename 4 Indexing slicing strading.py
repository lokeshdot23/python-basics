Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[4]
'y'
a[7]
'a'
a[0]
'v'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
a[1]+a[10]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a[1]+a[10]
IndexError: string index out of range
a="1 am in class"
a[1]
' '
a[0]
'1'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[1]+a[4]+a[7]
'   '
b="i love python"
b[-1]
'n'
b[0]
'i'
b[2]+b[3]+b[4]+b[5]
'love'
b[7]+b[8]+b[9]+b[10]+b[11]+b[12]
'python'
b[-6]
'p'
b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'python'
b[-8]+b[-9]+b[-10]+b[-11]
'evol'
b[-11]+b[-10]+b[-9]+b[-8]
'love'
b[-13]
'i'
b[-7]+b[-12]
'  '
c="vijayawada is a royal city"
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]
'1 am in c'
a=c
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]
'vijayawad'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]
'vijayawada'
a[-1]
'y'
 a="vizag is a city of destiny"
 
SyntaxError: unexpected indent
a="vizag is a city of destiny"

 

a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'
a="codegnan it solutions"
a[-13]
' '
a[-12]
'i'
a[-10]
' '
a[-9]
's'
a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'solutions'
a[-13]+a[-14]
' n'
a[-12]+a[-11]
'it'
a[-24]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a[-24]
IndexError: string index out of range
a[-20]
'o'
a[-21]
'c'
a[-21]+a[-20]+a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'codegnan'
a="codegnan it solutions"
a="vizag is a city of destiny"
a[-15]+a[-14]+a[-13]+a[-12]
'city'
a[-24]
'z'
a[-26]
'v'
a[-26]+a[-25]+a[-23]+a[-22]+a[-21]
'viag '
#slicing
a="codegnan"
a[0:3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a="work hard until you succeed"
a[:4]
'work'
a[5:9]
'hard'
a[10:15]
'until'
a[17:21]
'ou s'
a[16:20]
'you '
a[16:19]
'you'
a[20:27]
'succeed'
a="i am learning python course"
a[2:4]
'am'
a[6:14]
'earning '
a[5:14]
'learning '
a[15:21]
'ython '
a[14:21]
'python '
a[5:13]
'learning'
a[14:20]
'python'
a[21:27]
'course'
a[5:10]
'learn'
a[-6:]
'course'
a="simple is better than complex"
b="beautiful is better than ugly"
a[-7:]
'complex'
a[-15:-8]
'er than'
a[-12:-8]
'than'
a[-18:-13]
'etter'
a[-19:-13
  ]
'better'
a[-22:-20]
'is'
a[-29:-23]
'simple'
a=b
a[-4:]
'ugly'
a[-9:-5]
'than'
a[-16:-10]
'better'
a[-19:-17]
'is'
a[:-21]
'beautifu'
>>> a[:-22]
'beautif'
>>> a[:-20]
'beautiful'
>>> #striding
>>> a="cloud computing"
>>> a[::5]
'c u'
>>> a[:6]
'cloud '
>>> a[8:]
'mputing'
>>> a[3:11]
'ud compu'
>>> a[::2]
'codcmuig'
>>> a[::7]
'cog'
>>> a[::1]
'cloud computing'
>>> a[5:12]
' comput'
>>> a="python course"
>>> a[-1:-9:-3]
'eu '
>>> a[-2:-12:-4]
'sch'
>>> a[-4:-13:-6]
'uh'
>>> a[-3:-9:-2]
'ro '
>>> a[7:4:2]
''
>>> a[-6:-5:-2]
''
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
