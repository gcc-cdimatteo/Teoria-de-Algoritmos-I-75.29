import sys, utils

class coord:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def print(self):
        print(f"({self.x}, {self.y})")
    
    def __str__(self):
        return str(f"({self.x}, {self.y})")
    
    def import_coord(c):
        tuple = c.replace('(','').replace(')','').split(", ")
        return coord(tuple[0], tuple[1])

    def y_distance(self, other):
        return abs(self.y - other.y)

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
        self.conj.sort(reverse = False, key = lambda c: c.x)

    def empty(self):
        return self.tam == 0
    
    def y_closest(self, a):
        choice = None
        pos = -1
        for i in range(self.tam):
            b = self.conj[i]
            if b.x > a.x: break
            if b.y > a.y: continue
            if not choice or b.y_distance(a) < choice.y_distance(a): 
                choice = b
                pos = i
        if choice: return self.pop(pos)
        return choice

class matches:
    def __init__(self):
        self.matches = []

    def match(self, a: coord, b: coord):
        self.matches.append((a, b))
    
    def import_match(self, match):
        tuple = match.split(" -> ")
        a = coord.import_coord(tuple[0])
        b = coord.import_coord(tuple[1])
        self.match(a, b)
    
    def as_list(self):
        res = []
        for match in self.matches:
            a = match[0]
            b = match[1]
            res.append([[a.x, b.x], [a.y, b.y]])
        return res
    
    def print(self):
        print(f"Tamaño del matching: {len(self.matches)}")

        print(f"Matching:")
        print()
        
        print(f"(A -> B)")
        for (a, b) in self.matches:
            print(f"{a} -> {b}")
    
    def print_file(self):
        original_stdout = sys.stdout

        with open(utils.HKEY_FILE_PATH_MATCHES, 'w') as f:
            sys.stdout = f
            self.print()
            sys.stdout = original_stdout        

def import_coords(path, conj):
    for point in open(path, "r"):
        (x, y) = point.rstrip().replace(',', '.').split(' ')
        c = coord(float(x), float(y))
        conj.push(c)

