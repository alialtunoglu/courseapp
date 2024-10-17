from django.shortcuts import render
from django.http import HttpResponse


def kurslar(request):
    return HttpResponse('kurs listesi')
def details(request):
    return HttpResponse('kurs detay sayfası')
def programlama(request):
    return HttpResponse('programlama kurs listesi')
def mobiluygulamalar(request):
    return HttpResponse('mobil uygulamalar kurs listesi')