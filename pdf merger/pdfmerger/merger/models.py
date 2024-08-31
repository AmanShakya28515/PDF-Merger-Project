from django.db import models

class PDFUpload(models.Model):
    pdf1 = models.FileField(upload_to='pdfs/')
    pdf2 = models.FileField(upload_to='pdfs/')


    
