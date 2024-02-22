import random as r


def gen_2d_array(rows,cols):
    row = []
    for i in range (rows):
        col = []
        for j in range (cols):
            col.append(0)
        row.append(col)
    return row

def get_col(row,col,max_row,max_col):
    if(row == 0 or col == 0 or row == max_row or col == max_col):
        return (255,255,255)
    return (0,0,0)

def gen_map(rows,cols):
    map_data = gen_2d_array(rows,cols)
    for row in range (rows):
        for col in range (cols):
            map_data[row][col] = get_col(row,col,rows-2,cols-2)
    return map_data       
    