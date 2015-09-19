from django.shortcuts import render,render_to_response
from django.template import RequestContext
from haystack.generic_views import SearchView
from mainsite.forms import ProjectSearchForm

from myaccount.models import bizCategory, bizGoal, bizProject, projectPic

from haystack.forms import ModelSearchForm
from haystack.query import EmptySearchQuerySet, SearchQuerySet

# Create your views here.
# View class
class mySearchView(SearchView):
	form_class = ProjectSearchForm
	def create_response(self):
		"""
		Generates the actu HttpResponse to send back to the user.
		"""
		(paginator, page) = self.build_page()

		context = {
			'query': self.query,
			'form': self.form,
			
			'page': page,
            'paginator': paginator,
			'suggestion': None,
			'results': self.results,
		}

		if self.results and hasattr(self.results,'query') and self.results.query.backend.include_spelling:
			context['suggestion'] = self.form.get_suggestion()

		context.update(self.extra_context())
		return render_to_response(self.template, context, context_instance=self.context_class(self.request))

# Search view
def my_basic_search(request, template='search/search.html', load_all=True, form_class=ModelSearchForm, searchqueryset=None, context_class=RequestContext, extra_context=None, results_per_page=None):
    """
    A more traditional view that also demonstrate an alternative
    way to use Haystack.
    Useful as an example of for basing heavily custom views off of.
    Also has the benefit of thread-safety, which the ``SearchView`` class may
    not be.
    Template:: ``search/search.html``
    Context::
        * form
          An instance of the ``form_class``. (default: ``ModelSearchForm``)
        * page
          The current page of search results.
        * paginator
          A paginator instance for the results.
        * query
          The query received by the form.
    """
    query = ''
    results = EmptySearchQuerySet()
    form_class = ProjectSearchForm

    if request.GET.get('q'):
        form = form_class(request.GET, searchqueryset=searchqueryset, load_all=load_all)

        if form.is_valid():
            query = form.cleaned_data['q']
            results = form.search()
    else:
        form = form_class(searchqueryset=searchqueryset, load_all=load_all)

    # paginator = Paginator(results, results_per_page or RESULTS_PER_PAGE)

    # try:
    #     page = paginator.page(int(request.GET.get('page', 1)))
    # except InvalidPage:
    #     raise Http404("No such page of results!")

    context = {
        'form': form,
        # 'page': page,
        # 'paginator': paginator,
        'results':results,
        'query': query,
        'suggestion': None,
    }

    if results.query.backend.include_spelling:
        context['suggestion'] = form.get_suggestion()

    if extra_context:
        context.update(extra_context)

    return render_to_response(template, context, context_instance=context_class(request))

def viewProject(request,project_id):
	p = bizProject.objects.get(pk=project_id)
	try:
		pic = projectPic.objects.get(project_id = p)
	except projectPic.DoesNotExist:
		pic = None
	context = {'project':p,'pic':pic}
	return render(request, 'mainsite/viewProject.html', context)

def browseProject(request,category_name):
    if category_name == "ALL":
        results = bizProject.objects.order_by('-updated_at').all()
    else:
        results = bizProject.objects.filter(category__category__contains=category_name).order_by('-updated_at')
    project_form = ProjectSearchForm()
    context = {'results':results,'form':project_form,'category':category_name}
    return render(request, 'mainsite/browseProject.html', context)

