def sort_pair(pair):
    return(min(pair),max(pair))

print(sort_pair((5, 1)))  # (1, 5)
print(sort_pair((2, 2)))  # (2, 2)
print(sort_pair((7, 8)))  # (7, 8)
print(sort_pair((10, 3))) # (3, 10)
print(sort_pair((0, -1)))