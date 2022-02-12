from django import forms


class AnswerForm(forms.Form):
    answer = forms.CharField(label='answer', \
        widget=forms.TextInput(attrs={'class':'form-control'}))