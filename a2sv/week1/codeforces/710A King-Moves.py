val = input()
if val in ["a1", "a8", "h8", "h1"]:
    print(3)
elif val[0] in["a", "h"] or val[1] in ["1" , "8"]:
    print(5)
else:
    print(8)