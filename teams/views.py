from django.shortcuts import render, redirect
from django.views import View
from teams.models import Stadiums


# Create your views here.


class TeamsView(View):
    def get(self, request):
        form = request.GET.dict()
        tbs = Stadiums.objects.all()

        if (form != {}):
            team = Stadiums.objects.get(based=form['based'])
        else:
            team = Stadiums.objects.get(based='서울')
            print(team)

        context = {'tbs': tbs,
                   'stname': team.stname,
                   'opdate': team.opdate,
                   'based': team.based,
                   'hteam': team.hteam,
                   'accnum': format(team.accnum, ','),
                   'addr': team.location,
                   'addrstmp': team.addrstmp,
                   'addrkey': team.addrkey,
                   }

        print(context)

        return render(request, 'teams/stadium.html', context)
