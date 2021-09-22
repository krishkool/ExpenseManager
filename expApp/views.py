from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BalanceManage, ExpenseManage
from decimal import Decimal

#packages for login and logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

#packages for Email setup
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from ExpenseManager.settings import EMAIL_HOST_USER

#packages for User
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home(request):
    return render(request, 'index.html')

def expenseView(request):
    return render(request, 'addexpenseview.html')

def walletView(request):
    return render(request, 'walletview.html')

def totexpenseView(request):
    return render(request, 'showexpense.html')


def login_view(request):
    uname = request.POST['username']
    pwd   = request.POST['password']

    user = authenticate(request, username = uname, password = pwd)

    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login')


def addBalance(request):
    try:
        amt = request.POST['bal-amt']
        try:

            balData = BalanceManage.objects.get()
            cur_bal = balData.Balance
            val_amt = Decimal(amt)
            new_bal = cur_bal + val_amt
            balData.Balance = new_bal
            balData.save()
            return render(request, 'walletview.html', {"msg": "Balance Added!"})
        except Exception as e:
            print(e)
            firstData = BalanceManage(Balance = amt)
            firstData.save()
            return render(request, 'walletview.html', {"msg": "Balance Added!"})
    except Exception as e:
        print(e)
        return render(request, 'walletview.html', {"msg": "Unable to Add Balance!"})

def showBalance(request):
    try:
        balData = BalanceManage.objects.get()
        bal = balData.Balance
        return render(request, 'walletview.html', {"balance": bal})

    except Exception as e:
        print(e)
        return render(request, 'walletview.html', {"msg1": "Unable to Display Balance"})

def showExpenses(request):
    try:
        tot = 0
        expData = ExpenseManage.objects.all()
        for i in expData:
            tot = tot + i.Amount
        
        return render(request, 'showexpense.html', {"data": expData, "val": tot})

    except Exception as e:
        print(e)
        return render(request, 'showexpense.html', {"msg": "Unable to Display Expense History!"})


def addExpense(request):
    try:
        name = request.POST['exp-name']
        amount = request.POST['exp-amt']
        desc = request.POST['exp-desc']
        date = request.POST['exp-date']

        balData = BalanceManage.objects.get()
        curbal = Decimal(balData.Balance)
        amt = Decimal(amount)

        if (amt > curbal):
            return render(request, 'addexpenseview.html', {"fail": "Insufficient Wallet Balance!"})

        else:
            expData = ExpenseManage(Name = name, Amount = amount, Description = desc, Date = date)
            expData.save()
            balData = BalanceManage.objects.get()
            curbal = Decimal(balData.Balance)
            amt = Decimal(amount)
            new_bal = curbal - amt
            balData.Balance = new_bal
            balData.save()
            return render(request, 'addexpenseview.html', {"success": "Expense Created!"})

    except Exception as e:
        print(e)


def reset_view(request):
    return render(request, 'registration/ResetPassword.html')

def passReset(request):
    try:

        respDict = {}
        username = request.POST['uname']
        receiver = request.POST['em']
        pwd = request.POST['password']
 
        subject = "Password Reset"

        try:
            user = User.objects.get(username = username)
            if user is not None:
                user.set_password(pwd)
                user.save()
                message = "Password Changed Successfully"

                send_mail(subject, message, EMAIL_HOST_USER, [receiver])
                respDict["msg"] = "Password Reset Successful!"
                return redirect('login')
        except Exception as e:
            print(e)
            respDict["msg"] = "Email verification failed!"
            return render(request, 'registration/resetpassword.html', respDict)

    except Exception as e:
        print(e)
        respDict["msg"] = "Username doesn't exists"
        return render(request, 'registration/resetpassword.html', respDict)


    

    







