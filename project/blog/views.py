from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import ParentForm
from .models import Child, Parent


class ChildCreate(CreateView):
    model = Child
    fields = '__all__'
    success_url = "/"


class ParentCreate(CreateView):
    model = Parent
    fields = '__all__'


def parent_create(request):
    if request.method == "GET":
        form = ParentForm()
        return render(request, 'parent_form.html', {"form": form})
    elif request.method == "POST":
        form = ParentForm(request.POST)
        if form.is_valid():
            id = form.save()
            # print(id.pk)
            return HttpResponse(f'<script type="text/javascript">window.close(); window.opener.setData("{id.pk}");</script>')
        else:
            return render(request, 'parent_form.html', {"form": form})


def get_parent_id(request):
    print('ajax call :', request)
    if request.method == "GET":
        return HttpResponse("OK")
    if request.is_ajax():
        id = request.POST['id']
        parent = Parent.objects.filter(pk=id)
        print(id)
        print(parent)
        data = serialize("json", parent, fields=("name"))
        return HttpResponse(data, content_type="application/json")
