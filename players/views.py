from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from players.models import Records, Soccers
from teams.models import Stadiums
from django.core import serializers

# Create your views here.


# Player -> 선수1 감독 뷰


class CoachView(View):
    def get(self, request):
        form = request.GET.dict()
        tbs = Stadiums.objects.all()

        if (form != {}):
            pinfo = Soccers.objects.filter(team=form['team'])
        else:
            pinfo = Soccers.objects.filter(team='FC서울')

        print(pinfo)

        context = {'pinfo': pinfo, 'tbs': tbs}
        return render(request, 'players/coach1.html', context)

    def post(self, request):
        pass


# Player -> 기록/순위 뷰
class RecordView(View):
    def get(self, request):
        form = request.GET.dict()
        pbs = Records.objects.all()

        if (form != {}):
            player = Records.objects.get(name=form['name'])
        else:
            player = Records.objects.get(name='무고사')
            print(player)
        pbs = Records.objects.all()

        context = {'pbs': pbs,
                   'rank': player.rank,
                   'name': player.name,
                   'team': player.team,
                   'goal': player.goal,
                   'assist': player.assist,
                   'attackpoint': player.attackpoint,
                   'losspoint': player.losspoint,
                   'cornerkick': player.cornerkick,
                   'foul': player.foul,
                   'shoot': player.shoot,
                   'offside': player.offside,
                   'warning': player.warning,
                   'exit': player.exit,
                   'norun': player.norun,
                   'trip': player.trip,
                   'replace': player.replace,
                   'matchpoint': player.matchpoint,
                   }

        print(context)

        return render(request, 'players/record.html', context)



    def post(self, request):
        pass


class PlayerView(View):
    def get(self, request):
        form = request.GET.dict()
        print(form)
        player1 = Records.objects.get(rank = form['rank'])
        context = {'rank': player1.rank,
                   'name': player1.name,
                   'team': player1.team,
                   'goal': player1.goal,
                   'assist': player1.assist,
                   'attackpoint': player1.attackpoint,
                   'losspoint': player1.losspoint,
                   'cornerkick': player1.cornerkick,
                   'foul': player1.foul,
                   'shoot': player1.shoot,
                   'offside': player1.offside,
                   'warning': player1.warning,
                   'exit': player1.exit,
                   'norun': player1.norun,
                   'trip': player1.trip,
                   'replace': player1.replace,
                   'matchpoint': player1.matchpoint,}