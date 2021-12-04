import sys

iden = 1
orig_stdout = sys.stdout
sys.stdout = open('instr.asm', 'w')

class Matrix():    
    def __init__(self, row, col, name = None, modifier = None):
        global iden
        self.id = iden
        self.name = name
        self.row = row
        self.col = col
        self.modifier = modifier
        iden += 1
        if self.name == None:
            print("def ${} [1:{}] [1:{}]\n\t{} ".format(self.id, self.row, self.col, self.modifier), end = '')
        else:
            print("def ${} [1:{}] [1:{}]\n\tdataset {}\nend ${}".format(self.id, self.row, self.col, self.name, self.id))
        
    def createMatrix(self, other, modifier):
        temp = Matrix(self.row, self.col, None, modifier)
        print("${} ${}\nend ${}".format(self.id, other.id, temp.id))
        return temp
    
    def __add__(self, other):
        return Matrix.createMatrix(self, other, '+')
    
    def __sub__(self, other):
        return Matrix.createMatrix(self, other, '-')

    def __truediv__(self, other):
        return Matrix.createMatrix(self, other, '/')
    
    def __mul__(self, other):
        return Matrix.createMatrix(self, other, '*')
    
    def __mod__(self, other):
        return Matrix.createMatrix(self, other, '%')
    
    def __pow__(self, other):
        return Matrix.createMatrix(self, other, '**')        
    
    def __rshift__(self, other):
        return Matrix.createMatrix(self, other, '>>')
    
    def __lshift__(self, other):
        return Matrix.createMatrix(self, other, '<<')        
    
    def __and__(self, other):
        return Matrix.createMatrix(self, other, '&')
    
    def __or__(self, other):
        return Matrix.createMatrix(self, other, '!')        
    
    def __xor__(self, other):
        return Matrix.createMatrix(self, other, '^')
        
    def __repr__(self):
        return "print ${}".format(self.id)


first = Matrix(4, 3, "testOne")
second = Matrix(4, 3, "testTwo")
third = first + second
fourth = first ** second
fifth = first << second
print(first)
print(second)
print(third)
print(second * third)


sys.stdout = orig_stdout

"""
inp = sys.stdin.readline() #Reads input x = matrix("name", a, b)
s = inp.split()
v1 = s[0]
name = s[2].split('"')[1]
row = s[3][:-1]
col = s[4][:-1] #need to fix accidental addition of ')' to instr.asm here, maybe .split('\s | ( | ) | , | =')?

d = {v1:1}

orig_stdout = sys.stdout
sys.stdout = open('instr.asm', 'w')

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