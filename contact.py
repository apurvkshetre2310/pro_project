from tkinter import *
from tkinter import ttk
from  view import*
from tkinter import messagebox
#colors
co0 = "#ffffff"
co1 = "#000000"
co2 = "#4456f0"

Window = Tk()
Window.title("CONTACT BOOK")
Window.geometry("485x450")
Window.configure(background=co0)
Window.resizable(width=False,height=False)


#frames
frame_up = Frame(Window,width=500,height=50,bg="violet")
frame_up.grid(row=0,column=0,padx=0,pady=1)

frame_down = Frame(Window,width=500,height=150,bg="white")
frame_down.grid(row=1,column=0,padx=0,pady=1)

frame_table = Frame(Window,width=500,height=100,bg="black",relief='flat')
frame_table.grid(row=2,column=0,columnspan=2,padx=10,pady=1,sticky=NW)


#functions
def show():
    global tree

    listheader = ['name','telephone','email']
    
    demo_list = view()

    tree = ttk.Treeview(frame_table,selectmode="extended",columns=listheader,show="headings")


    
    vsb = ttk.Scrollbar(frame_table, orient="vertical",command=tree.xview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal",command=tree.xview)


    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0,row=0,sticky='nsew')
    vsb.grid(column=1,row=0,sticky='ns')
    hsb.grid(column=0,row=1,sticky='ew')

    #tree head
    tree.heading(0,text='Name',anchor=NW)
    tree.heading(1,text='telephone', anchor=NW)
    tree.heading(2,text='email', anchor=NW)

    #tree columns
    tree.column(0,width=120, anchor='nw')
    tree.column(1,width=50, anchor='nw')
    tree.column(2,width=100, anchor='nw')

    for item in demo_list:
        tree.insert('','end',values=item)

show()

def insert():
    name = e_name.get()
    telephone= e_telephone.get()
    email = e_email.get()

    data = [name,telephone,email]

    if name == '' or telephone == '' or email == '':
        messagebox.showwarning('data','please fill in all fileds')


    else:
        add(data)
        messagebox.showinfo('data','data added successfully')
        e_name.delete(0,'end')
        e_telephone.delete(0,'end')
        e_email.delete(0,'end')

        show()


def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']


        name = str(tree_list[0])
        telephone = str(tree_list[1])
        email = str(tree_list[2])

        e_name.insert(0,name)
        e_telephone.insert(0,telephone)
        e_email.insert(0,email)


        def confirm():
            new_name = e_name.get()
            new_telephone = e_telephone.get()
            new_email = e_email.get()


            data = [new_telephone,new_name,new_telephone,new_email]
            update(data)

            messagebox.showinfo('success','data updated successfully')


            e_name.delete(0,'end')
            e_telephone.delete(0,'end')
            e_email.delete(0,'end')

            for widget in frame_table.winfo_children():
                widget.destroy()

            b_confirm.destroy()

            show()

    
        b_confirm = Button(frame_down, text="confirm", width=10, height=1, bg='white',fg='blue', font=('Ivy 8 bold'),command=confirm)
        b_confirm.place(x=230,y=110)

    except IndexError:
        messagebox.showerror('error','select one from the table')
        

def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_telephone = str[tree_list[2]]

        remove(tree_telephone)

        messagebox.showinfo('success','data has been deleted successfully')

        for widget in frame_table.winfo_children():
            widget.destroy()

        show()

    except IndexError:
        messagebox.showerror('error','select one of them from the table')

def to_search():
    telephone = e_search.get()


    data = search(telephone)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()


    for item in data:
        tree.insert('','end',values=item)   


    
    
    






        
                        
#frame_up widgets

app_name = Label(frame_up,text="CONTACTBOOK",height=1,font=('verdana 17 bold'),bg="black",fg="white")
app_name.place(x=5,y=5)

#frame_down widgets
l_name =Label(frame_down,text="name*",width=20,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_name.place(x=10,y=20)
e_name = Entry(frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_name.place(x=80,y=20)


l_telephone =Label(frame_down,text="telephone*",width=20,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_telephone.place(x=10,y=80)
e_telephone = Entry(frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_telephone.place(x=80,y=80)


l_email =Label(frame_down,text="Email*",width=20,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_email.place(x=10,y=110)
e_email = Entry(frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_email.place(x=80,y=110)


b_search = Button(frame_down,text="Search", height=1,bg='white',fg ="blue",font=('Ivy 8 bold'),command= to_search)
b_search.place(x=290,y=20)
e_search = Entry(frame_down,width=16,justify='center',font=('Ivy',11),highlightthickness=1,relief="solid")
e_search.place(x=347,y=20)

b_view = Button(frame_down,text="View", height=1, bg='white', fg ="blue",font=('Ivy 8 bold'),command= show)
b_view.place(x=300,y=50)

b_add = Button(frame_down, text="add", width=10, height=1, bg='white',fg='blue', font=('Ivy 8 bold'),command=insert)
b_add.place(x=400,y=50)

b_update = Button(frame_down, text="update", width=10, height=1, bg='white',fg='blue', font=('Ivy 8 bold'),command = to_update)
b_update.place(x=400,y=80)

b_delete = Button(frame_down, text="delete", width=10, height=1, bg='white',fg='blue', font=('Ivy 8 bold'),command = to_remove)
b_delete.place(x=400,y=110)



Window.mainloop()

