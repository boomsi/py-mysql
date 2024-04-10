# from dataclasses import dataclass

# @dataclass
# class A:
#     name: str
#     age: int

# a = A('abc', 1)
# print(a.name)


# class B:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
    
# r = B('abcdef')
# for k in r:
#     print(k)


class A:
    a = 1
    pass

import os
print(os.getcwd())
# print(dir(A))

import shutil
# shutil.copy('test.py', 'test2.py')

import glob
# print(glob.glob('*.py'))

import sys
print(sys.argv)
# sys.exit()
sys.stderr.write('error\n')

import re 
print(re.findall(r'a', 'abac'))

from datetime import date
now = date.today()
print(now)
f = now.strftime('%Y-%m-%d %H:%m:%s')
print(f)

# from urllib.request import urlopen
# with urlopen('http://localhost:5001') as resp:
#     for line in resp:
#         line = line.decode('utf-8')
#         print(line)


import zlib
s =  b'ab def'
print(len(s))
t = zlib.compress(s)
print(len(t))

import reprlib
print(reprlib.repr('abc'*100))
# 'abcabcabcabc...cabcabcabcabc'

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=30)


from string import Template
s = Template('dsa%{d}sa')
class BatchRename(Template):
    delimiter = '%'
ss = BatchRename(s)
print(s.substitute(d='123'))

from dataclasses import dataclass, asdict

@dataclass
class AA:
    name: str
    age: int
    def __init__(self, name, age):
        self.__dict__ = {'name': name, 'age': age}

a = AA('abc', 1)
print(a)

aa = '213'

from werkzeug.security import generate_password_hash

a1 = generate_password_hash('123')
a2 = generate_password_hash('123')

print(a1 == a2)
