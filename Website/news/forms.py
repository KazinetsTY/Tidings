from django import forms


class NewsForm(forms.Form):
    section = forms.CharField(label="Раздел")
    header = forms.CharField(label="Заголовок статьи", required=False)
    article = forms.CharField(label="Текст статьи", required=False)
