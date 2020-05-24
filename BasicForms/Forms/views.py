from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'Forms/index.html')


def form_name_view(request):
    form = forms.FormName()
    #form_dict = {'form': form}
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATIONS SUCCESS.")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, 'Forms/form.html', {'form': form})


