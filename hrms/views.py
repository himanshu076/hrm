from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import json
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError
from django.contrib.auth.models import check_password
from rest_framework.permissions import AllowAny
from rest_framework import serializers

# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def Register_Users(request):
    try:
        data = []
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.is_active = True
            account.save()
            token = Token.objects.get_or_create(user=account)[0].key
            data["message"] = "user registered successfully"
            data["email"] = account.email
            data["username"] = account.username
            data["token"] = token

        else:
            data = serializer.errors


        return Response(data)
    except IntegrityError as e:
        account=User.objects.get(username='')
        account.delete()
        raise ValidationError({"400": f'{str(e)}'})

    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})

@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):

        data = {}
        reqBody = json.loads(request.body)
        email1 = reqBody['Email_Address']
        print(email1)
        password = reqBody['password']
        try:

            Account = User.objects.get(Email_Address=email1)
        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})

        token = Token.objects.get_or_create(user=Account)[0].key
        print(token)
        if not check_password(password, Account.password):
            raise ValidationError({"message": "Incorrect Login credentials"})

        if Account:
            if Account.is_active:
                print(request.user)
                login(request, Account)
                data["message"] = "user logged in"
                data["email_address"] = Account.email

                Res = {"data": data, "token": token}

                return Response(Res)

            else:
                raise ValidationError({"400": f'Account not active'})

        else:
            raise ValidationError({"400": f'Account doesnt exist'})



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