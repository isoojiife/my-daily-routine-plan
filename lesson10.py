#activity1
a = 5
b = 5
c = 5.0
print(a == b)
print(a is b)
print(a == c)
print(a is c)

#activity2
a = 10
b = -10
print(a >> 1)
print(b << 1)

#activity3
s1 = int(input("Enter ur marks:"))
s2 = int(input("Enter ur marks:"))
s3 = int(input("Enter ur marks:"))
s4 = int(input("Enter ur marks:"))
s5 = int(input("Enter ur marks:"))
avg = (s1 + s2 + s3 + s4 + s5) / 5
if avg >= 91 and avg <= 100:
    print("A")
elif avg >= 81 and avg <= 90:
    print("B")