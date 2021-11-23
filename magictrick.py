string = input()
print( (len(set([c for c in string])) is len(string)) * 1 )