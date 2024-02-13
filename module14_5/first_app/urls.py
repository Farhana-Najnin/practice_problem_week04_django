from django.urls import path

from first_app.views import home,about,submitform,contactform,Modelform
urlpatterns = [
    path('', home, name = 'home_page'),
    path('about/', about, name = 'about_page'),

    path('form/', submitform, name = 'form_page'),
    path('Contact/', contactform, name = 'contact_page'),
    path('model/', Modelform, name = 'model_page'),
]