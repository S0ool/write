from math import ceil

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from app.models import Post, Category
import random


# Create your views here.

def index(request):
    print('hello')
    # cat = get_object_or_404(Category.objects.get(name='Спорт'))
    cat = Category.objects.get(name='Спорт')
    # post = Post(
    #     title='title 1',
    #     category=cat
    # )
    # post.save()
    # post = Post.objects.create(
    #     title='title 1',
    #     category=cat
    # )
    # post = Post.objects.get(id=1)
    # post, _ = Post.objects.get_or_create(title='title new 2', category=cat)
    # post, _ = Post.objects.get_or_create(title='title new 3', defaults={
    #     'category': cat,
    #     'description': 'description new'
    # })
    # post.description = 'description 1'
    # post, _ = Post.objects.update_or_create(title='title new 1', defaults={
    #     'category': cat,
    #     'content': 'content',
    #     'description': 'description new',
    #     'is_published': True
    # })
    # post.save()
    # print(post)

    # data = [
    #     Post(title='title 5', category=cat),
    #     Post(title='title 6', category=cat),
    #     Post(title='title 7', category=cat),
    #     Post(title='title 8', category=cat),
    # ]
    # data = [
    #     {
    #
    #         'title': 'title 4',
    #         'category': cat
    #     },
    #     {
    #
    #         'title': 'title 5',
    #         'category': cat
    #     }
    # ]
    # data = list(map(lambda i: Post(**i), data))
    # Post.objects.bulk_create(data)
    return HttpResponse('success')


def posts(request):
    data = Post.objects.order_by('-title').all()  # - чтобы сортировалось по убыванию
    colors = ['red', 'purple', 'orange', 'yellow', 'blue', 'lime', 'grey', 'black']
    color = random.choice(colors)
    ctx = {
        'data': data,
        'color': color
    }
    return render(request, 'app/index.html', context=ctx)


def post_info(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    ctx = {
        'post': post
    }
    return render(request, 'app/post_info.html', context=ctx)


def post_id(request):
    posts = Post.objects.all()
    for post in posts:
        post.title = post.title + str(post.id)
        print(post.title)
        post.save()

    return redirect('main')


def delete_posts(request):
    posts = Post.objects.all()

    for post in posts:
        for symbol in post.title:
            if symbol.isnumeric():
                if int(symbol) % 2 != 0:
                    print(post)
                    post.delete()
                    break
    return redirect('main')


def add_posts(request):
    categories = Category.objects.all()
    if len(categories) == 0:
        raise Http404("Нет категорий")
    length = 10
    divide = length / len(categories)
    for i in range(length):
        post = Post(
            title=f'title {i}',
            content=f'content {i}',
            description=f'description {i}',
            category=categories[int(i // divide)],
            status='public'
        )
        post.save()
    return redirect('main')
