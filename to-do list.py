import tkinter
from tkinter import *
root=Tk()
root.title("To-Do-List")
root.geometry("400x600+400+100")
root.resizable(False,False)
task_list=[]
def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)
def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt",'r') as taskfile:
            tasks=taskfile.readlines()
        for task in tasks:
            if task!='\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file=open("tasklist.txt",'w')
        file.close()

heading=Label(root,text="ALL TASKS",width=400,font=("arial",20,"bold"),fg="white",bg="dark blue")
heading.place(x=0,y=0)
frame=Frame(root,width=400,height=50,bg="dark blue")
frame.place(x=0,y=180)
task=StringVar()
task_entry=Entry(frame,width=18,font=("arial",20),bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()
button=Button(frame,text="ADD",font=("arial",20,"bold"),width=6,bg="blue",fg="white",bd=0,command=addTask)
button.place(x=300,y=0)
frame1=Frame(root,bd=3,width=700,height=280,bg="dark blue")
frame1.place(x=0,y=230)
listbox=Listbox(frame1,font=("arial",12),width=40,height=16,bg="dark blue",fg="white",cursor="hand2",selectbackground="blue")
listbox.pack(side=LEFT,fill=BOTH,padx=2)

Button1=Button(root,text="Delete",font=("arial",20),fg="red",bg="white",command=deleteTask)
Button1.pack(side=BOTTOM)
root.mainloop()
