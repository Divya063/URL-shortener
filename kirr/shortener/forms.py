from django import forms
from django.core.validators import URLValidator

class SubmitUrlForm(forms.Form):
    url=forms.CharField(label="submit url")
    def clean(self): # for forms
        cleaned_data=super(SubmitUrlForm,self).clean()
        url=cleaned_data.get("url")
        print(url)
    def clean_url(self): #for fields
        url=self.cleaned_data["url"]
        print(url)
        url_validator=URLValidator()
        try:
            url_validator(url)
        except:
             raise forms.ValidationError("Invalid URL")
        return(url)