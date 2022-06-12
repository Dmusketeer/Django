from django.urls import path
from . import views

urlpatterns=[

    path('',views.about,name='about'),
    path('add/',views.add,name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
]
