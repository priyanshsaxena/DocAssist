from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response

# Create your views here.

from .models import Disease
from .models import Material
from .forms import SearchForm

# Create your views here.
def index(request):
    top_diseases_list = []
    context = {
        'top_diseases_list': 2,
    }
    return render(request, 'index.html', context)    

def disease(request):
    import nehatest as nt
    import addnewdisease as ad
    import csv
    symptoms = "uncoordination,fever,dysuria"
    nt.parse_string(symptoms)
    file = open("/var/www/html/out.csv","r")
    top_diseases_list = []
    lines = csv.reader(file)
    for line in lines:
        top_diseases_list.append([line[0],float(line[1])])

    x = []
    for i in top_diseases_list:
        x.append(str(i[0]+','+str(i[1])))
    x = ";".join(x)
    context = {
    	'top_diseases_list': x,
    }
    return render(request, 'disease.html', context)

def training(request):
    top_diseases_list = Disease.objects.order_by('disease_probability')[:4]
    context = {
        'top_diseases_list': top_diseases_list,
    }
    return render(request, 'training.html', context)

def newdata(request):
    top_diseases_list = Disease.objects.order_by('disease_probability')[:4]
    context = {
        'top_diseases_list': top_diseases_list,
    }
    return render(request, 'newdata.html', context)

def get_query(request):
    return Http404()


def search(request):
    if request.method=='POST':
        query = request.POST.get('q')
        print "inside search", query
        import search
        results = search.main(query)
        print results
        return render(request, 'search.html', {'results': results })
    else:
        form = SearchForm(request)
        return render(request, 'search.html', {'form': form})