from django import forms

from project.models import Project, Sample, Seq


class CreateProjectForm(forms.ModelForm):

	class Meta:
		model = Project
		fields = ['title', 'summary']


class UpdateProjectForm(forms.ModelForm):

	class Meta:
		model = Project
		fields = ['title', 'summary']

	def save(self, commit=True):
		project = self.instance
		project.title = self.cleaned_data['title']
		project.summary = self.cleaned_data['summary']

		if commit:
			project.save()
		return project

class CreateSampleForm(forms.ModelForm):

	class Meta:
		model = Sample
		fields = ['title', 'organism']


class UpdateSampleForm(forms.ModelForm):

	class Meta:
		model = Sample
		fields = ['title', 'organism']

	def save(self, commit=True):
		sample = self.instance
		sample.title = self.cleaned_data['title']
		sample.summary = self.cleaned_data['organism']

		if commit:
			sample.save()
		return sample


class CreateSeqForm(forms.ModelForm):

	class Meta:
		model = Seq
		fields = ['title', 'instrument', 'strategy', 'source', 'layout', 'seqfile']


class UpdateSeqForm(forms.ModelForm):

	class Meta:
		model = Seq
		fields = ['title', 'instrument', 'strategy', 'source', 'layout', 'seqfile']

	def save(self, commit=True):
		seq = self.instance
		seq.title = self.cleaned_data['title']
		seq.instrument = self.cleaned_data['instrument']
		seq.strategy = self.cleaned_data['strategy']
		seq.source = self.cleaned_data['source']
		seq.layout = self.cleaned_data['layout']
		seq.seqfile = self.cleaned_data['seqfile']

		if commit:
			sew.save()
		return seq
