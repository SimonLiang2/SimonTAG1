import random as r

def gen_2d_array(rows,cols):
    row = []
    for i in range (rows):
        col = []
        for j in range (cols):
            col.append(0)
        row.append(col)
    return row

def get_bin(bin_thresh=0.25):
    num = r.random()
    if num >= bin_thresh: num = 0
    else: num = 1
    return num

def get_col(row,col,max_row,max_col):
    if(row == 0 or col == 0 or row == max_row or col == max_col):
        return 1
    return get_bin()

def gen_map(res,width,height):
    rows = int(height/res)
    cols = int(width/res)
    map_data = gen_2d_array(rows,cols)
    for row in range (rows):
        for col in range (cols):
            map_data[row][col] = get_col(row,col,rows-1,cols-1)
    return map_data       
    