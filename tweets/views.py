from django.shortcuts import render,get_object_or_404
from .models import Tweet
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .forms import TweetModelForm
from django.urls import reverse_lazy

# Create your views here.
class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create/'


#Update
class TweetUpdateView(UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = '/tweet/update/'


#Delete
class TweetDeleteView(DeleteView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/delete_confirm.html'
    model = Tweet
    success_url = reverse_lazy('author-list')



def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user= request.user
        instance.save()
        context = {
            'form':form
        }
        return render(request, 'tweets/create_view.html', context)



class TweetDetailView(DetailView):
    #template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()
    '''def get_object(self):
        pk=self.kwargs.get("pk")
        obj = get_object_or_404(Tweet, pk=pk)
        return obj'''

class TweetListView(ListView):
    #template_name = "tweets/ist_view.html"
    queryset = Tweet.objects.all()
    def get_context_dat(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        #context['another_list']=Tweet.objects.all()
        return context





'''def tweet_detail_view(request, pk=None):
    obj = Tweet.objects.get(pk=pk)
    print(obj)
    context = {
        'object':obj
    }
    return render(request, "detail_view.html", context)


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    print(queryset)
    for obj in queryset:
        print(obj.content)
    context = {
        'object_list': queryset
    }
    return render(request, "list_view.html", context)'''


