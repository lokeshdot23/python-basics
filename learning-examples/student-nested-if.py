'''
if a student is in class or not
first clg
2nd diff blocks
3rd floor
4 in class

while True:
    clg = input("did you see him/her in clg (y/n)")
    if clg == 'y':
        block = input("did you see him/her in block (y/n)")
        if block =='y':
            floor = input("did you see him/her in floor (y/n)")
            if floor =='y':
                class_room = input("did you see him/her in class (y/n)")
                if class_room == 'y':
                    print('he is present in the class')
                else:
                    print("in floor")
            else:
                print("in block")
        else:
            print("in collage")
    else:
        print("absent")

#movie tickets
#rain

tickets = input('entre if tickets are there (y/n)')
rain = input('entre if raining (y/n)')
if (tickets == 'n' and rain == 'y') :
    print("no movie today")
elif (tickets == 'n' and rain == 'n') :
    print('no movie today')
elif tickets == 'y' and rain == 'n':
    print("yeaah movie")
elif tickets =='y' and rain == 'y':
    print("no movie today")
'''
