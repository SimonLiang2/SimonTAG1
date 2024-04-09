import random as r

def gen_2d_array(rows,cols):
    row = []
    for i in range (rows):
        col = []
        for j in range (cols):
            col.append(0)
        row.append(col)
    return row

def get_bin(bin_thresh=0.1):
    num = r.random()
    if num >= bin_thresh: num = 0
    else: num = 1
    return num

def get_col(row,col,max_row,max_col):
    if(row == 0 or col == 0 or row == max_row or col == max_col):
        return 1
    return get_bin()

def find_spawn_point(map_data, res, square_region=3):
    max_rows = len(map_data)
    max_cols = len(map_data[0])
    while True:
        row = r.randint(1, max_rows - square_region)
        col = r.randint(1, max_cols - square_region)
        valid_spawn = True
        for i in range(row, row + square_region):
            for j in range(col, col + square_region):
                if map_data[i][j] != 0:
                    valid_spawn = False
                    break
            if not valid_spawn:
                break 
        if valid_spawn:
            return (col + 1) * res, (row + 1) * res



def gen_map(res,width,height):
    rows = int(height/res)
    cols = int(width/res)
    map_data = gen_2d_array(rows,cols)
    for row in range (rows):
        for col in range (cols):
            map_data[row][col] = get_col(row,col,rows-1,cols-1)
    return map_data       
    