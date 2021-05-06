from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from contact_form.forms.contact_us_form import ContactUsForm
from contact_form.models import ContactUs


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

def feedback(request):
    feedbacks = [ {
        'id': x.id,
        'name': x.name,
        'email': x.email,
        'message': x.message,
    } for x in ContactUs.objects.all() ]
    #return JsonResponse({ 'data': feedbacks })
    context = {'feedbacks': ContactUs.objects.all().order_by('id')}
    return render(request, 'feedback.html', context)