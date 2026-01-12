def add_prefix(items,prefix):
    result = []
    for item in items:
        result.append(f"{prefix} {item}")
    return result

names = ['john', 'smith', 'karl']

new_names = add_prefix(names, 'Mr')
print(new_names)  # ['Mr john', 'Mr smith', 'Mr karl']

print(names)      # ['john', 'smith', 'karl'] (исходный список не изменён)

# Другие примеры:
print(add_prefix(['apple', 'banana'], 'fruit'))  # ['fruit apple', 'fruit banana']
print(add_prefix([], 'Mr'))                      # [] (пустой список)
print(add_prefix(['word'], 'prefix'))   