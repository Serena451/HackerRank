#QUESTION DESCRIPTION

# Sean invented a game involving a 2n x 2n matrix where each cell of the matrix contains an integer. He
# can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum
# of the elements in the n x n submatrix located in the upper-left quadrant of the matrix.

# LET'S SOLVE IT

# The crucial question is: can each element reach any position of the matrix? If the answer were yes, then taking the n x n biggest integers of the matrix would be sufficient.
# But of course, with the given operations this is not possible. Let us check the orbit of the integer in (i,j):

# (i,j) itself;
# reversing the column, (2n-1-i,j);
# reversing the row, (i,2n-1-j);
# reversing both column and row, (2n-1-i,2n-1-j)

# Here is the required function:

def flippingMatrix(matrix):
    summa = 0

    for i in range(n):
        for j in range(n):
            summa += max(matrix[i][j], matrix[2*n-1-i][2*n-1-j], matrix[i][2*n-1-j], matrix[2*n-1-i][j])

    return summa


# NB It can be shown that one can move each of the entries a_i,j along its orbit without moving any other entry.
