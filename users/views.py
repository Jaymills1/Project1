from django.shortcuts import render
from . decorators import unauthenticated_user,allowed_users
from django.contrib.auth.decorators import login_required
from dashboard.models import Report
from dashboard.froms import UpdateViewForm
# Create your views here.
@allowed_users(allowed_roles=['student'])
# @login_required(login_url='login')
def userPage(request):
    reports = Report.objects.all().order_by('-date')
    context ={
        'reports':reports
    }
    return render(request, 'users/userPage.html',context)


def details(request,pk):
    report = Report.objects.get(pk=pk)

    context = {
        'report':report,
    }
    return render(request, 'users/usersView.html',context)



