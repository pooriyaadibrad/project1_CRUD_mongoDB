from tkinter import *
from tkinter import ttk,messagebox
from repository import *


win=Tk()
win.geometry("800x600")
win.configure(background="#ECDFCC")
win.title("CRUD")


init()

#def
def ChangeButtonStyleIn(e):
    btnRegister.configure(fg='#ECDFCC',bg='#D6C0B3')

def ChangeButtonStyleInSearch(e):
    btnSearch.configure(fg='#ECDFCC', bg='#D6C0B3')

def ChangeButtonStyleOut(e):
    btnRegister.configure(bg="#626F47",fg="#ECDFCC")

def ChangeButtonStyleOutSearch(e):
    btnSearch.configure(bg="#626F47",fg="#ECDFCC")

def onClickRegister():
    person = {'name':txtName.get(), 'family': txtFamily.get(), 'field': txtField.get(), 'age': txtAge.get()}
    register(person)
    allData = ReadData()
    CleanTable()
    CleanForm()
    for data in allData:
        InsertDataToTable(data)
                          
    messagebox.showinfo("ثبت اطلاعات", "عملیات موفق") 

def FillTable():
    allData = ReadData()
    for data in allData:
        InsertDataToTable(data)


def CleanForm():
    txtName_var.set("")
    txtFamily_var.set("")
    txtField_var.set("")
    txtAge_var.set("")

def ReadData():
    allData = persons.find()
    return allData

def CleanTable():
    for item in student_tbl.get_children():
        student_tbl.delete(item)

def InsertDataToTable(person):
    student_tbl.insert('', 'end', values=[person['name'], person['family'], person['field'], person['age']])



def on_select(e):
    selected_item=txtField.get()
    print(f"selected:{selected_item}")

def change_header_color():
    style=ttk.Style()
    style.configure("Treeview.Heading",background="#A0D683",foreground="#54473F")
    style.map("Treeview.Heading",background=[('active','#E4E0E1')])


def Search():
    allData = ReadData()
    print(type(allData))
    Finded = []
    str = txtSearch.get()
    for item in allData:
        if item['name'] == str or item['family'] == str or item['age'] == str or item['field'] == str :
            Finded.append(item)
    
    if len(Finded) > 0:    
        CleanTable()
        for item in Finded:
            InsertDataToTable(item)
    else:
        messagebox.showerror("","جستجو بی نتیجه بود")


academic_fields=["computer sience","civil engineering","Industrial Engineering","Physic"
    ,"Rights","Chemistry","Psychiatry","Architecture","Philosophy","Dentistry","Medicine"]
#txt

txtName_var = StringVar()
txtName=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg="white",fg="black", textvariable=txtName_var)
txtName.place(x=100,y=100)

txtFamily_var = StringVar()
txtFamily=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg="white",fg="black", textvariable=txtFamily_var)
txtFamily.place(x=100,y=160)

txtAge_var= StringVar()
txtAge=Entry(win,width=15,bd=5,font=('arial',15,'bold'),bg="white",fg="black", textvariable=txtAge_var)
txtAge.place(x=100,y=220)

txtField_var = StringVar()
txtField=ttk.Combobox(win,values=academic_fields,width=18,font=('arial'), textvariable=txtField_var)
txtField.set("Select Your Academic Field")
txtField.place(x=100,y=280)
txtField.bind("<<ComboboxSelected>>",on_select)
txtField.current(0)

txtSearch_var = StringVar()
txtSearch=Entry(win,width=27,bd=5,font=('arial',15,'bold'),bg="white",fg="black", textvariable=txtSearch_var)
txtSearch.place(x=460,y=400)

#lbl
lblName=Label(win,text="Name",font=('arial',15,'bold'),bg="#ECDFCC",fg="#3B3030")
lblName.place(x=20,y=100)

lblFamily=Label(win,text="Family",font=('arial',15,'bold'),bg="#ECDFCC",fg="#3B3030")
lblFamily.place(x=20,y=160)

lblAge=Label(win,text="Age",font=('arial',15,'bold'),bg="#ECDFCC",fg="#3B3030")
lblAge.place(x=20,y=220)

lblField=Label(win,text="Feild",font=('arial',15,'bold'),bg="#ECDFCC",fg="#3B3030")
lblField.place(x=20,y=280)


#btn
btnRegister=Button(win,text="Register",bg="#626F47",fg="#ECDFCC",font=('arial',10,'bold'),command=onClickRegister)
btnRegister.bind('<Enter>',ChangeButtonStyleIn)
btnRegister.bind('<Leave>',ChangeButtonStyleOut)
btnRegister.place(x=140,y=340)

btnSearch=Button(win,text="Search",bg="#626F47",fg="#ECDFCC",font=('arial',10,'bold'),command=Search)
btnSearch.bind('<Enter>',ChangeButtonStyleInSearch)
btnSearch.bind('<Leave>',ChangeButtonStyleOutSearch)
btnSearch.place(x=380,y=400)

#table
columns=("Name","Family","Age","Field")
student_tbl=ttk.Treeview(win,columns=(columns),show="headings")
style=ttk.Style()
style.configure("Treeview",rowheight=25)
for i in range(len(columns)):
    student_tbl.heading(columns[i],text=columns[i])
    student_tbl.column(columns[i],width=100)
student_tbl.place(x=380,y=100)
change_header_color()


FillTable()

win.mainloop()