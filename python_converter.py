import sys

iden = 0

class Matrix():
    def __init__(self, name, row, col):
        global iden
        self.id = iden
        self.name = name
        self.row = row
        self.col = col
        iden += 1
        
    def get_id(self):
        return self.id
        
    def add(self, other):
        a = Matrix(self.name, self.row, self.col)
        return a
        
    def __repr__(self):
        return "def ${} [1:{}] [1:{}]\n\t\tdataset {}\nend ${}\n".format(self.id, self.row, self.col, self.name, self.id)

        
first = Matrix("testOne", 4, 3)
second = Matrix("testTwo", 4, 3)
third = first.add(second)
print(first)
print(second)
print(third)

"""
inp = sys.stdin.readline() #Reads input x = matrix("name", a, b)
s = inp.split()
v1 = s[0]
name = s[2].split('"')[1]
row = s[3][:-1]
col = s[4][:-1] #need to fix accidental addition of ')' to instr.asm here, maybe .split('\s | ( | ) | , | =')?

d = {v1:1}

orig_stdout = sys.stdout
f = open('instr.asm', 'w')
sys.stdout = f

i = 1
print("def ${} [1:{}] [1:{}]\n".format(i, row, col))
print("\t\tdataset {}\n".format(name))
print("end ${}\n".format(i))
i += 1

for line in sys.stdin:
    if (line in d.keys()):
        print("print ${}\n".format(d[line]))
        
        sys.stdout = orig_stdout
        print("${} [1:{}] [1:{}]\n".format(i, row, col))
        orig_stdout = sys.stdout
        sys.stdout = f
    else:
        s = line.split(' ')
        d[s[0]] = i
        #print(s[2].equals(s[4]))
        #print(s[2])
        #print(s[4])
        print("def ${} [1:{}] [1:{}]\n".format(i, row, col))
        print("\t \t{} ${} ${}\n".format(s[3], d.get(s[2]), d.get(s[3]))) #Should throw an error if var doesn't exist in dictionary
        print("end ${}\n".format(i))
        
    i += 1
            
sys.stdout = orig_stdout
f.close()
"""