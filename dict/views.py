from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context #pass context to the html and render itself
from django.template.loader import get_template
from .forms import ContactForm

# Create your views here.

def index(request):
    # title = "Welcome"
    # if request.user.is_authenticated():
    #     title = "Hello %s" %(request.user)

    #add a form
    form = ContactForm(request.POST or None)
    context = {
        "form": form,
        }


    if form.is_valid():
        instance = form.save(commit=False)

        email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        if not full_name:
            full_name = "Анонім_ка"
        instance.full_name = full_name
        instance.save()
        # print (instance.email)
        # print (instance.timestamp)


    return render(request, 'index.html', context)

def qa(request):
    return render(request, 'q-a.html', {})
