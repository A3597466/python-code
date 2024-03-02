#!python
# 定义不同类型的变量
a = "Hello"
b = 10
c = [1, 2, 3]
d = {"name": "Alice", "age": 25}
e = (4.5, 6)
f = True
g = None
h = print("Printing")
i = lambda x: x * 2
j = open("array.py", "r")
k = object()
l = str(10)
m = int(5.7)
n = float(8)
o = bool(True)
p = list([1, 2])
q = tuple((3,))
s = dict({'key': 'value'})
t = set(['apple', 'banana'])
u = frozenset(['cat', 'dog'])
v = complex(2 + 3j)
w = bytes('hello', encoding='utf-8')
x = bytearray(b'world')


# 打印每个变量及其对应的类型
#for var in locals().values():
#    print(var, type(var).__name__)

print("a", a, type(a).__name__)
print("b", b, type(b).__name__)
print("c", c, type(c).__name__)
print("d", d, type(d).__name__)
print("e", e, type(e).__name__)
print("f", f, type(f).__name__)
print("g", g, type(g).__name__)
print("h", h, type(h).__name__)
print("i", i, type(i).__name__)
print("j", j, type(j).__name__)
print("k", k, type(k).__name__)
print("l", l, type(l).__name__)
print("m", m, type(m).__name__)
print("n", n, type(n).__name__)
print("o", o, type(o).__name__)
print("p", p, type(p).__name__)
print("q", q, type(q).__name__)
#print("r", r, type(r).__name__)
print("s", s, type(s).__name__)
print("t", t, type(t).__name__)
print("u", u, type(u).__name__)
print("v", v, type(v).__name__)
print("w", w, type(w).__name__)
print("x", x, type(x).__name__)

