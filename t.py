letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
path = ['2', '22', '222', '3', '33', '333', '4', '44', '444', '5', '55', '555', '6', '66', '666', '7', '77', '777', '7777', '8', '88', '888', '9', '99', '999', '9999']
for n in range(int(input())):
    case = "case #"+ str(n+1) +": "
    text = input()
    for char in text:
        if char == ' ':
            new = "0"
        else:
            new = path[letter.index(char)]
        if new[0] == case[len(case)-1]:
            case += " "
        case += new
    print(case)
