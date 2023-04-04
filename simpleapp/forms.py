from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .models import News1


class NewsForm(forms.ModelForm):

    class Meta:
        model = News1
        fields = ['title', 'content']

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get("content")
        title = cleaned_data.get("title")


        if title == content:
            raise ValidationError(
                "Content can not be the same as the title!"
            )

        if content is not None and len(content) < 20:
            raise ValidationError({
                "content":"Описание не может быть менее 20 символов."
            })

        return cleaned_data