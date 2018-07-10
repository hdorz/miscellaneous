import numpy
from scipy.linalg import solve

import xlrd

'''
This program takes an excel spreadsheet containing a scatter plot and 
implements matrices to determine the "line (or polynomial) of best fit."
'''

class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.matrix = []

        self.create_matrix()

    def __getitem__(self, xy):
        assert type(xy) is tuple, "Given coordinates are not more than one (>1)."
        return self.matrix[xy[0]][xy[1]]

    def __setitem__(self, xy, value):
        assert type(xy) is tuple, "Given coordinates are not more than one tuple (>1)."
        assert (type(value) is int) or (type(value) is float), "Value is not a number."
        self.matrix[xy[0]][xy[1]] = value

    def __str__(self):
        retVal = ""
        for thing in self.matrix:
            retVal += str(thing) + "\n"
        return retVal

    def create_matrix(self):
        for i in range(0, self.row):
            self.matrix.append([0]*self.column)

    def read_string(self, string_of_entries): # column entries in row separated by "," - rows separated by "/"
        readable = string_of_entries.split("/")
        for row in range(0, len(readable)):
            readable[row] = readable[row].split(",")

        for i in range(0, self.row):
            for j in range(0, self.column):
                try:
                    self[i, j] = int(readable[i][j])
                except ValueError:
                    self.matrix[i][j] = "error"

def matrix_multiplication(matrixA, matrixB):
    assert (type(matrixA) is Matrix), "MatrixA is not class Matrix."
    assert (type(matrixB) is Matrix), "MatrixB is not class Matrix."
    if matrixA.column == matrixB.row:
        welldefined_element = matrixA.column # or matrixB.row
        new_matrix = Matrix(matrixA.row, matrixB.column)
        for i in range(0, new_matrix.row):
            for j in range(0, new_matrix.column):
                for k in range(0, welldefined_element):
                    try:
                        new_matrix[i, j] += int(matrixA[i, k])*int(matrixB[k, j])
                    except ValueError:
                        new_matrix.matrix[i][j] = "error"
        return new_matrix
    else:
        return "Product is not well-defined."

def transpose(matrix):
    assert (type(matrix) is Matrix), "Entered matrix is not class Matrix."
    transpose_matrix = Matrix(matrix.column, matrix.row)
    for i in range(0, matrix.row):
        for j in range(0, matrix.column):
            transpose_matrix[j, i] = matrix[i, j]
    return transpose_matrix

def normal_system(M, y):
    assert (type(M) is Matrix), "Entered matrix (M) is not class Matrix."
    assert (type(y) is Matrix), "Entered matrix (y) is not class Matrix."
    M_transpose = transpose(M)
    MTM = matrix_multiplication(M_transpose, M)
    MTy = matrix_multiplication(M_transpose, y)

    MTM_numpy = numpy.matrix(MTM.matrix)
    MTy_numpy = numpy.matrix(MTy.matrix)
    v_matrix = solve(MTM_numpy, MTy_numpy)

    return v_matrix

def testing():
    test = Matrix(3, 3)
    print(test[0, 0])
    test[0, 0] = -34
    print(test[0, 0])
    print(test)
    test.read_string("1,5,1/-8,4,1/9,1,9000")
    print(test)
    bruh = transpose(test)
    print("============")
    print(bruh)

    a = Matrix(2, 2)
    a.read_string("1,2/3,1")
    print(a)
    b = Matrix(2, 2)
    b.read_string("1,2/3,0")
    print(b)

    c = matrix_multiplication(a, b)
    print("============")
    print(c)

    d = matrix_multiplication(b, a)
    print("============")
    print(d)

    print("=========================")

    M = Matrix(4, 2)  # rows depends on how many data points there are, columns for desired polynomial fit
    y = Matrix(M.row, 1)

    M.read_string("1,0/1,1/1,3/1,6")
    print(M)
    y.read_string("2/3/7/12")
    print(y)

    x = normal_system(M, y)

    print(x)
    print(type(x))
    print(x[0, 0])
    print(x[1, 0])

    print("=========================")

    bruh = Matrix(2, 2)
    bruh.read_string("1,2/3,4")
    print(bruh[0, 1])
    bruh[0, 1] = 9000
    print(bruh[0, 1])
    print(bruh)

def main_program():
    while True:
        try:
            excel_name = str(input("Enter excel file name (without .xlsx): ")) + ".xlsx"
            readtemp = xlrd.open_workbook(excel_name)
            break
        except FileNotFoundError:
            print("File not found. Try again.")

    sample = xlrd.open_workbook(excel_name)

    print("===== Data sheets available =====")
    num = 1
    for sheet in sample.sheet_names():
        print(str(num) + ". " + sheet)
        num += 1

    while True:
        try:
            sheet_name = str(input("Enter sheet name: "))
            worksheet = sample.sheet_by_name(sheet_name)
            break
        except xlrd.biffh.XLRDError:
            print("Try again. No such sheet name exists. (xlrd.biffh.XLRDError)")

    count = 0
    try:
        while True:
            worksheet.cell(count, 0).value
            count += 1
    except IndexError:
        pass

    while True:
        try:
            polynomial = int(input("What degree polynomial should be used for data fitting? (1, 2 or 3): "))
            deg = 2
            if (polynomial >= 1) and (polynomial <= 3):
                M = Matrix(count, polynomial+1)
                y = Matrix(count, 1)

                for i in range(0, count):
                    M[i, 0] = 1
                    M[i, 1] = worksheet.cell(i, 0).value
                    y[i, 0] = worksheet.cell(i, 1).value

                while deg <= polynomial:
                    for i in range(0, count):
                        M[i, deg] = (M[i, deg-1])**deg
                    deg += 1

                break

            else:
                print("That is an invalid number. Try again.")
        except ValueError:
            print("Input is not valid. Try again.")

    x = normal_system(M, y)

    print()
    # print(M)
    # print(y)
    # print(x)

    retVal = "The best fit for polynomial of degree " + str(polynomial) + " is: "

    for i in range(0, polynomial+1):
        if i == 0:
            retVal += str(x[i, 0]) + " + "
        elif i == polynomial:
            retVal += str(x[i, 0]) + "x^" + str(i)
        elif i > 0:
            retVal += str(x[i, 0]) + "x^" + str(i) + " + "

    print(retVal)

if __name__ == "__main__":
    main_program()
    # testing()