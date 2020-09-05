from django.db import models


class article(models.Model):
    author=models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.FileField()
    alternative = models.CharField(max_length=300)
    status = models.CharField(max_length=200, blank=True, null=True)
    genres = models.CharField(max_length=200, blank=True, null=True)
    view = models.CharField(max_length=200, blank=True, null=True)
    rating = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


class chapter(models.Model):
    article = models.ForeignKey(article, on_delete=models.CASCADE)
    chapter_number=models.IntegerField(default=0)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{} : {}".format(self.article.title, self.name)


class ChapterImage(models.Model):
    chapter_obj = models.ForeignKey(chapter, on_delete=models.CASCADE)
    image = models.FileField()

    def __str__(self):
        return "{}".format(self.chapter_obj.name)



