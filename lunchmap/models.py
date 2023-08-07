from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        "auth.User",
        on_delete = models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    author = models.ForeignKey(
        "auth.User",
        on_delete = models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    #リダイレクト先を指定
    def get_absolute_url(self):
        return reverse("lunchmap:detail", kwargs={"pk" : self.pk})