from django.shortcuts import render
from partners.models import Partners
# Create your views here.
def BrowsePartners(request):
    partners = Partners.objects.all()
    context = {'partners':partners}
    return render(request,'partners/browse.html',context)