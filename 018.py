raw_data = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
triangle = [list(map(int, line.split())) for line in raw_data.strip().splitlines()]

# from the current row and column, you can access row + 1 or row + 1 and col + 1

def best(row,col,height):
    if row >= len(triangle) or height <= 0:
        return 0
    
    curr = triangle[row][col]
    # go left, or go right?
    left = best(row + 1, col, height - 1) + curr
    right= best(row + 1, col + 1, height - 1) + curr
    
    return max(left,right)
    
res = best(0,0,len(triangle))
print(res)


    