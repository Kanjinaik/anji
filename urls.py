from django.urls import path
from .import views

urlpatterns=[

    path('available/',views.available_rooms),
    path('create/',views.create_customer),
    path('book/',views.book_rooms),
]