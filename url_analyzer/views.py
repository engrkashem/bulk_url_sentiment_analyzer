from django.shortcuts import render
from .forms import UrlSentimentForm

# Create your views here.


def url_sentiment_view(request):
    template = 'index.html'
    context = {}
    context['form'] = UrlSentimentForm()
    if request.method == 'GET':
        return render(request, template, context)
    elif request.method == 'POST':
        used_form = UrlSentimentForm(request.POST)
        if used_form.is_valid():
            url_obj = used_form.save()
            return render(request, template, context)
        context['errors'] = used_form.errors
        return render(request, template, context)
