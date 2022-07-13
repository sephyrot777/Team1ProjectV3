from django.shortcuts import render
from django.views import View

# Create your views here.

# Media->news 뷰
class PrivacyView(View):
    def get(self, request):
        return render(request, 'policy/privacy.html')

    def post(self, request):
        pass


class ServiceView(View):
    def get(self, request):
        return render(request, 'policy/service.html')

    def post(self, request):
        pass