from django.shortcuts import render,redirect
from .forms import studentRegistration
from .models import User

# The Function Will Add New Student And Show All Student 
def add_show(request):
    form = studentRegistration()
    if request.method == 'POST':
        form = studentRegistration(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = studentRegistration()   
    student = User.objects.all()         
    return render(request,'enroll/add_and_show_data.html',{'form':form,'student':student})

# The Function Will Update Student
def update_data(request,id):
        user = User.objects.get(id=id) 
        form = studentRegistration(instance=user)
        if request.method == 'POST':
            form = studentRegistration(request.POST,instance=user)
            if form.is_valid():
                form.save()
            else:
                 user = User.objects.get(id=id) 
                 form = studentRegistration(instance=user) 
        return render(request,'enroll/update_data.html',{'form':form})           

# The Function Will Delete Student 
def delete_data(request,id):
    user = User.objects.get(id=id) 
    user.delete()
    return redirect('enroll:add_and_show_data')
