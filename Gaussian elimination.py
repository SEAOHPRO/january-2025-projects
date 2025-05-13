import numpy as np
import re

def split_equ(equations):
    equations = [equations.split(",")]
    return equations

def equations_to_matrix(equations):
    # Still in progress!! because equation isn't prepared
    # Split left and right side of the equations
    A = []
    B = []
    for equ in equations:
        lhs, rhs = equ.replace(" ", "").split("=")  
        # Find all coefficients and variables using regex
        terms = re.findall(r'([+-]?\d*\.?\d*)([a-zA-Z]+)', lhs)

        coeffs = []
        variables = []
        for coef, var in terms:
            if coef in ("", "+"):
                coef = 1
            elif coef == "-":
                coef = -1
            else:
                coef = float(coef)
            coeffs.append(coef)
            variables.append(var)

        # Convert right-hand side to float
        rhs_value = float(rhs)
        A.append( coeffs )
        coeffs.append(rhs_value)
        G.append( coeffs )

    G = np.array(A)
    A = G

    return A, G


def find_a_pivot(G):
    # Creating diagonal positions
    diagonal = []
    for i in range(G.shape[0]):
        diagonal.append((i, i))
    return diagonal

def case_zero(G):
    # ✅ This function checks if the top-left pivot is zero,
    # and if so, attempts to swap with a lower row that has a non-zero pivot.
    checker = G[0, 0]
    row = 0
    col = 0
    while row < G.shape[0]:
        if checker != 0:
            return
        else:
            for r in range(row + 1, G.shape[0]):
                if G[r, col] != 0:
                    G[[row, r]] = G[[r, row]]  # Swap rows
                    return
            col += 1
            if col == G.shape[1] - 1:
                return True  # All entries in this column are zero
            checker = G[row, col]

def make_pivots_one(G, diagonal):
    for (row, col) in diagonal:
        if G[row, col] == 0:
            achieved = False
            for r in range(row + 1, G.shape[0]):
                if G[r, col] != 0:
                    G[[row, r]] = G[[r, row]]  # Swap rows
                    achieved = True
                    break
            if not achieved:
                continue

        G[row] = G[row] / G[row, col]
        for zero_r in range(row + 1, G.shape[0]):
            if G[zero_r, col] != 0:
                G[zero_r] = G[zero_r] - (G[row] * G[zero_r, col])

def rref(G, diagonal):
    reversed_diagonal = list(reversed(diagonal))
    for (row, col) in reversed_diagonal:
        for i in range(1, G.shape[0] ):
            x = -i
            target_row = row + x
            if 0 <= target_row:
                G[target_row] = G[target_row] - (G[row] * G[target_row, col])

    # ✅ Print final values from RREF matrix
    print("\n📌 Final values:")
    for i in range(G.shape[0]):
        variable = chr(97 + i)  # a, b, c, ...
        value = G[i, -1]
        print(f"{variable} = {value}")
    
    return G

def gaussian_elim_alg(G):
    
    print("🔷 Welcome to the Gaussian Elimination Solver 🔷")
    print("📌 Starting the elimination steps. Please wait...\n")

    result = case_zero(G)

    if result == True:
        print("❌ No valid pivot found in the matrix.")
        print("⛔️ The system might have no unique solution.\n")
        return G, "No Answer"
    
    diagonal = find_a_pivot(G)
    

    make_pivots_one(G, diagonal)

    x = 0
    for (row, col) in diagonal:
        x += G[row, col]

    if x == G.shape[0]:
        rref(G, diagonal)
        print("\n✅ Matrix has been successfully converted to RREF form!")
        print("🎯 You can now read the final solution from the matrix.\n")
        return G, "True Answer"
    else:
        result = case_zero(G)
        if result == True:
            print("⛔️ The system have 0 unique solution.\n")
            return G, "No Answer" 
        
        print("⛔️ The system have infnite solutions.\n")
        return G, "No Answer"

# ✅ Test with a 3x4 matrix
a = 3  # You can change 'a' to any integer you want

# Generate random integer values for the matrix
# a = np.random.randint(0,10)
# matrix = np.random.randint(0, 10, size=(a, a + 1)).astype(float)
matrix = np.array([[5,2,0], [1,2, 1]])


print("Original Matrix:")
print(matrix)

result_matrix, status = gaussian_elim_alg(matrix)

print("\nFinal Matrix:")
print(result_matrix)
print("\nStatus:", status)