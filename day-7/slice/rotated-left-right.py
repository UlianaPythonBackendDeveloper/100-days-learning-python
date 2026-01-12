def rotated_left(sequence):
    return sequence[1:] + sequence[:1]

def rotated_right(sequence):
    return sequence[-1:] + sequence[:-1]