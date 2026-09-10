p = input("what was your start intrest?:")
p = float(p)
r = input("what was your start intrest rate?:")
r = float(r)
total1 = r / 100
t = input("the amount of time?:")
t = float(t)
total2 = p * total1 * t
print("your balance is:",total2)