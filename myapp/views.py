from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserUpdateForm
from django.conf import settings
from .paytm import checksum
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')

def doctor_profile(request):
    return render(request, 'doctor_profile.html')

def register(request):
    return render(request, 'register.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

def initiate_payment(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        order_id = "ORDERID" + str(checksum.__time_stamp__())
        
        data = {
            'MID': settings.PAYTM_MERCHANT_ID,
            'ORDER_ID': order_id,
            'TXN_AMOUNT': str(amount),
            'CUST_ID': 'CUST001',
            'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
            'WEBSITE': settings.PAYTM_WEBSITE,
            'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
            'CALLBACK_URL': settings.PAYTM_CALLBACK_URL,
        }
        data['CHECKSUMHASH'] = checksum.generate_checksum(data, settings.PAYTM_MERCHANT_KEY)
        return render(request, 'payment.html', {'paytm_dict': data})
    return render(request, 'payment.html')

@csrf_exempt
def callback(request):
    if request.method == "POST":
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            paytm_params[key] = str(value[0])
        is_valid_checksum = checksum.verify_checksum(paytm_params, settings.PAYTM_MERCHANT_KEY, paytm_checksum)
        if is_valid_checksum:
            return render(request, 'callback.html', {'response': paytm_params})
        else:
            return render(request, 'callback.html', {'error': 'Checksum verification failed'})
