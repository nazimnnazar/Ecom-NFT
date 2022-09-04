from math import prod
from django.shortcuts import render,get_object_or_404
from.models import*
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# home.html
def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=products.objects.filter(category=c_page,available=True)
    else:
        prodt=products.objects.all().filter(available=True)
    cat=categ.objects.all()
    paginator=Paginator(prodt,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request, 'home.html',{'pr':prodt,'ct':cat,'pg':pro})

# view.html 
def ProdDetails(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
       raise

    return render(request,'view.html',{'pr':prod})

# search.html
def  SearChing(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})