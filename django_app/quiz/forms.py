from django import forms

class QuizSelect(forms.Form):
    select = forms.IntegerField(label='問題選択')


class AnswerForm(forms.Form):
    answer = forms.CharField(label='回答', \
        widget=forms.TextInput(attrs={'class':'form-control'}))