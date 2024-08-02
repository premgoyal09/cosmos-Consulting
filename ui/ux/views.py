from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ux.models import Contact
from ux.models import User
from .forms import SignupForm, LoginForm





from django.views.decorators.csrf import csrf_protect
# Create your views here.


def home(request):
    return render(request, 'first/home.html')
    # return HttpResponse('This si sthe gom')   

def about(request):
    return render(request, 'first/about.html')

def whychoose(request):
    return render(request, 'first/whychoose.html')

def industry(request):
    return render(request, 'first/industry.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "please fill the form attentively ")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "thanks you , your messages was sent sucessfully")

    return render(request, 'first/contact.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password']
            user.save()
            return redirect('login')        
    else:
        form = SignupForm()
    return render(request, 'torm/signup.html', {'form': form})
    # return HttpResponse("I am Sign up")




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                request.session['user_id'] = user.id
                messages.success(request, 'Logged in successfully!')
                return redirect('home')
            except User.DoesNotExist:
                messages.error(request, 'Invalid credentials!')
    else:
        form = LoginForm()
    return render(request, 'torm/login.html', {'form': form})
        
# def home_view(request):
#     if 'user_id' in request.session:
#         user = User.objects.get(id=request.session['user_id'])
#         return render(request, 'torm/home.html', {'user': user})
#     return redirect('login')


# def users_view(request):
#     if 'user_id' in request.session:
#         users = User.objects.all()
#         return render(request, 'torm/users.html', {'users': users})
#     return redirect('login')


def logout_view(request):
    try:
        del request.session["user_id"]
    except KeyError:
        print("error")
    return redirect('signup')

    return render(request, 'torm/logout.html')
    # return HttpResponse("I am logout up")


    