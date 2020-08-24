from django.shortcuts import render
from learning_logs.models import Topic, Poster

# Create your views here.
def index(request):
    """make view for homepage"""
    return render(request, 'learning_logs/index.html') #render(reqeust_obj, template)

def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_text):
    #show all entries for a single topic
    topic = Topic.objects.get(text=topic_text)
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'entries': entries,
        }
    return render(request, 'learning_logs/topic.html', context)

def poster(request,):
    context = {'url': Poster.get_url()}
    return render(request, 'learning_logs/topic.html', context)






