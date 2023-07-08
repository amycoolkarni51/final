import sys
import subprocess

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def editor(request):
    # place holders
    codeareadata = """
<?php
    echo "Hello, World!";
?>
    """
    output = ""

    if request.method == 'POST':
        # get the code in the codearea thru post and write it in a file to be executed
        codeareadata = request.POST['codearea']
        with open('files/file.php', 'w') as file:
            file.write(codeareadata)

        try:
            # run the php code
            output = subprocess.run(['php', 'files/file.php'], capture_output=True, text=True, timeout=10)

            # if the code runs well, stdout is returned else stderr is returned
            if output.returncode == 0:
                output = output.stdout
            else:
                output = output.stderr

        # any other exceptions are handled here
        except Exception as e:
            output = e

    #finally return and render page and send the codedata on index page
    return render(request,"editor_php.html", {"code": codeareadata , "output": output })