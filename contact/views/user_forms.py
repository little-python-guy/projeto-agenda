from django.contrib import messages
from django.shortcuts import redirect, render

from contact.forms import RegisterFrom


def register(request):

    form = RegisterFrom()

    if request.method == 'POST':
        form = RegisterFrom(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:index')
    
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )
