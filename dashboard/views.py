from django.shortcuts import render,redirect

from . decorators import unauthenticated_user,allowed_users
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .froms import ReportForm, UpdateReportForm
from .models import Report
from django.contrib.auth.models import User, Group
# Create your views here.


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    if request.user.is_authenticated:
        total_reports = Report.objects.all().order_by('-date').count()
        reports = Report.objects.all().order_by('-date')[0:8]
        limits= Report.objects.all().order_by('-date')[0:4]
        total_data = reports.count() 
        updated_reports = Report.objects.filter(isUpdated=True).count()
        UnUpdated_reports = total_reports - updated_reports
        viewed_reports = Report.viewers
        students =User.objects.filter(groups__name__in=['student'])
        NStudents =students.count()
        
        context = { 
            'reports': reports,
            'limits':limits,
            'total_data':total_data,
            'updated_reports':updated_reports,
            'UnUpdated_reports':UnUpdated_reports,
            'viewed_reports':viewed_reports,
            'total_reports':total_reports,
            'students':students,
            'NStudents':NStudents
            }
        return render(request, 'dashboard/dashboard.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def upload(request):
    
    students =User.objects.filter(groups__name__in=['student'])
    NStudents =students.count()
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        pdf = request.POST.get('pdf')
        files = {
            'title':title,
            'author':author,
            'description':description,
            'pdf':pdf,
        }
        form = ReportForm(files, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-page')
    else:
        form = ReportForm()
    context = {
        'form':form,
        'students':students,
        'NStudents':NStudents
        }
    return render(request, 'dashboard/upload.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def edit(request,pk):
    report = Report.objects.get(pk=pk)
    students =User.objects.filter(groups__name__in=['student'])
    NStudents =students.count()
    if request.method == 'POST':
        form = UpdateReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('dashboard-page')
    else:
        form = UpdateReportForm(instance=report)

    context = {
        'form':form,
        'students':students,
        'NStudents':NStudents
    }
    return render(request, 'dashboard/edit.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete(request,pk):
    students =User.objects.filter(groups__name__in=['student'])
    NStudents =students.count()
    if request.method == 'POST':
        report = Report.objects.get(pk=pk)
        report.delete()
        return redirect('dashboard-page')
    context = {
        'students':students,
        'NStudents':NStudents
    }
    return render(request, 'dashboard/delete.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def allStudents(request):
    # ty =Group.objects.order_by('students')
    students =User.objects.filter(groups__name__in=['student'])
    NStudents =students.count()
    context = {
        'students':students,
        'NStudents':NStudents
    }
    return render(request, 'dashboard/all_students.html',context)

@allowed_users(allowed_roles=['admin'])
@login_required(login_url='login')
def allReports(request):
    reports = Report.objects.all().order_by('-date')
    total_reports = Report.objects.all().order_by('-date').count()
    students =User.objects.filter(groups__name__in=['student'])
    NStudents =students.count()
    context = {
        'reports':reports,
        'total_reports':total_reports,
        'students':students,
        'NStudents':NStudents
    }
    return render(request, 'dashboard/all_reports.html',context)
