import sys

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,'index.html')

def editor(request):
    codeareadata = "print('Hello World!')"
    output = ""

    if request.method == 'POST':

        codeareadata = request.POST['codearea']

        try:
            #save original standard output refernce
            original_stdout = sys.stdout
            sys.stdout = open('files/file.txt','w')  # change the standard output to the file we created

            #execute code
            exec(codeareadata)  # similar to print(codedata)

            sys.stdout.close()

            sys.stdout = original_stdout  #reset the original data into standard value


            #finally read output from file and save its output

            output = open('files/file.txt','r').read()

        except Exception as e:
            # to return error in code
            sys.stdout = original_stdout
            output = e

    #finally return and render page and send the codedata on index page
    return render(request,"editor_py.html", {"code": codeareadata , "output": output })