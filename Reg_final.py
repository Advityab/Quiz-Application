from tkinter import *
from tkinter import ttk ,messagebox
from PIL import Image,ImageTk
# import pymysql
import mysql.connector
from plyer import notification

class Registration():
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form ")
        self.root.geometry("1600x1200+0+0")
        self.root.config(bg="White")

        # ================================Background Image==========================================
        self.bg = ImageTk.PhotoImage(file=r"D:\quiz python\python quiz MP\backimg.jpeg")
        bg= Label(self.root,image=self.bg).place(x=200, y=0, relwidth=1, relheight=1)

        #==================================Left side images Here====================================
        logo = Image.open(r"D:\quiz python\python quiz MP\logoimg.jpeg")
        logo = logo.resize((420, 600), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(logo)

        f_Lable = Label(self.root, image=self.photoimg)
        f_Lable.place(x=80, y=100, width=420, height=600)

        SignIn_button = Button(f_Lable,comman=self.Login_Window,text="Sign In", font=("times new roman", 15), bg="black", fg="gold",cursor="hand2")
        SignIn_button.place(x=140, y=480, width=140, height=40)

        # Registration From
        Reg_frame = Frame(self.root,bg="White")
        Reg_frame.place(x=500,y=100,width=700,height=600)


        title = Label(Reg_frame, text= "REGISTRATION FORM" , font= ("times new roman",20,"bold") , bg="white",fg="blue")
        title.place(x=185,y=30,width=300,height=40)

        # =======================================Row 1==============================
        # self.var_fname = StringVar()
        f_name = Label(Reg_frame,text="First Name ",font=("times new roman" ,20,"bold"),bg="white" , fg ="Purple")
        f_name.place(x=50,y=90,width=140,height=30)

        self.txt_fname=Entry(Reg_frame,font=("times new roman",15) , bg="lightgray",fg="black")
        self.txt_fname.place(x=50,y=130,width=240)

        l_name = Label(Reg_frame, text="Last Name ", font=("times new roman", 20, "bold"), bg="white", fg="Dark blue")
        l_name.place(x=380, y=90, width=140, height=30)

        self.txt_lname = Entry(Reg_frame, font=("times new roman", 15), bg="lightgray", fg="black")
        self.txt_lname.place(x=380, y=130,width=240)

        # =======================================Row 2==============================
        User = Label(Reg_frame,text="Username",font=("times new roman" ,20,"bold"),bg="white" , fg ="Purple")
        User.place(x=50,y=160,width=120,height=30)

        self.txt_user=Entry(Reg_frame,font=("times new roman",15) , bg="lightgray",fg="black")
        self.txt_user.place(x=50,y=200,width=240)

        Pass = Label(Reg_frame,text="Password",font=("times new roman" ,20,"bold"),bg="white" , fg ="Dark blue")
        Pass.place(x=380,y=160,width=120,height=30)

        self.txt_pass=Entry(Reg_frame,font=("times new roman",15) , bg="lightgray",fg="black")
        self.txt_pass.place(x=380,y=200,width=240)

        # =======================================Row 3==============================
        gender = Label(Reg_frame,text="Gender",font=("times new roman" ,20,"bold"),bg="white" , fg ="Purple")
        gender.place(x=50,y=230,width=100,height=30)

        self.choice1 = ttk.Combobox(Reg_frame, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.choice1["values"] = ("Select", "Male", "Female")
        self.choice1.place(x=50, y=270,width=240)
        self.choice1.current(0)

        email = Label(Reg_frame, text="Email Id", font=("times new roman", 20, "bold"), bg="white", fg="Dark blue")
        email.place(x=380, y=230, width=100, height=30)

        self.txt_email = Entry(Reg_frame,text="", font=("times new roman", 15), bg="lightgray", fg="black")
        self.txt_email.place(x=380, y=270,width=240)

        # =======================================Row 4==============================
        phone_no = Label(Reg_frame, text="Phone No", font=("times new roman", 20, "bold"), bg="white", fg="Purple")
        phone_no.place(x=50, y=300, width=120, height=30)

        self.txt_phone = Entry(Reg_frame, font=("times new roman", 15), bg="lightgray", fg="black")
        self.txt_phone.place(x=50, y=340,width=240)

        DOB = Label(Reg_frame, text="DOB (DD/MM/YY)", font=("times new roman", 18, "bold"), bg="white", fg="Dark blue")
        DOB.place(x=380, y=300, width=200, height=30)

        self.txt_dob = Entry(Reg_frame, font=("times new roman", 15), bg="lightgray", fg="black")
        self.txt_dob.place(x=380, y=340,width=240)

        # =======================================Row 5==============================
        security_que = Label(Reg_frame, text="Security Question", font=("times new roman", 20, "bold"), bg="white", fg="Purple")
        security_que.place(x=50, y=370, width=210, height=30)

        self.choice = ttk.Combobox(Reg_frame, font=("times new roman", 15),state="readonly",justify=CENTER)
        self.choice["values"]=("select","Your pet name" ,"Your School name","Your Favorite colour","Your Favorite Place")
        self.choice.place(x=50, y=410,width=240)
        self.choice.current(0)

        answer= Label(Reg_frame, text="Answer", font=("times new roman", 20, "bold"), bg="white", fg="Dark blue")
        answer.place(x=380, y=370, width=100, height=30)

        self.txt_answer = Entry(Reg_frame, font=("times new roman", 15), bg="lightgray", fg="black")
        self.txt_answer.place(x=380, y=410,width=240)

        # ===================================== check Box==============================
        self.var_check = IntVar()
        check=Checkbutton(Reg_frame,text="I agree with the Terms & Conditions",variable=self.var_check,onvalue=1,offvalue=0,bg="white",fg="Red",font=("times new roman ",15,)).place(x=50,y=450)

        # ==========================================Registration button=====================================
        # self.button_image=ImageTk.PhotoImage(file="image/button.png")
        button=Button(Reg_frame,text="Register here",font=("times new roman",15) , bg = "blue" ,fg ="white",cursor="hand2",command=self.register_data).place(x=270,y=500,width=140,height=40)

    def Login_Window(self):
        self.root.destroy()
        import main


    def register_data(self):
       F_NAME = self.txt_F_NAME.get()
       L_NAME = self.txt_L_NAME.get()
       USERNAME  = self.txt_USER.get()
       PASSWORD  = self.txt_PASSWORD.get()
       GENDER  = self.choice1.get()
       EMAIL_ID =   self.txt_EMAIL_ID.get()
       PHONE =   self.txt_PHONE.get()
       DOB =     self.txt_DOB.get()
       SEC_QEU =  self.choice.get()
       ANSWER =   self.txt_ANSWER.get()

       if F_NAME == "" or USERNAME == "" or PASSWORD == ""or GENDER == ""or EMAIL_ID == ""or PHONE == ""or DOB == "" or SEC_QEU =="" or ANSWER =="":
        messagebox.showerror("Error","All Fields Are Required",parent=self.root)

       elif self.var_check.get() == 0:
           messagebox.showerror("Error", "Please agree with our Terms And Conditions", parent=self.root)

       else:
           try:
               con = mysql.connector.connect(host="localhost",port=3306,user="root",password="saloni",database="quizguru")

               cur=con.cursor()

               cur.execute("insert into reg values('"+F_NAME+"' ,'"+L_NAME+"' ,'"+USERNAME+"','"+PASSWORD+"','"+GENDER+"','"+EMAIL_ID+"','"+PHONE_NO+"','"+DOB+"','"+SEC_QEU+"','"+ANSWER+"')")

               con.commit()
               con.close()
               messagebox.showinfo("Success","Register Successfully",parent=self.root)
               title = "Quiz Guru"
               message = "Congratulations , You have Successfully Register in Quiz Guru!!\n Thank You."
               notification.notify(
                   title=title,
                   message=message,
                   app_icon=None,
                   timeout=5,
                   toast=False
               )
           except Exception as ae:
               messagebox.showerror("Error",f"Error due to the : str{ae}",parent=self.root)

root=Tk()
obj=Registration(root)
root.mainloop()