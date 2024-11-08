from django.forms import ModelForm, TextInput, Textarea
from courses.models import Course


'''
class CourseCreateForm(forms.Form):

    title = forms.CharField(
        label = "Kurs Başlığı", 
        error_messages={
        "required":"Kurs Başlığı girmelisiniz"},
        widget = forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    imageUrl = forms.CharField(widget = forms.TextInput(attrs={"class": "form-control"}))
    slug = forms.SlugField(widget = forms.TextInput(attrs={"class": "form-control"}))
    #isActive = forms.BooleanField(label="isActive",required=False)
    #isHome = forms.BooleanField(label="isHome",required=False)
 '''   

class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields=["title", "description","imageUrl","slug" ,]  
        labels={
            'title':"Kurs Başlığı",
            'description':'Kurs Açıklaması'
        }

        widgets={
            "title":TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "imageUrl": TextInput(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"})
        }
        
        error_messages={
            'title': {
                "required":"Kurs Başlığı girmelisiniz",
                "max_length" : "Maksimum 50 Karakter Girmelisiniz"
            },
            'description': {
                "required":"Kurs açıklaması girmelisiniz",

            }
        }
    