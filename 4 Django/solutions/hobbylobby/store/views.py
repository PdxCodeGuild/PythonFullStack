from django.shortcuts import render
from django.http import HttpResponse


def list_products(request):
    return HttpResponse('list products')

def cart(request):
    return HttpResponse('cart')

def faq(request):
    return HttpResponse('faq')