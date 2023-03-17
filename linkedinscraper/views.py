from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import LinkedinScraperLoginDetails, LinkedinScraper
from .scraper import url_scraper, bulk_url_scraper

@ensure_csrf_cookie
def scraper(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        email = data['email']
        password = data['password']
        """if LinkedinScraperLoginDetails.objects.filter(email=email).exists():
            return render(request, 'scraper.html', {'message': 'Email Id already exists!'})"""
        # LinkedinScraperLoginDetails.objects.create(email=email, password=password)
        if data['url']:
            details = url_scraper(email, password, data['url'])
            LinkedinScraper.objects.create(email=details[0], phone=details[1])
            return render(request, 'scraper.html', {'message': 'Contact details saved successfully!'})
        elif data['url_file']:
            with open(data['url_file'], 'r') as f:
                urls = f.readlines()
            for dt in bulk_url_scraper(email, password, urls):
                LinkedinScraper.objects.create(email=dt[0], phone=dt[1])
            return render(request, 'scraper.html', {'message': 'Contact details saved successfully!'})
    return render(request, 'scraper.html')
