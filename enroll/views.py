from django.shortcuts import render,HttpResponseRedirect, redirect
from .forms import StudentRegistration
from .models import User

# this function show all item and add new  item
def add_show(request):
 if request.method == 'POST':
    fm = StudentRegistration(request.POST)
    stud = User.objects.all()
    if fm.is_valid():
        nm =fm.cleaned_data['name']
        em =fm.cleaned_data['email']
        pm =fm.cleaned_data['password']
        rg = User(name = nm, email = em, password = pm)
        rg.save()
        fm = StudentRegistration()

 else:
    fm = StudentRegistration()
    stud = User.objects.all()

 return render(request, 'enroll/addandshow.html',{'form' :fm , 'stu': stud})

# this function use for update data
def update_data(request,id):
    print("testttt", request.method)
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()   
        return redirect("/")
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})
   
   

# this function will delete item
def delete_data(request,id):
   if request.method == 'POST':
      pi = User.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/')
      
   