from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

from project.models import Project
from project.forms import CreateProjectForm, UpdateProjectForm
from account.models import Account


def create_project_view(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = CreateProjectForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		account = Account.objects.filter(email=user.email).first()
		obj.owner = account
		obj.save()
		form = CreateProjectForm()

	context['form'] = form

	return render(request, "project/create_project.html", context)


def detail_project_view(request, slug):

	context = {}

	project = get_object_or_404(Project, slug=slug)
	context['project'] = project

	return render(request, 'project/detail_project.html', context)



def edit_project_view(request, slug):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("must_authenticate")

	project = get_object_or_404(Project, slug=slug)

	if project.owner != user:
		return HttpResponse('You are not the owner of that project.')

	if request.POST:
		form = UpdateProjectForm(request.POST or None, instance=project)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			project = obj

	form = UpdateProjectForm(
			initial = {
					"title": project.title,
					"body": project.summary,
			}
		)

	context['form'] = form
	return render(request, 'project/edit_project.html', context)


def get_project_queryset(query=None):
	queryset = []
	queries = query.split(" ") # python install 2019 = [python, install, 2019]
	for q in queries:
		posts = Project.objects.filter(
				Q(title__icontains=q) | 
				Q(summary__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))	