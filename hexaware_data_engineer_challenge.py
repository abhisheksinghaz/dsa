
# challenge link: https://www.techgig.com/challenge/hexaware-datascience

# Input:
# 8
# OOOO OOOM
# OVOO OOOO
# OOVO OOVO
# OOOO OOOO
# OOOO OOOO
# OOOO OOOO
# OOOO OOOO
# OOOO VOOO


# following program passed for 3/10 testcases
import sys
rows_count = int(input())
rows = sys.stdin.read().splitlines()
for _ in range(rows_count):
    rows[_] = rows[_].replace(" ","")

# for char in rows[1]:
#     if 'V' == char:
#         print(char)    
#print(rows[0])

col_count = len(rows[0])

def search_m(rows, rows_count, col_count):
    for row in range(rows_count):
        for col in range(col_count):
            if 'M' == rows[row][col]:
                return (row, col)

m_index = list(search_m(rows, rows_count, col_count))
# print(m_index)
# print(type(m_index))

def search_v(rows, rows_count, col_count):
    #v_set = set()
    for row in range(rows_count):
        for col in range(col_count):
            if 'V' == rows[row][col]:
                yield (row, col)
    
v_list = (search_v(rows, rows_count, col_count))
# print(v_list)

flag = 0
dist = -1

for ele in v_list:
    #print(ele[1])
    #print(dist)
    if flag == 0:
        dist = abs(ele[0] - m_index[0]) + abs(ele[1] - m_index[1])
        flag = 1
    if ( abs(ele[0] - m_index[0]) + abs(ele[1] - m_index[1]) ) < dist:
        dist = abs(ele[0] - m_index[0]) + abs(ele[1] - m_index[1]) - 1
        #print(ele,m_index,dist)

print(dist)
