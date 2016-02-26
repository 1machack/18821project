def get_next_vector(vector):
    n = len(vector)-1
    new_vector = []
    for i in range(n+2):
        row = []
        for j in range(n+2):
            row.append(0)
        new_vector.append(row)
    for y in range(n):
        j = y+1
        for x in range(j):
            i = x+1
            for z in range(j-i):
                new_vector[i][i+1+z] += vector[i][j]
            for z in range(i+1):
                new_vector[z+1][j+1] += vector[i][j]
    return new_vector

def sum_vector(vector):
    s = 0
    for v in vector:
        s += sum(v)
    return s

def prune_vector(vector):
    def shrink_row(row):
        return row[1:]
    shrinked = [shrink_row(row) for row in vector]
    return shrinked[1:]

def print_vector(matri):
    matrix = prune_vector(matri)
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)


vector = [[0,0],[0,1]]
for i in range(10):
    print_vector(vector)
    print '\n'
    print '\n'
    vector = get_next_vector(vector)
print_vector(vector)

    
