from django.http import Http404

def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404