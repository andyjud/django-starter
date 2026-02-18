from django import forms
from a_messageboard.models import Message


class MessageCreateForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["body"]
        widgets = {
            "body": forms.TextInput(attrs={
                "placeholder": "Drop your message  📩",
                "maxlength": 2000,
                "class": "p-4 text-black",
                "autocomplete": "off",
                "rows": 5
            })
        }

