from django.shortcuts import render
from django.http import HttpResponse
import subprocess

HELLO_WORLD = """
#include<iostream>
using namespace std;

int main() {
    cout << "Hello World!";
    return 0;
}
"""

# Create your views here.
def editor(request):
    # Endpoint for client's visit
    if request.method == 'GET':
        return render(request, 'editor.html', { 'code': HELLO_WORLD, 'output': '' })
    
    # Endpoint to execute the program sent thru POST
    elif request.method == 'POST':
        code_area_data = request.POST['codearea']
        output = ""

        try:
            # the contents of the code area are written to a file on the server
            with open('files/cpp_code.cpp', 'w') as file:
                file.write(code_area_data)

            input_file_path = 'files/cpp_code.cpp'
            output_file_path = 'files/cpp_code'

            # output of the execution of the stored program
            result = subprocess.run(['g++', input_file_path, '-o', output_file_path], capture_output=True, text=True, timeout=10)

            # if there is compilation err:
            if result.returncode == 1:
                output = result.stderr
            else:
                # run the compiled script
                result = subprocess.run(['files/cpp_code'], capture_output=True, text=True)

                # output is set to either stderr or stdout
                if result.returncode == 1:
                    output = result.stderr
                elif result.returncode == 0:
                    output = result.stdout

        # in case any other exception occurs in the subprocess, client will be notified
        except subprocess.CalledProcessError as e:
            output = str(e)
        except subprocess.TimeoutExpired as e:
            output = 'TIME LIMIT EXCEEDED'

        return render(request, 'editor.html', { 'code': code_area_data, 'output': output })
