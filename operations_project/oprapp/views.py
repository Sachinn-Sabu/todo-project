from django.shortcuts import render

# Create your views here.
def home(request):

        return render(request,'home.html')

def result(request):
        a = int(request.GET['num1'])
        b = int(request.GET['num2'])

        add = a + b
        sub = a - b
        mul = a * b
        div = a / b
        return render(request,'result.html',{'obj1':add,'obj2':sub,'obj3':mul,'obj4':div})