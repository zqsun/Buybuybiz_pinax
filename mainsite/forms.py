from django import forms
from haystack.forms import SearchForm
from myaccount.models import bizCategory, bizGoal

class ProjectSearchForm(SearchForm):
	category = forms.ModelChoiceField(queryset=bizCategory.objects.all(),required=False,empty_label="All Categories")
	goal = forms.ModelChoiceField(queryset=bizGoal.objects.all(),required=False,empty_label="U.S./ Israel technologies")
	def serch(self):
		sqs = super(ProjectSearchForm, self).search()
		if not self.is_valid():
			return self.no_query_found()

		if self.cleaned_data['category']:
			sqs = sqs.filter(category=self.cleaned_data['category'])
		if self.cleaned_data['goal']:
			sqs = sqs.filter(goal=self.cleaned_data['goal'])
		return sqs

# class PartnerForm(forms.ModelForm):
# 	description = forms.CharField(widget=forms.Textarea)
# 	class Meta:
# 		model = Partners
# 		fields = ['name','company','title','description','picture']