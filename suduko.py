'''
Question for suduko
9x9 Soduku
True : If this is valid Sudoku
False :If this is valid Sudoku
1.Verify all rows
2 Verify all columns
3 Verify all 3x3 squares

Author: Nagmani Kumar
Date: 4th Feb 2023

'''
s=[[7,3,5,6,1,4,8,9,2], [8,4,2,9,7,3,5,6,1], [9,6,1,2,8,5,3,7,4], [2,8,6,3,4,9,1,5,7], [4,1,3,8,5,7,9,2,6], [5,7,9,1,2,6,4,3,8], [1,5,7,4,9,2,6,8,3], [6,9,4,7,3,8,2,1,5], [3,2,8,5,6,1,7,4,9]]
# s=[[8,2,7,1,5,4,3,9,6], [9,6,5,3,2,7,1,4,8], [3,4,1,6,8,9,7,5,2], [5,9,3,4,6,8,2,7,1], [4,7,2,5,1,3,6,8,9],[6,1,8,9,7,2,4,3,5], [7,8,6,2,3,5,9,1,4], [1,5,4,7,9,6,8,2,3], [2,3,9,8,4,1,5,6,7]]
def transpose(s):
    """
    Return:copy of table with rows and columns swapped.
    Precondition: table is a (non-ragged) List.
    """
    column_lst = []
    for m in range(len(s[0])):
        row = []
        for n in range(len(s)):
            row.append(s[n][m])
        column_lst.append(row) 
    return column_lst
column_list=transpose(s)
# print(column_list)


result=[]
def square(s):
    """
    Return:table of first 3 element of first,second & third row.
    Precondition: table is a (non-ragged) List.
    """
    #for row 1,2 & 3
    acc1=[]
    acc2=[]
    acc3=[]
    for i in range(9):
        if i<3:
            for j in range(3):
                acc1.append(s[i][j])
        elif i<6:
            for j in range(3):
                acc2.append(s[j][i])
        else:
            for j in range(3):
                acc3.append(s[j][i])
    result.append(acc1)
    result.append(acc2)
    result.append(acc3)

    #for row 4,5 & 6
    acc1=[]
    acc2=[]
    acc3=[]
    for i in range(3,6):
        for j in range(3):
            acc1.append(s[i][j])
    for i in range(3,6):
        for j in range(3,6):
            acc2.append(s[i][j])
    for i in range(3,6):
        for j in range(6,9):
            acc3.append(s[i][j])
    result.append(acc1)
    result.append(acc2)
    result.append(acc3)

    #for row 7,8 & 9
    acc1=[]
    acc2=[]
    acc3=[]
    for i in range(6,9):
        for j in range(3):
            acc1.append(s[i][j])
    for i in range(6,9):
        for j in range(3,6):
            acc2.append(s[i][j])
    for i in range(6,9):
        for j in range(6,9):
            acc3.append(s[i][j])
    result.append(acc1)
    result.append(acc2)
    result.append(acc3)
    return result
square_matrix=square(s)
# print(square_matrix)


def verify_soduko(s):
    for i in s:
        for j in range(1,10):
            if i.count(j)!=1:
                return False
    for i in s:
        for j in range(1,10):
            if i.count(j)!=1:
                return False
    for i in s:
        for j in range(1,10):
            if i.count(j)!=1:
                return False
    else:
        return True
print(verify_soduko(s))


    

















