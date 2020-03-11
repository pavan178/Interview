from django.shortcuts import render

from .forms import ContactForms, SnippetForm


#creating comtact form to save details
def contact(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['Phone']
            email = form.cleaned_data['Email']
            list1 = [name, phone, email] #saving the input as a list

            print(list1) #printing the data as a list which will be displayed in the cmd

    form = ContactForms()

    return render(request, 'form.html', {'form': form})

#creating a snippit form to store data in db and later edit it with admin panel
def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['Phone']
            email = form.cleaned_data['Email']
            list1 = [name, phone, email] #saving the input as a list

            print(list1) #printing the data as a list  which will be displayed in the cmd
            form.save() #Saving the form into db

    form = SnippetForm()

    return render(request, 'form.html', {'form': form})
