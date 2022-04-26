from django.http import HttpResponse
from django.shortcuts import redirect, render

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard-page')
        else:
            return HttpResponse('Login')
    return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
				print(group)

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return redirect('user-page')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'student':
			return redirect('user-page')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function

def user_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'admin':
			return redirect('dashboard-page')

		if group == 'students':
			return view_func(request, *args, **kwargs)

	return wrapper_function


# from django. http import HttpResponse
# from django.shortcuts import redirect

# def unauthenticated_user(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('user-page')
#         else:
#             return view_func(request, *args, **kwargs)
#     return wrapper_func

# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):

#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name

#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse('You are not authorized to view this page')
#         return wrapper_func
#     return decorator

# def student_only(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name
#         if group == 'admin':
#             return redirect('dashboad-page')
#         if group == 'students':
#             return view_func(request, *args, **kwargs)
            
#     return wrapper_function