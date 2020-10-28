A= {10,20,30}
B= {30,40,50}

# Functions like intersection_update, diffrence_update will update original set (here set A) with output of intersection or diffrence depending on which set operation is mentioned in update

A.intersection_update(B)

print(A)

# o/p= set([30])

print (A.intersection(B))

#o/p= set([30])

print (A.difference(B))

# o/p = set([10, 20])

# Update works as union operation on both sets and store value in original set

A.update(B)

print (A)

# o/p= set([50, 20, 40, 10, 30])
