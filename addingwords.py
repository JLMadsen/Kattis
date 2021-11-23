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
        # print('MEM', mem)
        for s in symbols:
            # print('S', s)
            if s == '=':
                continue
            if s == '+' or s == '-':
                equation += " "+ s +" "
            else:
                if s not in mem:
                    # print(s, 'not in MEM')
                    print(' '.join(ops[1:]), 'unknown')
                    break
                equation += str(mem[s])
        else:
            # print('A', symbols)
            # print('B', equation)
            value = eval(equation)
            for k, v in mem.items():
                if v == value:
                    print(' '.join(ops[1:]), k)
                    break
            else:
                print(' '.join(ops[1:]), 'unknown')


        # for idx, var in enumerate(ops[1:]):
        #     print(idx, var)
        #     if var in ['calc', '+', '-']:
        #         continue
        #     if var not in mem.keys():
        #         print(' '.join(ops[1:]), 'unknown')
        #         break
        #     value = value + ( mem[var] if ops[idx-1] != '-' else -mem[var] )
        #     print('VALUE', value)
        # else:
        #     for v, k in mem.items():
        #         if v == value:
        #             print(' '.join(ops[1:]), k)
        #             break
        #     else:
        #         print(' '.join(ops[1:]), 'unknown')
        
    elif ops[0] == 'clear':
        mem = {}