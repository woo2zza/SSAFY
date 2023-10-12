from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Movie,Comment 
from django.contrib.auth.decorators import login_required
from .forms import MovieForm, CommentForm



# 전체 페이지
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)




@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit= False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk )
    else:
        form = MovieForm()
    
    context = {
        'form' : form
    }
    return render(request, 'movies/create.html', context)





@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie' : movie,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'movies/detail.html', context)




@require_POST
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == movie.user:
            movie.delete()
    return redirect('movies:index')



@login_required
@require_http_methods(['GET','POST'])
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance = movie)
    else:
        return redirect('movies:index')
    
    context = {
        'form' : form,
        'movie' : movie
    }

    return render(request, 'movies/update.html', context)
    




@login_required
def comments_create(request,pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit = False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
    return redirect('movies:detail', movie.pk)





@require_POST

def comments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)