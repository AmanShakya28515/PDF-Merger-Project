from django.urls import path 
from . import views

urlpatterns=[
    path('',views.merge_pdfs_view,name='merger_pdf'),
    
]