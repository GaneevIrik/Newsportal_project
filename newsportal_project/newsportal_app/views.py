from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostF
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin                    #модуль D5.6



class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context



class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class SearchPost(ListView):
    model = Post
    template_name = 'search.html'
    ordering = 'title'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(PermissionRequiredMixin, CreateView):               # было LoginRequiredMixin,  модуль D5.6
    #raise_exception = True                                         #модуль D5.6
    permission_required = ('newsportal_app.add_post')               #модуль D5.6
    form_class = PostF
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.postCategory = 'NW'
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):              # было LoginRequiredMixin,  модуль D5.6
    permission_required = ('newsportal_app.change_post',)            #модуль D5.6
    form_class = PostF
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.postCategory = 'NW'
        return super().form_valid(form)


class PostDelete(PermissionRequiredMixin, DeleteView):                   # было LoginRequiredMixin,  модуль D5.6
    permission_required = ('newsportal_app.delete_post',)                #модуль D5.6
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.postCategory = 'NW'
        return super().form_valid(form)


class ArticleCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PostF
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.postCategory = 'AR'
        return super().form_valid(form)


class ArticleUpdate(UpdateView):
    form_class = PostF
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.postCategory = 'AR'
        return super().form_valid(form)

class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.postCategory = 'AR'
        return super().form_valid(form)

