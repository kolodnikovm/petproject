from django.shortcuts import render
from django.views.generic import View


class Index(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'core/index.html')
