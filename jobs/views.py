from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def portfolio(request):
    jobs = Job.objects
    return render(request, 'jobs/portfolio.html', {'jobs': jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail})

def index(request):
    return render(request, 'jobs/index.html')

def header(request):
    return render(request, 'jobs/header.html')

def footer(request):
    return render(request, 'jobs/footer.html')

def base(request):
    return render(request, 'jobs/base.html')

def about(request):
    return render(request, 'jobs/about.html')

def contact(request):
    return render(request, 'jobs/contact.html')

def index(request):
    images = [
        "1.png",
        "5.png",
        "6.png",
        "13.png",
        "14.png",
        "15.png",
    ]
    return render(request, "jobs/index.html", {"images": images})
