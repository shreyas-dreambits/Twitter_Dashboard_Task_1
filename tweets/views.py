from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet


def tweets(request):
    search = Tweet.objects.all()
    context = {'tweet':search}
    return render(request, 'tweets.html', context)


def searchHashtags(request):
    # tweet_id = Tweet.objects.get(id=)

    search_query = ''

    if request.GET.get('search_query'):
        print('hello')
        search_query = request.GET.get('search_query')
        print(search_query)

    hashtag_search = Tweet.objects.filter(hashtag_name__icontains=search_query)

    print(hashtag_search)
    # print(request.POST['search'])

    context = {'hashtag_search1': hashtag_search}
    return render(request, 'tweets_data.html', context)


# def tweetWithdata(request):
    # context = {}
#     return render(request, 'tweets.html', context)

