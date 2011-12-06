from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.db.models import Count

from models import Chavales, Ramas , ChavalesForm, RamasForm

from django.template import RequestContext

def base_vars(request):
    "A context processor that provides 'version', and 'ramas_list'."
    return {
        'version': '3.0beta',
        'ramas_list': Ramas.objects.all(),
        'ramas_count': Chavales.objects.values('rama').annotate(Count('rama'))
    }

@login_required()
def index(request):
	return render_to_response('website/index.html', context_instance=RequestContext(request, processors=[base_vars]))
	
@login_required()
def export(request):
	return render_to_response('website/export.html', context_instance=RequestContext(request, processors=[base_vars]))

@login_required()
def view(request, _id):
	result = Chavales.objects.get(id=_id)
	form = ChavalesForm(result)
	return render_to_response('website/new.html', {'form': form}, context_instance=RequestContext(request, processors=[base_vars]))

@login_required()
def search(request, search_query):
	ramas = Ramas.objects.all()
	if ramas.filter(nombre=search_query):
		search_result = Chavales.objects.all().filter(rama=ramas.filter(nombre=search_query).values('id'))
	else:
		search_result = Chavales.objects.all().filter(nombre__contains=search_query)
	
	return render_to_response('website/search.html', {'search_result': search_result}, context_instance=RequestContext(request, processors=[base_vars]))

@login_required()
def new(request):
	
	if request.method == 'POST':
		form = ChavalesForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/new/')
	else:
		form = ChavalesForm()
	return render_to_response('website/new.html', {'form': form}, context_instance=RequestContext(request, processors=[base_vars]))

@login_required()
def ramas(request):
	return render_to_response('website/index.html', context_instance=RequestContext(request, processors=[base_vars]))
