## all about sets
## sets are unordered collection of unique items. use curley brasises

s = {1 ,3, 4, 4, 5, 6}
print(s)

## why we use sets

l = [1, 5, 5, 6, 5, 2, 2, 5, 8]


#remove duplicate

s2 = set(l)
print(s2)

s3 = list(set(s2))
print(s3)

## add() method

s.add(25)
print(s)

s.remove(25)
print(s)

s.discard(25)
s.discard(6)
print(s)
s4 = s.copy()
print(s4)
s.clear()
print(s)

## you can't store list and dictionaries in sets

for item in s4:
    print(item)
if 2 in s4:
    print("There")
else:
    print("Not there")
s5 = {1, 2, 3, 5, 8, 5}
#union, we use pipe |
s6 = s4|s5
print(s6)

## intersection we use &

print(s4&s5)
