from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import Student

# Create your views here.


def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list')
    else:
        form = StudentForm()
        context = {
            'form': form
        }
        return render(request, 'create.html', context)


def list(request):
    dataset = Student.objects.all()
    return render(request, 'list.html', {'dataset': dataset})


def delete(request, id):
    try:
        data = get_object_or_404(Student, id=id)
    except Exception:
        raise ('Does Not Exist')

    if request.method == 'POST':
        data.delete()
        return redirect('/list')
    else:
        return render(request, 'delete.html')


def update(request, id):
    try:
        old_data = get_object_or_404(Student, id=id)
    except Exception:
        raise ('Does Not Exist')

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=old_data)

        if form.is_valid():
            form.save()
            return redirect(f'/list')

    else:

        form = StudentForm(instance=old_data)
        context = {
            'form': form
        }
        return render(request, 'update.html', context)
