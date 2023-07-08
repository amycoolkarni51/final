''' Added by Shruti Bathe and Vishal Patil - Description below'''

from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Registeration , SignUp , Contact , Course
from django.template import loader
from django.http import HttpResponse
import mysql.connector 



''' Added By:- Shruti Bathe  
    Function Name:- index
                    contact
                    login
                    registerlogin
                    DeleteRegistration
                    DeleteSignup
                    DeleteContact
                    DeleteCourse
                    student_dashboard
                    ourcourses
                    frontend
                    backend
                    database
                    marketing
                    faculty
                    about
                    course_detail
                    course_page
                    logout
'''

''' Added By :- Vishal Patil
    Function Name :-    registeration   (Date:-13/06/2023)
                        admin_dashboard_registration  (Date:-24/06/2023)
'''
            

# home page where we have signup also 
# function to fetch data from html signup form and insert in into database table
def index(request):
    if request.method=="POST":
        # connection with database
        m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
        cursor=m.cursor()
        d=request.POST
        # table field's data 
        for key,value in d.items():
            if key=="Full_Name":
                Full_Name=value
            if key=="EmailId":
                EmailId=value
            if key=='Password':
                Password=value
            if key=='Confirm_Password':
                Confirm_Password=value

            # checking conditions
        if len(Full_Name)<2 or len(EmailId)<2 or len(Password)<2 or len(Confirm_Password)<2:
            messages.error(request,"Please Enter All the Details Carefully!! Fields Should Not Be Empty")
        else:
            # inserting data into signup table          
            c="insert into signup(Full_Name,EmailId,Password,Confirm_Password) values('%s','%s','%s','%s')"%(Full_Name,EmailId,Password,Confirm_Password)
            cursor.execute(c)
            m.commit()
            #messages.success(request,'Your Successfully SignUp!!')
            return render(request,'login.html')
    else:
        return render(request,'index.html')
    

# function to fetch data from html contact form and insert in into database table
def contact(request):
    if request.method=="POST":
        # connection with database
        m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
        cursor=m.cursor()
        d=request.POST
        # table field's data 
        for key,value in d.items():
            if key=="First_Name":
                First_Name=value
            if key=="Last_Name":
                Last_Name=value
            if key=="EmailId":
                EmailId=value
            if key=="Location":
                Location=value
            if key=="Message":
                Message=value
        
            # inserting data into contact table          
            c="insert into contact(First_Name,Last_Name,EmailId,Location,Message) values('%s','%s','%s','%s','%s')"%(First_Name,Last_Name,EmailId,Location,Message)
            cursor.execute(c)
            m.commit()
            #messages.success(request,'Your Message has been send Successfully!!')
    return render(request,'contactus.html')


# function for login where we check login user is already signup or not
def login(request):
    global UserName,EmailId,Password
    if request.method=="POST":
        # connection with database
        m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
        cursor=m.cursor()
        data=request.POST
        # table field's data 
        for key,value in data.items():
            if key=='UserName':
                UserName=value
            if key=='EmailId':
                EmailId=value
            if key=='Password':
                Password=value
                          
         # selecting only email and password from signup tale                     
        query="select * from signup where EmailId='{}' and Password='{}'".format(EmailId,Password)  
        cursor.execute(query)
        t=tuple(cursor.fetchall())
            
        if t==():
            messages.error(request,"Kindly SignUp First!!")
            #messages.error(request,"If you have already register then might be your login details and your registration details are not matching")
            return render(request,'index.html') 
        else:
            return render(request,'course.html') 
    return render(request,'login.html')


# function for those student who has already registered to the course
def registerlogin(request):
    global UserName,EmailId,Password
    if request.method=="POST":
        # connection with database
        m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
        cursor=m.cursor()
        data=request.POST
        # table field's data 
        for key,value in data.items():
            if key=='EmailId':
                EmailId=value
            if key=='Password':
                Password=value
                          
         # selecting only email and password from signup tale                     
        query="select * from registeration where EmailId='{}' and Password='{}'".format(EmailId,Password)  
        cursor.execute(query)
        t=tuple(cursor.fetchall())
            
        if t==():
            #messages.error(request,"Kindly SignUp First!!")
            #messages.error(request,"If you have already register then might be your login details and your registration details are not matching")
            return render(request,'registeration.html')   
        else:
            query2="select * from registeration where EmailId='{}' and Password='{}'".format(EmailId,Password)
            cursor.execute(query2)
            result=tuple(cursor.fetchall())
            return render(request,'student_dashboard.html',{'result':result})
    return render(request,'registerlogin.html')


# function for registeration for the courses
def registeration(request):
    global First_Name,Last_Name,UserName,Address,Profession,Courses,EmailId,Password
    if request.method=="POST":
        # connection with database
        m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
        cursor=m.cursor()
        d=request.POST
        
        for key,value in d.items():
            if key=="Full_Name":
                Full_Name=value
            if key=="EmailId":
                EmailId=value
            if key=="Mobile":
                Mobile=value
            if key=="Gender":
                Gender=value
            if key=="City":
                City=value
            if key=="Qualification":
                Qualification=value
            if key=="Profession":
                Profession=value
            if key=="Courses":
                Courses=value
            if key=="Password":
                Password=value
            
        
        c="insert into registeration(Full_Name,EmailId,Mobile,Gender,City,Qualification,Profession,Courses,Password) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(Full_Name,EmailId,Mobile,Gender,City,Qualification,Profession,Courses,Password)
        cursor.execute(c)
        m.commit()
        #messages.success(request,"Congratulation! You have Successfully Registered!!! Kindly go to the home page for login!!")
        query2="select * from registeration where EmailId='{}' and Password='{}'".format(EmailId,Password)
        cursor.execute(query2)
        result=tuple(cursor.fetchall())
        return render(request,'student_dashboard.html',{'result':result})
    return render(request,'registeration.html')


 
#Task:- For deleting the register student from admin dashboard
def DeleteRegistration(request,key):
    # connection with database
    m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
    cursor=m.cursor()
    query="delete from registeration where id='{}'".format(key)
    cursor.execute(query)
    m.commit()
    return redirect('admin_dashboard_registration')



#Task:- For deleting the contact student from admin dashboard
def DeleteContact(request,key):
    # connection with database
    m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
    cursor=m.cursor()
    query="delete from contact where id='{}'".format(key)
    cursor.execute(query)
    m.commit()
    return redirect('admin_dashboard_registration')



#Task:- For deleting the signup student from admin dashboard
def DeleteSignup(request,key):
    # connection with database
    m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
    cursor=m.cursor()
    query="delete from signup where id='{}'".format(key)
    cursor.execute(query)
    m.commit()
    return redirect('admin_dashboard_registration')

  
#Task:- For deleting the course detail from admin dashboard
def DeleteCourse(request,key):
    # connection with database
    m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
    cursor=m.cursor()
    query="delete from course where id='{}'".format(key)
    cursor.execute(query)
    m.commit()
    return redirect('admin_dashboard_registration')



 
#Task:- For deleting the register student from admin dashboard
def RegistrationApproved(request,key):
    # connection with database
    m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
    cursor=m.cursor()
    query="update registeration SET Status='Approved' where id='{}'".format(key)
    cursor.execute(query)
    m.commit()
    return redirect('admin_dashboard_registration')




#Task:- For student dashboard
def student_dashboard(request):
    return render(request,'student_dashboard.html')
    
    



#Task :- data fetching for admin Dashboard 
def admin_dashboard_registration(request):
  Info = Registeration.objects.all().values()
  sign= SignUp.objects.all().values()
  contact= Contact.objects.all().values()
  course= Course.objects.all().values()
  template = loader.get_template('admin_dashboard.html')
  context = {
    'Info': Info,
    'sign': sign,
    'contact': contact,
    'course': course
  }
  return HttpResponse(template.render(context, request))






# Task :- for Courses page
def ourcourses(request):
   return render(request, 'course.html')



# Task :- fetch the frontend courses from database table
def frontend(request):
    # connection with database
    m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
    cursor=m.cursor()
    query="select id,course_name,course_desc,syllabus_pdf from course where select_course='Frontend'"
    cursor.execute(query)
    result=tuple(cursor.fetchall())
    return render(request,'frontend.html',{'result':result})



# Task :- fetch the backtend courses from database table
def backend(request):
    # connection with database
    m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
    cursor=m.cursor()
    query="select id,course_name,course_desc,syllabus_pdf from course where select_course='backend'"
    cursor.execute(query)
    result=tuple(cursor.fetchall())
    return render(request,'backend.html',{'result':result})
    


# Task :- fetch the database courses from database table
def database(request):
    # connection with database
    m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
    cursor=m.cursor()
    query="select id,course_name,course_desc,syllabus_pdf from course where select_course='Database'"
    cursor.execute(query)
    result=tuple(cursor.fetchall())
    return render(request,'database.html',{'result':result})
    



# Task :- fetch the marketing courses from database table
def marketing(request):
    # connection with database
    m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
    cursor=m.cursor()
    query="select id,course_name,course_desc,syllabus_pdf from course where select_course='Marketing'"
    cursor.execute(query)
    result=tuple(cursor.fetchall())
    return render(request,'marketing.html',{'result':result})
   


# Task :- for faculty page
def faculty(request):
    return render(request,'faculty.html')

# Task :- for about page
def about(request):
    return render(request,'about.html')


# Task :- to add courses with the help of add course form from admin dashboard and insert data into database table
def add_course(request):
    if request.method == 'GET':
        return render(request, 'add_course.html')
    else:
        Course(
            course_name=request.POST['c_name'],
            course_desc=request.POST['c_desc'],
            syllabus_pdf=request.POST['s_pdf'],
            introduction_link=request.POST['i_link'],
            pdf_link=request.POST['p_link'],
            video_link=request.POST['v_link'],
            select_course=request.POST['s_course'],
            filename=request.POST['filename']
        ).save()
        return render(request, 'add_course.html')
    

# Task :- to fetch course data from database table and display it on course_detail page  
def course_detail(request,key):
    # connection with database
    m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
    cursor=m.cursor()
    query="select * from course where id='{}'".format(key)
    cursor.execute(query)
    result=tuple(cursor.fetchall())
    return render(request, 'course_detail.html', {'result':result})

# Task :- to fetch course data from database table and display it on course_page page
def course_page(request,key):
    # connection with database
    m=mysql.connector.connect(host="localhost",user="root",password="",database="web_db")
    cursor=m.cursor()
    query="select * from course where id='{}'".format(key)
    cursor.execute(query)
    result=tuple(cursor.fetchall())
    return render(request, 'course_page.html', {'result':result})

# Task:- user logout from student dashboard
def logout(request):
    return render(request,'index.html')