from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import racerForm,groupForm
from .models import Match,comments,round,group,Racer,Racing_car,result
from django.views.generic.edit import UpdateView,CreateView

def group_list(request):
  model1 = group.objects.filter().all
  model2 = result.objects.filter().all

  return render(request,"group_list.html",context=locals())

class group_deta(DetailView):
    model = group
    template_name = "group_deta.html"

def create_group(request):
    context = {}
    form = groupForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "creategroup.html", context)

def create_racer(request):
    context = {}
    form = racerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "createracer.html", context)

class racerUpdateView(UpdateView):
  model = Racer
  fields = ('racer_name','Introduction','rank','ID_group')
  success_url = "/grouplist/"
  template_name = 'modifyracer.html'

def delete_racer(respons,pk):
    d = Racer.objects.get(pk=pk)
    d.delete()
    return HttpResponse("Deleted")

class car_type(UpdateView):
  model = Racing_car
  fields = ('Vehicle_type',)
  success_url = "/grouplist/"
  template_name ="First_one.html"

class AuthorCreate(CreateView):
    model = result
    fields = ['result','ID_racer','ID_Match','time_cost']
    template_name = "create_result.html"
    success_url = "/grouplist/"

class AuthorCreate2(UpdateView):
    model = result
    fields = ['result','ID_racer','ID_Match','time_cost']
    template_name = "up_data_result.html"
    success_url = "/grouplist/"

def delete_result(respons,pk):
    d = result.objects.get(pk=pk)
    d.delete()
    return HttpResponseRedirect('/grouplist/')

def result_list(request):
  model2 = result.objects.filter().all

  return render(request,"result_list.html",context=locals())


