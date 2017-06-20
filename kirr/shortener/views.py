from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from .models import KirrURL
from .forms import SubmitUrlForm

# Create your views here.
def kirr_redirect_view(request, shortcode=None, *args,**kwargs): #function based view
    #obj=KirrURL.objects.get(shortcode=shortcode)
    #obj_url=None
   # qs=KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
   # if qs.exists() and qs.count==1:
       # obj=qs.first()
       # obj_url=obj.url
    obj=get_object_or_404(KirrURL,shortcode=shortcode)
    obj_url=obj.url

    return HttpResponseRedirect(obj_url)
class HomeView(View):
    def get(self,request, *args, **kwargs):
        the_form=SubmitUrlForm()
        context={
            "title":"Kirr.co",
            "form": the_form
        }
        return render(request, "shortener/home.html", context)


    def post(self,request, *args, **kwargs):
        form=SubmitUrlForm(request.POST)
        context = {
            "title": "Kirr.co",
            "form": form
        }
        template="shortener/home.html"
        if form.is_valid():
            new_url=form.cleaned_data.get("url")
            obj,created=KirrURL.objects.get_or_create(url=new_url)
            context={
                "object":obj,
                "created":created,
            }
            if created:
                template="shortener/success.html"
            else:
                template="shortener/already-exists.html"


        return render(request, template ,context)

class KirrCbView(View):
    def get(self,request, shortcode=None,*args,**kwargs):
        # obj_url=obj.url
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        obj_url = obj.url

        return HttpResponseRedirect(obj_url)

    def post(self, request,  *args, **kwargs):
        return HttpResponse()
