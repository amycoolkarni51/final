from django.db import models

class CodeSnippet(models.Model):
    html_code = models.TextField()
    css_code = models.TextField()
    js_code = models.TextField()

