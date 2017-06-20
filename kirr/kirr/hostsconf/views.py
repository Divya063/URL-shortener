from django.http import HttpResponseRedirect
from django.conf import settings

Default_Redirect_Url = getattr(settings,"Default_Redirect_Url","http://www.kirr.com:8000")

def wildcard_redirect(request,path=None):
    new_url=Default_Redirect_Url
    if path is not None:
        new_url=Default_Redirect_Url+"/"+path
    return HttpResponseRedirect(new_url)

