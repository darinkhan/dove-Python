import sys

inp = sys.stdin.readline() #Reads input x = matrix("name", a, b)
s = inp.split(' ')
v1 = s[0]
name = s[2].split('"')[1]
row = s[3][:-1]
col = s[4][:-1]

d = {v1:1}
boo = False

orig_stdout = sys.stdout
f = open('instr.asm', 'w')
sys.stdout = f

i = 1
print("def ${} [1:{}] [1:{}]\n".format(i, row, col))
print("dataset {}\n".format(name))
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
    
        print("def ${} [1:{}] [1:{}]\n".format(i, row, col))
        print("{} ${} ${}\n".format(s[3], d[s[2]], d[s[4]])) #Should throw an error if var doesn't exist in dictionary
        print("end ${}\n".format(i))
        
    i += 1
            
sys.stdout = orig_stdout
f.close()
