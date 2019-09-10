tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
def printTable(tableData):
    #Find the longest string in each list of tableData
    colWidths = [0] * len(tableData)

    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if colWidths[i] < len(tableData[i][j]):
                colWidths[i] = len(tableData[i][j])

    print (colWidths)

    columns = len(tableData)
    #safe to assume all lists the same length
    rows = len(tableData[0])
    frmt_string = ''
    
    for i in range(rows):
        for j in range(columns):
            frmt_string += tableData[j][i].rjust(colWidths[j]) + ' '
        print(frmt_string)
        frmt_string = ''
        

printTable(tableData)
