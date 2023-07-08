from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # endpoint to send the user the page files
    return render(request, 'compiler/home.html')

def preview(request):
    # end point to process the code sent by the user
    if request.method == 'POST':
        html_code = request.POST.get('html_code', '')
        css_code = request.POST.get('css_code', '')
        js_code = request.POST.get('js_code', '')

        output = f'''
            <html>
            <head>
                <style>
                    /* CSS Code */
                    {css_code}
                </style>
            </head>
            <body>
                {html_code}
                <script>
                    // JavaScript Code
                    {js_code}
                </script>
            </body>
            </html>
        '''
        return HttpResponse(output)
    else:
        return HttpResponse(status=400)


