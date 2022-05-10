import random
from tkinter import *
root=Tk()
root.title("Pasword Genarator")
root.geometry("500x600")
label_1=Label(root)
array_3D=[[["1","2","3","4","5","6"],["chenxiaoling","luiweiling","leeyoonji","sakurasuzuki"],["C","A","B","X","W","H"]]]
def NewPassword() :
    randomnum_1=random.randint(0,5)
    randomnum_2=random.randint(0,3)
    randomnum_3=random.randint(0,5)
    letter_1=str(array_3D[0][0][randomnum_1])
    letter_2=array_3D[0][1][randomnum_2]
    letter_3=array_3D[0][2][randomnum_3]
    label_1["text"]="Genarated Password: "+letter_1+letter_2+letter_3
btn=Button(root,text="New Password",command=NewPassword)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)
label_1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()