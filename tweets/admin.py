from django.contrib import admin

# Register your models here.
from .forms import TweetModelForm

from .models import Tweet

#admin.site.register(Tweet)

class TweetModelAdmin(admin.ModelAdmin):
    form = TweetModelForm
    #class Meta:
     #   model= Tweet
      #  form = TweetModelForm
admin.site.register(Tweet, TweetModelAdmin)


