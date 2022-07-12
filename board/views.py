from django.shortcuts import render
from django.views import View

# Create your views here.

# Media->news 뷰
class NewsView(View):
    def get(self, request):
        return render(request, 'board/news.html')

    def post(self, request):
        pass

# Media->공지사항 뷰
class AnnounceView(View):
    def get(self, request):
        return render(request, 'board/announce.html')

    def post(self, request):
        pass

# Media->구단 뷰
class TeamPlayerView(View):
    def get(self, request):
        return render(request, 'board/teamplayer.html')

    def post(self, request):
        pass