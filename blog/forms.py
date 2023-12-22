from django import forms
from .models import Article




class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        # fields='__all__'  
        exclude=['view_count','author']

    def save(self,author):
        instance=super().save()
        instance.author=author
        instance.save()
        return instance