from django.shortcuts import render

from contact.forms import RegisterFrom


def register(request):

    form = RegisterFrom()

    if request.method == 'POST':
        form = RegisterFrom(request.POST)
        
        if form.is_valid():
            form.save()
    
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )
