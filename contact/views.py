from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import ContactForm


def Contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'This is not a valid form')
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
