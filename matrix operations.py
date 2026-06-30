import numpy as np

# Function to input a matrix
def input_matrix(name):
    rows = int(input(f"\nEnter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))

    print(f"\nEnter elements of Matrix {name} row by row:")

    matrix = []

    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    return np.array(matrix)

# Menu
while True:

    print("\n==============================")
    print("     MATRIX OPERATIONS TOOL")
    print("==============================")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Matrix Transpose")
    print("5. Matrix Determinant")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        A = input_matrix("A")
        B = input_matrix("B")

        if A.shape == B.shape:
            print("\nMatrix A:")
            print(A)

            print("\nMatrix B:")
            print(B)

            print("\nAddition Result:")
            print(A + B)

        else:
            print("\nError: Matrices must have same dimensions.")

    elif choice == 2:

        A = input_matrix("A")
        B = input_matrix("B")

        if A.shape == B.shape:
            print("\nSubtraction Result:")
            print(A - B)
        else:
            print("\nError: Matrices must have same dimensions.")

    elif choice == 3:

        A = input_matrix("A")
        B = input_matrix("B")

        if A.shape[1] == B.shape[0]:
            print("\nMultiplication Result:")
            print(np.dot(A, B))
        else:
            print("\nError: Number of columns of A must equal rows of B.")

    elif choice == 4:

        A = input_matrix("A")

        print("\nOriginal Matrix:")
        print(A)

        print("\nTranspose:")
        print(A.T)

    elif choice == 5:

        A = input_matrix("A")

        if A.shape[0] == A.shape[1]:
            print("\nMatrix:")
            print(A)

            print("\nDeterminant:")
            print(np.linalg.det(A))
        else:
            print("\nError: Determinant exists only for square matrices.")

    elif choice == 6:

        print("\nThank you for using Matrix Operations Tool!")
        break

    else:
        print("\nInvalid Choice.")