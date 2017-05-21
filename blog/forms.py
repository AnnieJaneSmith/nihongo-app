from django import forms
from .models import Post
from quiz_app.models import Choice


# from pagedown.widgets import PagedownWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "image",
        ]


def get_choices():
    choices_list=Choice.objects.all()
    return choices_list

class ChoiceForm(forms.Form):
    def __init__(self,*args,**kwargs):
        super(ChoiceForm,self).__init__(*args,**kwargs)
        self.fields['choice_text']=forms.CharField(
            choices=get_choices()
        )
# class ChoiceForm(forms.Form):
#     choice_field = forms.ModelChoiceField(queryset=Choice.objects.all())
#
#     class Meta:
#         model = Choice
#         fields = ['choice_text']
