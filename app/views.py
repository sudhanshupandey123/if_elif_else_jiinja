from django.shortcuts import render

# Create your views here.
def if_elif_else(request):
    d={'name':'Sudhanshu Pandey','marks':92}
    return render(request,'if_elif_else.html',context=d)