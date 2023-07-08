from django.shortcuts import render
from django.http import HttpResponse
import subprocess

HELLO_WORLD = """
public class JavaProgram {
    public static void main(String[] args) {
        // Write your code here
        System.out.println("Hello World!");
    }
}
"""

# Create your views here.
def editor(request):
    # Endpoint for client's visit
    if request.method == 'GET':
        return render(request, 'editor_java.html', { 'code': HELLO_WORLD, 'output': '' })
    
    # Endpoint to execute the program sent thru POST
    elif request.method == 'POST':
        code_area_data = request.POST['codearea']
        output = ""

        try:
            # the contents of the code area are written to a file on the server
            with open('files/JavaProgram.java', 'w') as file:
                file.write(code_area_data)

            input_file_path = 'files/JavaProgram.java'
            output_file_path = 'files/'

            # output of the execution of the stored program
            result = subprocess.run(['javac', '-d', output_file_path, input_file_path], capture_output=True, text=True)

            # if there is compilation err:
            if result.returncode == 1:
                output = result.stderr
            else:
                # run the compiled script
                result = subprocess.run(['java', '-cp', 'files', 'JavaProgram'], capture_output=True, text=True, timeout=10)

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

        return render(request, 'editor_java.html', { 'code': code_area_data, 'output': output })
