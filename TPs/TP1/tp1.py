import random
from matplotlib import pyplot as plt

beg = 1
end = 100
mayor_a_menor = True

class coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = ((self.x) ** 2 + (self.y) ** 2 ) ** 1/2 # distance to origin
        self.cuad = max(self.x, self.y) # belonging cuadrant

    def print(self):
        print(f"({self.x}, {self.y})")
    
    def __str__(self):
        return str(f"({self.x}, {self.y})")
    
    def __lt__(self, other):
        if self.cuad == other.cuad: return self.dist < other.dist
        return self.cuad < other.cuad

    def __le__(self, other):
        if self.cuad == other.cuad: return self.dist <= other.dist
        return self.cuad <= other.cuad

    def __gt__(self, other):
        if self.cuad == other.cuad: return self.dist > other.dist
        return self.cuad > other.cuad

    def __ge__(self, other):
        if self.cuad == other.cuad: return self.dist >= other.dist
        return self.cuad >= other.cuad

    def __eq__(self, other):
        return self.x == self.y and other.x == other.y

    def __ne__(self, other):
        return self.x != self.y or other.x != other.y

    def domina(self, other):
        return self.x >= other.x and self.y >= other.y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 1/2

class conj:
    def __init__(self):
        self.conj = []
        self.tam = 0
    
    def push(self, coord):
        self.conj.append(coord)
        self.tam += 1

    def pop(self, k=0):
        if self.tam == 0: return None
        self.tam -= 1
        return self.conj.pop(k)

    def print(self):
        for c in self.conj:
            c.print()
    
    def sort(self):
        self.conj.sort(reverse=mayor_a_menor)

    def get(self, key):
        return self.conj[key]

    def empty(self):
        return self.tam == 0
    
    def closest(self, b):
        choice = None
        pos = -1
        for i in range(self.tam):
            a = self.conj[i]
            if a < b: break
            if not choice or a.distance(b) < choice.distance(b): 
                choice = a
                pos = i
        if choice: return self.pop(pos)
        return choice

A = conj()
B = conj()

matches = []

for i in range(20):
    a = coord(random.randint(beg, end), random.randint(beg, end))
    b = coord(random.randint(beg, end), random.randint(beg, end))

    A.push(a)
    B.push(b)

    plt.scatter(a.x, a.y, c='green')
    plt.scatter(b.x, b.y, c='blue')
    plt.text(a.x, a.y, f"({a.x},{a.y})")
    plt.text(b.x, b.y, f"({b.x},{b.y})")

A.sort()
B.sort()

print("A sorted: ")
A.print()
print()
print("B sorted: ")
B.print()

while not B.empty():
    b = B.pop()
    a = A.closest(b)
    if not a: continue
    matches.append((a, b))

print()
print("matches:")
for (a,b) in matches:
    print(f"{str(a)} - {str(b)}")
    plt.plot([a.x, b.x], [a.y, b.y], c='red')

plt.xlim(0, 100)
plt.ylim(0, 100)

plt.grid(which='major', axis='both', linestyle='-')

# plt.show()

plt.savefig("out3.png", bbox_inches='tight')