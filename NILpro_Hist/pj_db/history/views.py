# ListViewとDetailViewを取り込み
from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render

# ListViewは一覧を簡単に作るためのView
class Index(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = Post
#Post全てではなくあるカテゴリーだけを一覧したい場合、希望のpostをfilterして検索できる
    def get_queryset(self):
        return Post.objects.filter()

# DetailViewは詳細を簡単に作るためのView
class Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    model = Post

from django.views.generic.edit import CreateView

# CreateViewは新規作成画面を簡単に作るためのView
class Create(CreateView):
    model = Post
    
    # 編集対象にするフィールド
    fields = ["title", "body", "category", "tags"]

from django.views.generic.edit import UpdateView

class Update(UpdateView):
    model = Post
    fields = ["title", "body", "category", "tags"]

from django.views.generic.edit import DeleteView

class Delete(DeleteView):
    model = Post
    
    # 削除したあとに移動する先（トップページ）
    success_url = "/"

def top(request):
    return render(request, 'history/top.html') 