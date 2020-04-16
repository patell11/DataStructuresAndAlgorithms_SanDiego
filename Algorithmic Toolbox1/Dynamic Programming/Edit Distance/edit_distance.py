# python3
import sys


# A Naive recursive Python program to fin minimum number
# operations to convert str1 to str2
def editDistance_rec(str1, str2, m, n):
    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m == 0:
        return n

        # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return m

        # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m - 1] == str2[n - 1]:
        return editDistance(str1, str2, m - 1, n - 1)

        # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(editDistance(str1, str2, m, n - 1),  # Insert
                   editDistance(str1, str2, m - 1, n),  # Remove
                   editDistance(str1, str2, m - 1, n - 1)  # Replace
                   )


# Driver program to test the above function
str1 = "sunday"
str2 = "saturday"
print
editDistance(str1, str2, len(str1), len(str2))



def edit_distance(first_string, second_string):


    if first_string == second_string:
        return 0

    rows = len(second_string) + 1
    columns = len(first_string) + 1

    # Create a matrix of size rows and columns
    distance_matrix = [[ sys.maxsize for column in range(columns)] for row in range(rows)]

    # Insert the first row with the value same as the column index
    for column in range(columns):
        distance_matrix[0][column] = column

    # Insert the first column with the value same as the row index
    for row in range(rows):
        distance_matrix[row][0] = row

    '''Fill the matrix - if the characters are same for a given row and column value insert the value from the diagonal 
        position above. Else find the minimum of the value just left, diagonal and right to the given position.
        Return the value of the last indices for the rows and columns
    '''
    for row in range(1,rows):
        for column in range(1,columns):
            if first_string[column-1] == second_string[row-1]:
                distance_matrix[row][column] = distance_matrix[row-1][column-1]
            else:
                distance_matrix[row][column] = min(distance_matrix[row][column-1], distance_matrix[row-1][column-1],
                                                   distance_matrix[row-1][column]) +1
    # print(distance_matrix[rows-1][columns-1])
    # print(rows, columns)
    return  distance_matrix[rows-1][columns-1]

#print(edit_distance('editing','distance'))

if __name__ == "__main__":
    print(edit_distance(input(), input()))
