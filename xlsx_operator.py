from shutil import copy
import os
from time import time
from exchanger import write_matrix

cwd = os.getcwd()
time_handle = int(time())

print('current work dir: %s'%(cwd))
print('current time handle %s'%(time_handle))

os.mkdir(str(time_handle))

inner_cwd = os.path.join(str(time_handle))
empty_xlsx_f = 'blank.xlsx'

copy(empty_xlsx_f,inner_cwd)

os.chdir(str(time_handle))
cwd = os.getcwd()
print('swich to work dir: %s'%(cwd))

#formula(x-y) call:

def private_formula(x):
    y = x**3 -2*x #sample formula
    return y

#build cache:

def get_list(list_len,init_x,step):
    x_list = []
    y_list = []

    x_in_loop = init_x
    for i in range(list_len):
        y_in_loop = private_formula(x_in_loop)
        x_list.append(x_in_loop)
        y_list.append(y_in_loop)

        x_in_loop += step
    return [x_list,y_list]

#main
print('\033c')
print('''
Formula to Excel generator
         ____
        /\___\.
       / / __ \ 
      / / /_ \/ _    __  __   __
   _ / / __/  /\_\   \_\/\_\  \_\.
   \_\/ /     \/ /   /\ \/ /  /\ \.
    \__/       \_\   \/_/\_\  \/_/
Nick Computer [C] 2018-2023 
''')

init_x = -2

step = 0.1

list_len = int((abs(init_x)*2)/step); #default of list len is 10

obj = get_list(list_len,init_x,step)

write_matrix(empty_xlsx_f, obj, 'export.xlsx')

input('enter to exit')

exit()