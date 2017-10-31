from django.shortcuts import render
from .models import Video, Concert, Band, News
from datetime import datetime

# Create your views here.
def index(request):
	template_name='index.html'
	news=News.objects.all().order_by('-id')[:3]
	concerts=Concert.objects.all().order_by('date').filter(date__gte=datetime.today())[:5]
	videos=Video.objects.all().order_by('-id')[:1]
	return render(request, template_name,locals())

def news(request):
	template_name='news/index.html'
	rows=News.objects.all().order_by('-id')
	context=dict(
			rows=rows,
		)
	return render(request, template_name, context)


def videos(request):
	template_name='videos/index.html'
	rows=Video.objects.all().order_by('-id')
	context=dict(
			rows=rows,
		)
	return render(request, template_name,context)

def concerts(request):
	template_name='concerts/index.html'
	rows=Concert.objects.all().order_by('date').filter(date__gte=datetime.today())
	context=dict(
			rows=rows,
		)
	return render(request, template_name,context)


def all_concerts(request):
	print(request.path=='/all-concerts/' )
	template_name='concerts/index.html'
	rows=Concert.objects.all().order_by('date')
	context=dict(
			rows=rows,
		)
	return render(request, template_name,context)


def detail_concerts(request,pk):
    template_name = 'concerts/detail.html'
    rows = Concert.objects.filter(pk=pk)
    context = {'rows' : rows}
    return render(request, template_name, context)


def about(request):
	template_name='about/index.html'
	rows=Band.objects.filter(active=True)
	past_members=Band.objects.filter(active=False)
	context=dict(
			rows=rows,
			past_members=past_members,
		)
	return render(request, template_name,context)