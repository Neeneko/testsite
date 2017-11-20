from django import forms

class LoginForm(forms.Form):
    author_name = forms.CharField(label='Author Name', max_length=100)

class LogoutForm(forms.Form):
    pass

class CreateTopicForm(forms.Form):
    topic_name = forms.CharField(label='Topic Name', max_length=100)
    topic_desc = forms.CharField(label='Topic Desc',widget=forms.TextInput)

class CreateCommentForm(forms.Form):
    text = forms.CharField(label='New Comment')
