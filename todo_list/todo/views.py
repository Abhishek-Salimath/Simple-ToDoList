from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from todo.models import Todo


# Create your views here.



def index(request):
    todo=Todo.objects.all()
    if request.method=='POST':
        newnote=Todo()
        newnote.title=request.POST['title']
        newnote.save()
        return redirect('index')
    return render(request, 'todo/index.html',{'todos':todo})

def delete(request,pk):
    todo=Todo.objects.get(id=pk)
    todo.delete()
    return redirect('index')