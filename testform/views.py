from django.shortcuts import render

# Create your views here.
def form(request):
    return render(request,template_name="form.html")
def response(request):
    data= request.GET
    return render(request,template_name="response.html", context=data)
    # get data from request(the data written in form)