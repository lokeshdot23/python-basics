'''
successful=False
for i in range(3):
    print("Attempted"+i*".")
    if successful:
        print("attempt is successful")
        break
    elif not successful:
        print("not successful")
else:
    print('nnn')
'''
def greet():
    return("hello")
print(greet())
