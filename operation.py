import sympy as sp
import copy

def add (a,b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return("addition is not possible")
    else:
        A = copy.deepcopy(a)
        for i in range(len(a)):
            for j in range(len(a[0])):
                A[i][j] += b[i][j]
        return A

def sub (a,b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return("subtraction is not possible")
    else:
        A = copy.deepcopy(a)
        for i in range(len(a)):
            for j in range(len(a[0])):
                A[i][j] -= b[i][j]
        return A

def mul (a,b):
    g = []
    if len(a[0]) != len(b):
        return("multiplication is not possible")
    else:
        for i in range(len(a)):
            row = []
            for j in range(len(b[0])):
                row.append(0)
            g.append(row)

        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(a[0])):
                    g[i][j] += a[i][k] * b[k][j]
        return g

def det (a):
    if len(a) != len(a[0]):
        return("row and column should be equal")
    else:
        if len(a) == 1:
            return a[0][0]
        elif len(a) == 2:
            return a[0][0] * a[1][1] - a[0][1] * a[1][0]
        else:
            determinant = 0 
            for i in range(len(a)):
                sub_matrix = []
                for j in range(1, len(a)):
                    row = []
                    for k in range(len(a)):
                        if k != i:
                            row.append(a[j][k])
                    sub_matrix.append(row)
                determinant += ((-1) ** i) * a[0][i] * det(sub_matrix)
            return determinant

def transpose (a):
    g = []
    for i in range(len(a[0])):
        row = []
        for j in range(len(a)):
            row.append(a[j][i])
        g.append(row)
    return g

def eiganvector (a):
    
    a_lambda = copy.deepcopy(a)
    lam = sp.symbols('lambda')
    identity = [[0 for j in range(len(a))] for i in range(len(a))]
    for i in range(len(a)):
        identity[i][i] = lam

    for i in range(len(a)):
        for j in range(len(a)):
            a_lambda[i][j] -= identity[i][j]
            
    determinant = det(a_lambda)
    eiganvalues = sp.solve(determinant, lam)
    # for i in eiganvalues:
       

def rank(a):
    
    cpy = copy.deepcopy(a)
    rank = 0
    row = 0

    for col in range(len(cpy[0])):
        if row >= len(cpy):
            break

        pivot_row = -1
        for r in range(row, len(cpy)):
            if cpy[r][col] != 0:
                pivot_row = r
                break

        if pivot_row == -1:
            continue

        cpy[row], cpy[pivot_row] = cpy[pivot_row], cpy[row]

        pivot_val = cpy[row][col]
        for r in range(row + 1, len(cpy)):
            if cpy[r][col] != 0:
                factor = cpy[r][col] / pivot_val
                for c in range(len(cpy[0])):
                    cpy[r][c] = cpy[r][c] - factor * cpy[row][c]

        row += 1
        rank += 1

    return rank

def inverse(a):
    if len(a) != len(a[0]):
        return("row and column should be equal")
    else:
        determinant = det(a)
        if determinant == 0:
            return("inverse is not possible")
        else:
            identitiy = [[0 for j in range(len(a))] for i in range(len(a))]
            for i in range(len(a)):
                identitiy[i][i] = 1
            cpy= copy.deepcopy(a)
            row = 0
            
            for col in range(len(cpy[0])):
                if row >= len(cpy):
                    break
        
                pivot_row = -1
                for r in range(row, len(cpy)):
                    if cpy[r][col] != 0:
                        pivot_row = r
                        break
            
                if pivot_row == -1:
                    continue
            
                cpy[row], cpy[pivot_row] = cpy[pivot_row], cpy[row]
                identitiy[row],identitiy[pivot_row] = identitiy[pivot_row],identitiy[row]

                pivot_val = cpy[row][col]
                for c in range(len(cpy)):
                    cpy[row][c] = cpy[row][c] / pivot_val
                    identitiy[row][c] = identitiy[row][c] / pivot_val
                for r in range(row + 1, len(cpy)):
                            if cpy[r][col] != 0:
                                factor = cpy[r][col] / pivot_val
                                for c in range(len(cpy[0])):
                                    cpy[r][c] = cpy[r][c] - factor * cpy[row][c]
                                    identitiy[r][c] = identitiy[r][c] - factor * identitiy[row][c]
                row += 1        
            for col in range(len(cpy) - 1, -1, -1):
                pivot_row = col  
                for r in range(pivot_row - 1, -1, -1):
                    if cpy[r][col] != 0:
                        factor = cpy[r][col]
                        for c in range(len(cpy)):
                            cpy[r][c] = cpy[r][c] - factor * cpy[pivot_row][c]
                            identitiy[r][c] = identitiy[r][c] - factor * identitiy[pivot_row][c]
            return identitiy
        
def print_matrix(a):
    for row in a:
        print(row)

B = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]
print_matrix(inverse(B)) 




        