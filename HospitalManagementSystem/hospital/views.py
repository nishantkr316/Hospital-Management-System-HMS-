from django.shortcuts import render,redirect
from hospital.models import Doctor,Patient,Appointment
from hospital.forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# Create your views here.
#home view
@login_required
def home_view(request):
    return render(request,'home.html')


#doctor view
@login_required
def doctor_view(request):
    doctors = Doctor.objects.all()
    query = request.GET.get('q')
    if query:
        doctors = doctors.filter(Q(name__icontains=query) | Q(special__icontains=query))
    return render(request,'doctor.html',{'doctors':doctors})


#patient view'
@login_required
def patient_view(request):
    patients = Patient.objects.all()
    query = request.GET.get('q')
    if query:
        patients = patients.filter(Q(name__icontains=query) | Q(disease__icontains=query))
    return render(request,'patient.html',{'patients':patients})


#about view

@login_required
def about_view(request):
    return render(request,'about.html')

#doctor appointment view
@login_required
def doctor_appointment_view(request,id):
    doctor = Doctor.objects.get(id=id)
    appointments = doctor.appointments.all()
    query = request.GET.get('q')
    if query:
        appointments = appointments.filter(Q(patient__name__icontains=query) | Q(date__icontains=query))
    return render(request,'docapp.html',{'doctor':doctor,'appointments':appointments})

#patient appointment view

@login_required
def patient_appointment_view(request,id):
    patient = Patient.objects.get(id=id)
    appointments = patient.appointments.all()
    query = request.GET.get('q')
    if query:  
        appointments = appointments.filter(Q(doctor__name__icontains=query) | Q(date__icontains=query))
    return render(request,'patapp.html',{'patient':patient,'appointments':appointments})


#add doctor

@login_required
def add_doctor(request):
    if request.method == 'POST':
        name = request.POST['name']
        mob = request.POST['mob']
        special = request.POST['special']
        Doctor.objects.create(name=name,mob=mob,special=special)
        return redirect('doctors')
    return render(request,'adddoc.html')


#add patient
    
@login_required
def add_patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gen = request.POST['gen']
        disease = request.POST['disease']
        mob = request.POST['mob']
        address = request.POST['address']
        Patient.objects.create(name=name,age=age,gen=gen,disease=disease,mob=mob,address=address)
        return redirect('patients')
    return render(request,'addpat.html')

#delete doctor


@login_required
def delete_doctor(request,id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('doctors')

#delete patient


@login_required
def delete_patient(request,id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('patients')

#update doctor

@login_required
def update_doctor(request,id):
    doctor = Doctor.objects.get(id=id)
    if request.method == 'POST':
        doctor.name = request.POST['name']
        doctor.mob = request.POST['mob']
        doctor.special = request.POST['special']
        doctor.save()
        return redirect('doctors')
    return render(request,'updoc.html',{'doctor':doctor})


#update patient

@login_required
def update_patient(request,id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        patient.name = request.POST['name']
        patient.age = request.POST['age']
        patient.gen = request.POST['gen']
        patient.disease = request.POST['disease']
        patient.mob = request.POST['mob']
        patient.address = request.POST['address']
        patient.save()
        return redirect('patients')
    return render(request,'uppat.html',{'patient':patient})


#add appointment


@login_required
def add_appointment_view(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    if request.method == 'POST':
        doctor_id = request.POST['doctor']
        patient_id = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']
        doctor = Doctor.objects.get(id=doctor_id)
        patient = Patient.objects.get(id=patient_id)
        Appointment.objects.create(doctor=doctor,patient=patient,date=date,time=time)
        return redirect('appointments')
    return render(request,'addappointment.html',{'doctors':doctors,'patients':patients})


#view appointments


@login_required
def appointments_view(request):
    appointments = Appointment.objects.all()
    query = request.GET.get('q')
    if query:
        appointments = appointments.filter(Q(doctor__name__icontains=query) | Q(patient__name__icontains=query) | Q(date__icontains=query))
    return render(request,'appointment.html',{'appointments':appointments})


#update appointment


@login_required
def update_appointment(request,id):
    appointment = Appointment.objects.get(id=id)
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    if request.method == 'POST':
        doctor_id = request.POST['doctor']
        patient_id = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']
        doctor = Doctor.objects.get(id=doctor_id)
        patient = Patient.objects.get(id=patient_id)
        appointment.doctor = doctor
        appointment.patient = patient
        appointment.date = date
        appointment.time = time
        appointment.save()
        return redirect('appointments')
    return render(request,'upapp.html',{'appointment':appointment,'doctors':doctors,'patients':patients})


#delete appointment

@login_required
def delete_appointment(request,id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    return redirect('appointments')


#___________________________________________auth_______________________________________________________________________________


#signup view

def signup_view(request):
    type='Sign Up'
    form=SignupForm()
    
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request,"Account created successfully...")
            return redirect("login")
    return render(request, "signup.html",{'form':form,'type':type})



#login view


def login_view(request):
    type='Login'
    form=LoginForm()
    
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]  
            user=authenticate(username=username,password=password)
            
        if user:
            login(request,user)
            messages.success(request,"Logged in successfully...")
            return redirect("home")
        
        else:
            messages.warning(request,"Invalid username or password...")
    return render(request, "login.html",{'form':form,'type':type})


#logout view

@login_required
def logout_view(request):
    logout(request)
    messages.success(request,"Logged out successfully...")
    return redirect('login')



#change password view


from django.contrib.auth.forms import PasswordChangeForm
@login_required
def new_password(request):
    form =PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Password changed successfully...")
            return redirect('home')
    return render(request, "new_password.html", {'form': form})