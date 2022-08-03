# ------------------------------------LOVE CALCULATOR---------------------------------

print("-------------Wellcome to Love Calculator----------------------")

inp1 = input("Enter 1st Name\n")
inp2 =input("Enter Your 2nd Name")

name1 = inp1.lower()
name2 = inp2.lower()

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u= name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v= name1.count("v") + name2.count("v")
e= name1.count("e") +name2.count("e")

true = t+r+u+e  #5
love = l+o+v+e #7

ans = str(true) + str(love)  #57
score = int(ans)
if score > 90:
    print("Well relation")
elif score >50:
    print("Excellent relation")
else:
    print("not as good at all")