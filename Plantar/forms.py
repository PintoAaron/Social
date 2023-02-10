from django import forms
from .models import Plant

class PlantForm(forms.ModelForm):
    body = forms.CharField(required=True,             
               widget=forms.widgets.Textarea(
                    attrs={"placeholder":"Enter your Plantar plants here",
                            "class":"form-control"}
                           ),
                           label= "",
               )
    
    class Meta:
        model = Plant 
        exclude = ("user",)
    
    
    