from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import ListItems
from .forms import ToDoForms
# Create your views here.
list_items = []


def userlist(request):

    #items = request.GET.get('add')
    #list_items.append(items)
    #content = {
    #    'list_items': list_items[1:]
    #}
    #print(list_items)
    #if request.method == 'POST':
    #    if request.GET:
    #        list.remove()

    form = ToDoForms()
    items = ListItems.objects.order_by('id')
    content = {
        'items': items,
        'form': form
    }
    return render(request, 'base.html', content)


@require_POST
def addform(request):
    forms = ToDoForms(request.POST)
    if forms.is_valid():
        db = ListItems(items=request.POST['text'])
        db.save()

    return redirect("/")


def compform(request, item_id):
    items = ListItems.objects.get(pk=item_id)
    items.complete = True
    items.save()

    return redirect('/')


def delcomp(request):
    hell = ListItems.objects.filter(complete__exact=True).delete()

    return redirect('/')


def delall(request):
    hell = ListItems.objects.all().delete()

    return redirect('/')