from django.urls import path,include

from db import views



urlpatterns = [
    path('', views.index ,name="index"),
    path('contact/', views.contact ,name="contact"),
    #path('check/', views.check ,name="check"),
    path('login/', views.login ,name="login"), 
    #path('signup/', views.signup ,name="signup"), 
    path('registration/', views.registeration ,name="registeration"),
    path('admin_dashboard/',views.admin_dashboard_registration,name="admin_dashboard_registration"),
    path('student_dashboard/',views.student_dashboard,name="student_dashboard"),
    path('contact_us/',views.contact,name="contact"),
    path('signup/', views.index ,name="index"),
    path('DeleteRegistration/<int:key>', views.DeleteRegistration ,name="DeleteRegistration"),
    path('DeleteContact/<int:key>', views.DeleteContact ,name="DeleteContact"),
    path('DeleteSignup/<int:key>', views.DeleteSignup ,name="DeleteSignup"),
    path('DeleteCourse/<int:key>', views.DeleteCourse ,name="DeleteCourse"),
    path('RegistrationAprroved/<int:key>' ,views.RegistrationApproved , name="RegistrationApproved"),
    path('registerlogin/', views.registerlogin , name="registerlogin"),
    path('logout/',views.logout,name='logout'),


    
    path('course/',views.ourcourses, name="ourcourses"),

    path('frontend/',views.frontend, name="frontend"),
    
    path('backend/',views.backend, name="backend"),

    path('database/',views.database, name="database"),
    
    path('marketing/',views.marketing, name="marketing"),
   
    path('faculty', views.faculty, name="faculty"),
    
    path('about', views.about, name="about"),
    
    path('add_course/',views.add_course,name='add_course'),
    path('course_detail/<int:key>',views.course_detail,name='course_detail'),
    path('course_page/<int:key>',views.course_page,name='course_page'),
    
    path('cppcompiler/', include('cppcompiler.urls')),
    path('javacompiler/', include('javacompiler.urls')),
    path('jscompiler/', include('jscompiler.urls')),
    path('pycompiler/', include('pycompiler.urls')),
    path('phpcompiler/', include('phpcompiler.urls')),
    path('webcompiler/', include('webcompiler.urls')),
    
]