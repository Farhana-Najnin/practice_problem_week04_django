from django.shortcuts import render
from . forms import contact_form
from first_app.forms import PracticeForm
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        select = request.POST.get('select')
        return render(request, 'about.html',{'name': name, 'email': email, 'rating': select })
    else:
        return render(request, 'about.html')


def submitform(request):
    return render(request, 'form.html')
    

def contactform(request):
    if request.method == 'POST':
        form = contact_form(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = contact_form()

    return render(request, 'contactform.html', {'form' : form})

def Modelform(request):
    if request.method == 'post':
        res = PracticeForm(request.POST)
        if res.is_valid():
            res.save(commit = True)
    else:
        res = PracticeForm()
        
    return render(request,'model.html', {'form' : res})