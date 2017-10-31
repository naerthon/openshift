from django.contrib import admin
from .models import Band, Concert, Video, News
from django.db 		import models


# Register your models here.
class BandAdmin(admin.ModelAdmin):
    fields = ('name', 'avatar_thumbnail', 'function', 'birth_date','description','active',)

class ConcertAdmin(admin.ModelAdmin):
    fields = ('title', 'local', 'date','cartaz_thumbnail','localization')

class VideoAdmin(admin.ModelAdmin):
    fields = ('title', 'url', 'created_date', 'published_date')

class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'news_thumbnail', 'created_date', 'published_date')


admin.site.register(Band, BandAdmin)
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(News, NewsAdmin)