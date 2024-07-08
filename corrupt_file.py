try:
    f = open(r"C:\Users\Learner_9ZH3Z104\Development\test_file.txt")
    var = bad_var
    #if f.name == 'currupt_file.txt':
        #raise Exception
   

except FileNotFoundError as e:
    print(e)
    
else:
    print(f.read())
    f.close()
finally:
    print("Excecuting Finally...")    
except FileNotFoundError:
    print('sorry file does not exist')

except Exception as e:
    print(e) 
