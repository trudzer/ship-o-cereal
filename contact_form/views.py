from django.shortcuts import redirect, render

from contact_form.forms.contact_us_form import ContactUsForm


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('cereal-index')
    else:
        form = ContactUsForm()
    return render(request, 'contact_us.html', {
        'form': form
    })