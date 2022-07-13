from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
import requests
import json
# Create your views here.


# 이용약관 동의 뷰
from join.models import Member


class AgreeView(View):
    def get(self, request):
        return render(request, 'join/agree.html')

    def post(self, request):
        pass

# 본인확인 뷰
class CheckmeView(View):
    def get(self, request):
        return render(request, 'join/checkme.html')

    def post(self, request):
        SECRET_KEY = '6Lfc8qYgAAAAADTeEg2dB6tlHI25bUH3WiVuz0p2'
        VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'
        form = request.POST.dict()

        params = {'secret': SECRET_KEY, 'response': form['g-recaptcha']}

        result = requests.get(VERIFY_URL, params=params).json()


        # 생일 yyyy-mm-dd로 표현하기 위해 주민번호에서 자르기
        birth = form['birth']
        gender = int(form['gender'])
        # print(gender)
        birth_long=''
        birth_split = [birth[i:i + 2] for i in range(0, len(birth), 2)]
        # print(birth_split)

        if gender == 1 or gender == 2:
            birth_long='19'+birth_split[0]+'-'+birth_split[1]+'-'+birth_split[2]
        elif gender == 3 or gender == 4:
            birth_long='20'+birth_split[0]+'-'+birth_split[1]+'-'+birth_split[2]
        print(birth_long)

        # 성별 한글로
        if gender == 1 or gender == 3:
            gender_ko='남자'
        elif gender == 2 or gender == 4:
            gender_ko='여자'
        else:
            gender_ko='none'

        # tokens에 이름, 생일, 성별, 휴대폰번호 저장
        if result['success']:
            tokens = {'name': form['name'],
                      'birth': birth_long,
                      'gender': gender_ko,
                      'phone': form['phone']}

            tokens = json.dumps(tokens, ensure_ascii=True)
            print(tokens)

            res = redirect('/join/joinme')
            res.set_cookie('tokens',tokens, max_age=60*30)
            return res
        else:
            error='자동가입방지 인증이 실패했습니다'

        context = {'form': form, 'error': error}
        return render(request, 'join/checkme.html', context)

# 정보기입 뷰
class JoinmeView(View):
    def get(self, request):
        cookie = request.COOKIES.get('tokens')
        try:
            return render(request, 'join/joinme.html', eval(cookie))
        except:
            return redirect('/join/agree')

    def post(self, request):
        form = request.POST.dict()
        print(form)

        email = form['email1'] + '@' + form['email2']
        mailing = True if form['mailing'] == 'yes' else False
        addr = form['addr1'] + form['addr3'] + ' ' + form['addr2']

        m = Member(userid=form['userid'],
                   passwd=form['passwd'],
                   nickname=form['nickname'],
                   team=form['team'],
                   name=form['name'],
                   birth=form['birth'],
                   phone=form['phone'],
                   zipcode=form['zipcode'],
                   addr=addr,
                   email=email,
                   mailing=mailing)
        m.save()

        return redirect('/join/joinok?userid=' + form['userid'])


# 가입완료 뷰
class JoinokView(View):
    def get(self, request):
        form = request.GET.dict()
        m=Member.objects.select_related().get(userid=form['userid'])

        context = {'member': m}
        return render(request, 'join/joinok.html', context)

    def post(self, request):
        pass

# 회원가입관련 뷰
class UseridView(View):
    def get(self, request):
        form = request.GET.dict()

        # select count(*) from member where userid = ?
        count = Member.objects.filter(userid=form['userid']).count()
        # print(count)

        json_data = {'count': count}
        # print(json_data)

        return HttpResponse(json.dumps(json_data), content_type='application/json')

    def post(self, request):
        pass
