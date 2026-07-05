#undo redo operations using stack in text file
undostack=[]
redostack=[]
file='data.txt'
while True:
    print("1.write\n2.undo\n3.redo\n4.view\n5.exit")
    ch=int(input("enter choice"))
    if ch==1:
        txt=input("enter text")
        undostack.append(txt)
        redostack.clear()
        with open(file,'w') as f:
            f.write(txt)
    elif ch==2:
        if len(undostack)>1:
            redostack.append(undostack.pop())
            with open(file,'w') as f:
                f.write(undostack[-1])
            print("undo completed")
        else:
            print("nothing to undo")
    elif ch==3:
        if redostack:
            txt=redostack.pop()
            undostack.append(txt)
            with open(file,'w') as f:
                f.write(txt)
            print("redo completed")
        else:
            print("nothing to redo")
    elif ch==4:
        with open (file,'r') as f:
            print("file contents",f.read())
    else :
        print("quitting...")
        break
