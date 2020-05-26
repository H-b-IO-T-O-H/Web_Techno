from django import forms


class QuestionForm(forms.Form):
	title = forms.CharField(label='Title', max_length=255)
	text = forms.CharField(label='Your question', widget=forms.Textarea(attrs={'rows': '3'}))
	tags = forms.CharField(label="Tags", required=False, max_length=50)

	def clean_tags(self):
		tags = self.cleaned_data['tags']
		if tags:
			tags.split()
		return tags

	def clean_text(self):
		text = self.cleaned_data['text']
		return text

	def clean_title(self):
		title = self.cleaned_data['title']
		return title


class AnswerForm(forms.Form):
	text = forms.CharField(label='Your answer', widget=forms.Textarea(attrs={'rows': '3'}))

	def clean(self):
		return self.cleaned_data
