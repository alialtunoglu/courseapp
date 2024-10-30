from datetime import date,datetime
from django.shortcuts import get_object_or_404, render
from .models import Course,Category
from django.core.paginator import Paginator

 
# http://127.0.0.1:8000/kurslar
def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()

    
    paginator = Paginator(kurslar, 3)
    page = request.GET.get('page',1)
    page_obj= paginator.page(page)


    return render(request,'courses/index.html', {
         'categories':kategoriler,
         'page_obj':page_obj,
    })  

def details(request,slug): 
     #    try:
     #      course = Course.objects.get(pk=kurs_id) 
     #    except:
     #        raise Http404()

     course = get_object_or_404(Course,slug=slug)     
     context = {
          'course':course
     }
     return render(request,'courses/details.html',context)

def getCoursesByCategory(request,slug):
    kurslar = Course.objects.filter(categories__slug=slug,isActive=1).order_by("date")
    kategoriler = Category.objects.all()
    
    paginator = Paginator(kurslar, 3)
    page = request.GET.get('page',1)
    page_obj= paginator.page(page)

    print(page_obj.paginator.count) 
    print(page_obj.paginator.num_pages)
    print(page_obj.object_list)
    return render(request,'courses/index.html', {
         'categories':kategoriler,
         'page_obj':page_obj,
         'seciliKategori':slug
    })  
    