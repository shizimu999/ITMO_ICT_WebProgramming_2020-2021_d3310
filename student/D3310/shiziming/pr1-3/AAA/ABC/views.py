from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import personForm
from .models import person
def detail(request, poll_id):
    try:
        p = person.objects.get(pk=poll_id)
    except person.DoesNotExist:
        raise Http404("person does not exist")
    return render(request, 'person.html', {'person': p})
def detail(request, person_id):
    try:
        dr = person.objects.get(pk=person_id)
    except person.DoesNotExist:
        raise Http404("driver does not exist")  #用django raise抛出异常
    return render(request, 'driver.html', {'driver': dr})

class person_list(ListView):
    model = person
    template_name = "persondata.html"

class person_data(DetailView):
    model = person
    template_name = 'personlist.html'

# class Car_deta(DetailView):
#     model = Car
#     template_name = "Car_deta.html"

def delete_person_data(respons,pk):
    d = person.objects.get(pk=pk)
    d.delete()
    return HttpResponse("Deleted")


def create_view(request):
    context = {}
    form = personForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "createperson.html", context)

from django.views.generic.edit import UpdateView

class personUpdateView(UpdateView):
  model = person
  fields = ('name', 'age', 'gender', 'bir')
  success_url = '/personsdata/'
  template_name = 'personupdata.html'