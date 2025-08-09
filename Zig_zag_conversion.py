string = "PAYPALISHIRING"
numRows = 3
def convert(s, numRows):
    if numRows == 1:
        print("Single row case")
        return s
    row = [[] for _ in range(numRows)]
    idx = 0 #current row index
    d = 1 #move up or down
    for c in s:
        row[idx].append(c)
        if idx == 0:
            d = 1
        elif idx == numRows - 1:
            d = -1
        idx += d
    for i in range(numRows):
            row[i] = ''.join(row[i])
    return ''.join(row)


print(convert(string, numRows))