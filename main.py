import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="hospital")
if cnx.is_connected():
    print("Connection Established...")
else:
    messagebox.showerror("Error", "Connection can not be established")
    exit(1)
cur = cnx.cursor()

win = Tk()
win.state('zoomed')
win.config(bg='black')

Label(win,text='Psychiatric Discharge System',font='impact 31 bold',bg='brown',fg='white').pack(fill=X)

frame1 = Frame(win,bd=15,relief=RIDGE)
frame1.place(x=0,y=64,width=1600,height=510)

lf1=LabelFrame(frame1,text='Discharge Plan',font='ariel 15 bold',bd=10,bg='pink')
lf1.place(x=10,y=0,width=525,height=480)

Label(lf1,text='Psychiatric_ID',font='ariel 12 bold',bg='pink').place(x=5,y=10)
Label(lf1,text='Date of Closure',font='ariel 12 bold',bg='pink').place(x=5,y=80)
Label(lf1,text='Reason of Closure',font='ariel 12 bold',bg='pink').place(x=5,y=140)
Label(lf1,text='Goals Achieved',font='ariel 12 bold',bg='pink').place(x=5,y=210)
Label(lf1,text='Duration of Stay',font='ariel 12 bold',bg='pink').place(x=5,y=285)
Label(lf1,text='Date of Follow-up',font='ariel 12 bold',bg='pink').place(x=5,y=360)

PsychiatricID = StringVar()
DateOfClosure = StringVar()
ReasonOfClosure = StringVar()
GoalsAchieved = StringVar()
DurationOfStay = StringVar()
DateOfFollowup = StringVar()

e1 = Entry(lf1,bd=4,textvariable=PsychiatricID)
e1.place(x=0,y=40,width=260)

e2 = Entry(lf1,bd=4,textvariable=DateOfClosure)
e2.place(x=0,y=110,width=260)

e3 = Entry(lf1,bd=4,textvariable=ReasonOfClosure)
e3.place(x=0,y=180,width=260)

e4 = Entry(lf1,bd=4,textvariable=GoalsAchieved)
e4.place(x=0,y=250,width=260)

e5 = Entry(lf1,bd=4,textvariable=DurationOfStay)
e5.place(x=0,y=320,width=260)

e6 = Entry(lf1,bd=4,textvariable=DateOfFollowup)
e6.place(x=0,y=400,width=260)

lf2=LabelFrame(frame1,text='Patient Information',font='ariel 15 bold',bg='pink',bd=10)
lf2.place(x=535,y=0,width=515,height=480)

Label(lf2,text='Patient_ID',font='ariel 12 bold',bg='pink').place(x=0,y=10)
Label(lf2,text='Patient_Name',font='ariel 12 bold',bg='pink').place(x=0,y=70)
Label(lf2,text='Patient_Age',font='ariel 12 bold',bg='pink').place(x=0,y=130)
Label(lf2,text='Patient_Gender',font='ariel 12 bold',bg='pink').place(x=0,y=190)
Label(lf2,text='Disease/Abnormality Suffered',font='ariel 12 bold',bg='pink').place(x=0,y=250)
Label(lf2,text='Patient_Behavior',font='ariel 12 bold',bg='pink').place(x=0,y=310)
Label(lf2,text='Outcome',font='ariel 12 bold',bg='pink').place(x=0,y=370)

PatientID = StringVar()
PatientName = StringVar()
PatientAge = StringVar()
PatientGender = StringVar()
DiseaseOrAbnormality = StringVar()
PatientBehaviour = StringVar()
Outcomes = StringVar()

e7 = Entry(lf2,bd=4,textvariable=PatientID)
e7.place(x=0,y=45,width=260)

e8 = Entry(lf2,bd=4,textvariable=PatientName)
e8.place(x=0,y=100,width=260)

e9 = Entry(lf2,bd=4,textvariable=PatientAge)
e9.place(x=0,y=160,width=260)

e10 = Entry(lf2,bd=4,textvariable=PatientGender)
e10.place(x=0,y=220,width=260)

e11 = Entry(lf2,bd=4,textvariable=DiseaseOrAbnormality)
e11.place(x=0,y=280,width=260)

e12 = Entry(lf2,bd=4,textvariable=PatientBehaviour)
e12.place(x=0,y=335,width=260)

e13 = Entry(lf2,bd=4,textvariable=Outcomes)
e13.place(x=0,y=400,width=260)

lf3=LabelFrame(frame1,text='Prescription',font='ariel 15 bold',bd=10,bg='pink')
lf3.place(x=1050,y=0,width=470,height=480)

txt_frame= Text(lf3,font='impack 10 bold',width=40,height=30,bg='purple', foreground='white')
txt_frame.pack(fill=BOTH)

frame2 = Frame(win,bd=15,relief=RIDGE)
frame2.place(x=0,y=575,width=1545,height=170)

def insert_data():
    if e1.get() == "" or e2.get() == "" or e3.get() == "" or e4.get() == "" or e5.get() == "" or e6.get() == "" or e7.get() == "" or e8.get() == "" or e9.get() == "" or e10.get() == "" or e11.get() == "" or e12.get() == "" or e13.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        cur.execute("INSERT INTO patient(name, age, gender, disease, behavior, outcome, psychiatric_id, dateofclosure, reasonofclosure, goalsachieved, durationofstay, dateoffollowup) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PatientName.get(),PatientAge.get(),PatientGender.get(),DiseaseOrAbnormality.get(),PatientBehaviour.get(),Outcomes.get(),PsychiatricID.get(),DateOfClosure.get(),ReasonOfClosure.get(),GoalsAchieved.get(),DurationOfStay.get(),DateOfFollowup.get()))
        cnx.commit()
        messagebox.showinfo("Success", "Data Inserted Successfully")
        display_data()

def update_data():
    if e1.get() == "" or e2.get() == "" or e3.get() == "" or e4.get() == "" or e5.get() == "" or e6.get() == "" or e7.get() == "" or e8.get() == "" or e9.get() == "" or e10.get() == "" or e11.get() == "" or e12.get() == "" or e13.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        cur.execute("UPDATE patient SET name=%s,age=%s,gender=%s,disease=%s,behavior=%s,outcome=%s,psychiatric_id=%s,dateofclosure=%s,reasonofclosure=%s,goalsachieved=%s,durationofstay=%s,dateoffollowup=%s WHERE patient_id=%s",(PatientName.get(),PatientAge.get(),PatientGender.get(),DiseaseOrAbnormality.get(),PatientBehaviour.get(),Outcomes.get(),PsychiatricID.get(),DateOfClosure.get(),ReasonOfClosure.get(),GoalsAchieved.get(),DurationOfStay.get(),DateOfFollowup.get(),PatientID.get()))
        cnx.commit()
        if cur.rowcount > 0:
            messagebox.showinfo("Success", "Data Updated Successfully")
        else:
            messagebox.showwarning("Warning", "No record found")
        display_data()

def delete_data():
    if e7.get() == "":
        messagebox.showerror("Error", "Patient ID is required")
    else:
        cur.execute("DELETE FROM patient WHERE patient_id=%s",(PatientID.get(),))
        cnx.commit()
        if cur.rowcount > 0:
            messagebox.showinfo("Success", "Data Deleted Successfully")
        else:
            messagebox.showwarning("Warning", "No record found")
        display_data()

def display_data():
    cur.execute("SELECT * FROM patient")
    rows = cur.fetchall()
    if len(rows) > 0:
        table.delete(* table.get_children())
        for items in rows:
            table.insert('',END,values=items)
        cnx.commit()

def reset_data():
    PsychiatricID.set('')
    DateOfClosure.set('')
    ReasonOfClosure.set('')
    GoalsAchieved.set('')
    DurationOfStay.set('')
    DateOfFollowup.set('')
    PatientID.set('')
    PatientName.set('')
    PatientAge.set('')
    PatientGender.set('')
    DiseaseOrAbnormality.set('')
    PatientBehaviour.set('')
    Outcomes.set('')

def get_data(event=''):
    cursor_row = table.focus()
    data = table.item(cursor_row)
    row = data['values']
    PatientID.set(row[0])
    PatientName.set(row[1])
    PatientAge.set(row[2])
    PatientGender.set(row[3])
    DiseaseOrAbnormality.set(row[4])
    PatientBehaviour.set(row[5])
    Outcomes.set(row[6])
    PsychiatricID.set(row[7])
    DateOfClosure.set(row[8])
    ReasonOfClosure.set(row[9])
    GoalsAchieved.set(row[10])
    DurationOfStay.set(row[11])
    DateOfFollowup.set(row[12])
    perscription = "Patient ID: "+ str(row[0])+"\n"
    perscription += "Patient Name: "+ str(row[1])+"\n"
    perscription += "Patient Age: "+ str(row[2])+"\n"
    perscription += "Patient Gender: "+ str(row[3])+"\n"
    perscription += "Disease/Abnormality: "+ str(row[4])+"\n"
    perscription += "Patient Behavior: "+ str(row[5])+"\n"
    perscription += "Outcomes: "+ str(row[6])+"\n"
    perscription += "Psychiatric ID: "+ str(row[7])+"\n"
    perscription += "Date of Closure: "+ str(row[8])+"\n"
    perscription += "Reason of Closure: "+ str(row[9])+"\n"
    perscription += "Goals Achieved: "+ str(row[10])+"\n"
    perscription += "Duration of Stay: "+ str(row[11])+"\n"
    perscription += "Date of Followup: "+ str(row[12])+"\n"
    txt_frame.delete('1.0', END)
    txt_frame.insert(END,perscription)

def exit_gui():
    cnx.close()
    win.destroy()

I_btn = Button(win,text='Insert',font='ariel 15 bold',bg='brown',fg='white',bd=6,cursor='hand2',command=insert_data)
I_btn.place(x=0,y=745,width=255)

U_btn = Button(win,text='Update',font='ariel 15 bold',bg='purple',fg='white',bd=6,cursor='hand2',command=update_data)
U_btn.place(x=255,y=745,width=255)

d_btn = Button(win,text='Delete',font='ariel 15 bold',bg='green',fg='white',bd=6,cursor='hand2',command=delete_data)
d_btn.place(x=510,y=745,width=255)

d_btn = Button(win,text='Display',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=display_data)
d_btn.place(x=765,y=745,width=255)

r_btn = Button(win,text='Reset',font='ariel 15 bold',bg='red',fg='white',bd=6,cursor='hand2',command=reset_data)
r_btn.place(x=1020,y=745,width=255)

e_btn = Button(win,text='Exit',font='ariel 15 bold',bg='red',fg='white',bd=6,cursor='hand2',command=exit_gui)
e_btn.place(x=1275,y=745,width=260)

scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill='x')

scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill='y')

table=ttk.Treeview(frame2,columns=('p_id','p_n','p_a','p_g','d/a','p_b','out','psy_id','doc','roc','ga','dos','dofu'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x=ttk.Scrollbar(command=table.xview)
scroll_y=ttk.Scrollbar(command=table.yview)

table.heading('p_id',text='Patient_ID')
table.heading('p_n',text='Patient_Name')
table.heading('p_a',text='Patient_Age')
table.heading('p_g',text='Patient_Gender')
table.heading('d/a',text='Disease/Abnormality Suffered')
table.heading('p_b',text='Patient_Behaviour')
table.heading('out',text='Outcome')
table.heading('psy_id',text='Psychiatric_ID')
table.heading('doc',text='Date of Closure')
table.heading('roc',text='Reason of Closure')
table.heading('ga',text='Goals Achieved')
table.heading('dos',text='Duration of Stay')
table.heading('dofu',text='Date of Follow_up')
table['show']='headings'
table.pack(fill=BOTH,expand=1)

table.column('p_id',width=100)
table.column('p_n',width=100)
table.column('p_a',width=100)
table.column('p_g',width=100)
table.column('d/a',width=100)
table.column('p_b',width=100)
table.column('out',width=100)
table.column('psy_id',width=100)
table.column('doc',width=100)
table.column('roc',width=100)
table.column('ga',width=100)
table.column('dos',width=100)
table.column('dofu',width=100)
table.bind('<ButtonRelease-1>',get_data)
display_data()
mainloop()