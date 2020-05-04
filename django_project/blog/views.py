from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Post
from .models import Game
from .filter import GameFilter
import operator
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render



class RecommenderResultsView(ListView):
        model = Game
        template_name = 'game_results.html' #, 'game_info_page.html'
        paginate_by = 10

        def get_queryset(self):
             query = self.request.GET.get('q')
             object_list = Game.objects.filter(
                     Q(title__icontains = query) | Q(tags__icontains = query) | Q(genres__icontains = query)

             )
             return object_list  

        # def listing(self):
        #      game_list = Game.objects.all()
        #      paginator = Paginator(game_list, 10)
        #      page_number = self.GET.get('page')
        #      page_obj = paginator.get_page(page_number)
        #      return render (self, 'list.html', {'page_obj': page_obj})  
             

class GameInfoView(ListView):
    model = Game
    template_name = 'game_info_page.html'

    def get_gamequeryset(self):
     game_information = Game.objects.filter(
        Q(title__icontains = Game.title)

    )
     return game_information
        


# def home(request):
#     context = {
#         'Game': Game.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


class GameListView(ListView):
    model = Game
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'games'
    ordering = ['title']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def recommender(request):
    return render(request, 'blog/recommender.html', {'title': 'recommender'})

def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(content__icontains=query)

            results= Post.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'blog/recommender.html', context)

        else:
            return render(request, 'blog/recommender.html')

    else:
        return render(request, 'blog/recommender.html')





