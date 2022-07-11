from sys import stdin

mem = {}

for line in stdin:
    
    ops = line.split()

    if ops[0] == 'def':
        mem[ops[1]] = int(ops[2])

    elif ops[0] == 'calc':
        symbols = ops[1:]
        value = 0
        equation = ""

        for s in symbols:
            if s == '=':
                continue
            if s == '+' or s == '-':
                equation += " "+ s +" "
            else:
                if s not in mem:
                    print(' '.join(ops[1:]), 'unknown')
                    break
                equation += str(mem[s])
        else:
            value = eval(equation)

            for k, v in mem.items():
                if v == value:
                    print(' '.join(ops[1:]), k)
                    break
            else:
                print(' '.join(ops[1:]), 'unknown')
        
    elif ops[0] == 'clear':
        mem = {}