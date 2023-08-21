from django.shortcuts import render
from .models import Laptop
from django.contrib import messages
from django.db.models import Q


def index(request):
    laptops = Laptop.objects.all()
    query = ""

    if request.method == 'POST':
        if 'Add' in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            text = request.POST.get('text')
            Laptop.objects.create(
                id = id,
                name=name,
                comment=text,
                email=email,

            )
            messages.success(request, "Machine Added Successfully")


        elif 'update' in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            text = request.POST.get('text')
            update_laptop = Laptop.objects.get(id=id)
            update_laptop.name = name
            update_laptop.email = email
            update_laptop.text = text
            update_laptop.save()

            messages.success(request, 'Machine Updated Successfully')



        elif 'search' in request.POST:
            query = request.POST.get('searchquery')
            laptops = Laptop.objects.filter(
                Q(name__icontains=query) | Q(email__icontains=query) | Q(comment__icontains=query))

        elif 'delete' in request.POST:
            id = request.POST.get('id')
            Laptop.objects.get(id=id).delete()

            messages.success(request, 'Student Deleted Successfully')

    context = {'laptops': laptops, 'query': query}
    return render(request, 'index.html', context=context)
