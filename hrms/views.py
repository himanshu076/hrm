from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request, 'hrms/home/home.html')

def registration(request):
    if request.method == 'GET':
        form  = RegistrationForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    if request.method == 'POST':
        form  = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('home_page')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register.html', context)

    return render(request, 'hrms/registrations/registration.html')

# class Register (CreateView):
#     model = get_user_model()
#     form_class  = RegistrationForm
#     template_name = 'hrms/registrations/register.html'
#     success_url = reverse_lazy('hrms:login')

def books(request):
    if request.user.is_authenticated:
        return render(request, 'hrms/books/books.html')
    else:
        return redirect('accounts/login')
# class index(TemplateView):
#     template_name = 'hrms/home/home.html'

# class registration(TemplateView):
#     template_name = 'hrms/registrations/login.html'

# class view():
#     def my_view(request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             ...
#         else:
#             # Return an 'invalid login' error message.
            # ""

def login(request):
    if request.user.is_authenticated:
        return redirect('books/')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('hrms/')
        else:
            form = AuthenticationForm()
            return render(request,'hrms/registrations/login.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'hrms/registrations/login.html', {'form':form})