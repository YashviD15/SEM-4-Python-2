from django.shortcuts import render,HttpResponse

# Create your views here.
def add(request):
    return HttpResponse("Hello Yashviii")

def show(request):
     return render(request,"A.html")
  
def  display(request):
    name="Yashvi"
    age=20
    li=[23,20,25,18,21]
    data={"n":name,"a":age,"marks":li}
    return render(request,"B.html",data)

def main(request):
    return render(request,"main.html")

def h(request):
    return render(request,'home.html')

def s(request):
    return render(request,'s.html')

def a(request):
    return render(request,'ab.html')

def c(request):
    return render(request,'c.html')
