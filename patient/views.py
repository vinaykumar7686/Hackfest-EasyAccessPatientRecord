from .forms import RegForm, MedicalInfoForm
from django.shortcuts import render,redirect

# Create your views here.
def pat_homepage(request):
    return render(request=request, template_name='pat_home.html')

def pat_register(request):
    form = RegForm()
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('pat_homepage')
    context = {'form': form}
    return render(request, 'pat_register.html', context)


def pat_medicalForm(request):
    form = MedicalInfoForm()
    if request.method == 'POST':
        form = MedicalInfoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('pat_homepage')
    context = {'form': form}
    return render(request, 'pat_medicalForm.html', context)
