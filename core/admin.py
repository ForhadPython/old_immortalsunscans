from django.contrib import admin
from .models import article, chapter, ChapterImage


# Register your models here.

class CapterInline(admin.TabularInline):
    model = chapter
    extra = 0


class articleModel(admin.ModelAdmin):
    list_display = ["__str__", "posted_on"]
    search_fields = ["__str__", "details"]
    list_per_page = 10
    list_filter = ["posted_on"]
    inlines = [CapterInline]

    class Meta:
        Model = article


admin.site.register(article, articleModel)


class CapterImageInline(admin.TabularInline):
    model = ChapterImage
    extra = 0


class chapterModel(admin.ModelAdmin):
    list_display = ["__str__"]
    inlines = [CapterImageInline]
    search_fields = ["__str__"]

    class Meta:
        Model = chapter


admin.site.register(chapter, chapterModel)
