from django.shortcuts import render
from .forms import PDFUploadForm
from PyPDF2 import PdfMerger
from django.http import HttpResponse


def merge_pdfs_view(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():#If the form is valid, request.FILES['pdf1'] and request.FILES['pdf2'] allow you to access the files the user uploaded from the form ok hai tah 
            pdf1 = request.FILES['pdf1']
            pdf2 = request.FILES['pdf2']


            merger = PdfMerger()
            merger.append(pdf1)
            merger.append(pdf2)

            response = HttpResponse(content_type='application/pdf')  # here the instance has the  indeed contain the HTTP response data that is sent back to the client
            response['Content-Disposition'] = 'attachment; filename="merged.pdf" '
            #Content-Disposition: This is an HTTP header that indicates how the content should be displayed or handled by the browser.
            #attachment: This tells the browser to treat the response as a file to be downloaded rather than displayed directly in the browser window.

            merger.write(response)
            merger.close()

            return response
    else:
        #        # Initialize an empty form for GET request

        form= PDFUploadForm()

        # Render the form page with the form (for GET request or after invalid POST)

    return render(request, 'merge.html', {'form': form})
        
    





