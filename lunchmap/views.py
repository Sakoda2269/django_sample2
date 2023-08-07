from typing import Any
from django import http
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Category, Shop
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


#generic.ListViewで一覧を作れる
#テンプレート名を省略するとshop_list.htmlになる
class IndexView(generic.ListView):
    model = Shop


#shop_detail.html
class DetailView(generic.DetailView):
    model = Shop


#shop_form.html
class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Shop
    fields = ["name", "address", "category"]
    #"__all__"#すべてのカラムを入力できるフォーム


    def form_valid(self, form):
        form.instance.author = self.request.user#投稿者名をログインユーザーにする
        return super(CreateView, self).form_valid(form)


#shop_form.html
class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Shop
    fields = ["name", "address", "category"]


    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied("You don't have permission to edit.")
        return super(UpdateView, self).dispatch(request, *args, **kwargs)


#shop_confirm_delete.html
class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Shop
    success_url = reverse_lazy("lunchmap:index")#リダイレクト先を指定(汎用ビューではreverseではなくreverse_lazyを使う)