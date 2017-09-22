from django.shortcuts import render
from django.template  import Template, Context, RequestContext
from django.shortcuts import render, render_to_response, redirect, get_object_or_404


def index(request):
    return render_to_response('index.html')