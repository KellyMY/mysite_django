from django.http import HttpResponse
from django.views import generic

class PostView(generic):
    def get(self, request,*arg,**kwargs):
        return HttpResponse("Hello World!")