from django.shortcuts import render, redirect
from django.views import View

# Create your views here.

# 메인화면 뷰
from join.models import Member


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

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