from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from .forms import DoctorForm
from django.http import JsonResponse


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctor_form.html', {'form': form, 'title': 'Add Doctor'})

def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor_form.html', {'form': form, 'title': 'Edit Doctor'})

def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctor_confirm_delete.html', {'doctor': doctor})



def ajax_doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'ajax_doctor.html', {'doctors': doctors})

def ajax_doctor_add(request):
    if request.method == 'POST':
        doctor = Doctor.objects.create(
            name=request.POST['name'],
            specialty=request.POST['specialty'],
            contact=request.POST['contact']
        )
        return JsonResponse({'status': 'success', 'id': doctor.id})

def ajax_doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.name = request.POST['name']
        doctor.specialty = request.POST['specialty']
        doctor.contact = request.POST['contact']
        doctor.save()
        return JsonResponse({'status': 'updated'})

def ajax_doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    return JsonResponse({'status': 'deleted'})