string = input()
def check_smile(pos):
    if string[pos+1] == ")":
        return True
    if string[pos+1] == "-" and string[pos+2] == ")":
        return True
    return False
    
for idx, char in enumerate(string):
    if char == ";" or char == ":":
        try:
            if check_smile(idx):
                print(idx)
        except:
            pass