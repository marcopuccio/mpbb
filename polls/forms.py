from django import forms


class CreateQuestionForm(forms.Form):
    """
    Creating Question with choices form.
    """
    question_text = forms.CharField(label='Question Text')
    first_choice = forms.CharField(label='First Choice', required=False)
    second_choice = forms.CharField(label='Second Choice', required=False)
    third_choice = forms.CharField(label='Third Choice', required=False)