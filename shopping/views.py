from django.shortcuts import render
from django.views import View

# Create your views here.
from shopping.models import Shopping


class ShopView(View):
    def get(self, request):
        form = request.GET.dict()
        tbs = Shopping.objects.all()


        if (form != {}):
            team = Shopping.objects.get(based=form['based'])
        else:
            team = Shopping.objects.get(based='서울')

        context = {'tbs': tbs,
                   'based': team.based,
                   'hteam': team.hteam,
                   'url' : team.url
                   }

        return render(request, 'shop.html/', context)



    def post(self, request):
        pass