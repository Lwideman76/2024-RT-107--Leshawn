
try:
    f = open('test_file.txt')
    var = bad_var
    # if f.name == 'currupt_file.txt':
    #     raise Exception
except FileNotFoundError:
    print('sorry file does not exist')


