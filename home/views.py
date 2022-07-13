from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.core import serializers

# Create your views here.

# 메인화면 뷰
from home.models import Standing
from join.models import Member


class HomeView(View):
    def get(self, request):
        form = request.GET.dict()
        sbs = Standing.objects.all()
        print(form)

        if (form != {}):
            stand = Standing.objects.get(rank=form['rank'])
        else:
            stand = Standing.objects.get(rank='1')

        context = {'sbs': sbs,
                   'rank': stand.rank,
                   'based': stand.based,
                   'team': stand.team,
                   'match': stand.match,
                   'wpoint': stand.wpoint,
                   'win': stand.win,
                   'draw': stand.draw,
                   'defeat': stand.defeat,
                   'goal': stand.goal,
                   'loss': stand.loss,
                   'gol': stand.gol,
                   }

        print(context)

        return render(request, 'index.html', context)

    def post(self, request):
        pass

# 로그인 뷰
class LoginView(View):
    def post(self, request):
        form = request.POST.dict()

        returnPage = '/loginfail'
        isExisted = Member.objects.filter(userid=form['muserid'], passwd=form['mpasswd']).exists()


        if isExisted:
            user = Member.objects.get(userid=form['muserid'])

            request.session['userinfo'] = form['muserid'] + '|' + str(user.id) + '|' + str(user.team)
            print(request.session['userinfo'])

            returnPage='/'

        return redirect(returnPage)


# 로그인 실패 뷰
class LoginfailView(View):
    def get(self, request):
        return render(request, 'loginfail.html')

# 로그아웃 뷰
class LogoutView(View):
    def get(self, request):
        request.session.flush()

        return redirect('/')

    def post(self, request):
        pass

# 사이트맵 뷰
class SitemapView(View):
    def get(self, request):
        return render(request, 'sitemap.html')

    def post(self, request):
        pass

# 마이페이지 뷰
class MypageView(View):
    def get(self, request):
        return render(request, 'mypage.html')

    def post(self, request):
        pass


class SearchIdView(View):
    def get(self, request):
        form = request.GET.dict()

        # 아이디를 찾기 위해 가입 때 입력한 이메일로 가입여부 조회

        # isExisted가 True면 DB에서 id를 찾아 context로 보내고, False면 error 내용을 context로 보낸다
        # m= Member.objects.select_related().get(email=form['email'])
        # context = {'member': m}
        # return render(request, 'layouts/modal.html', context)

        result= Member.objects.select_related().filter(email=form['email'])
        json_data = serializers.serialize('json', result)
        print(json_data, form['email'])


        return HttpResponse(json_data, content_type='application/json')


class StandingView(View):
    def get(self, request):
        form = request.GET.dict()
        sbs = Standing.objects.all()
        print(form)

        if (form != {}):
            stand = Standing.objects.get(rank=form['rank'])
        else:
            stand = Standing.objects.get(rank='1')


        context = {'sbs': sbs,
                   'rank': stand.rank,
                   'based': stand.based,
                   'team': stand.team,
                   'match': stand.match,
                   'wpoint': stand.wpoint,
                   'win': stand.win,
                   'draw': stand.draw,
                   'defeat': stand.defeat,
                   'goal': stand.goal,
                   'loss': stand.loss,
                   'gol': stand.gol,
                   }

        print(context)

        return render(request, 'index.html', context)