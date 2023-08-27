from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

class NotFoundView(TemplateView):
    template_name = "404.html"

class Home(View):
      def get(self, request, *args, **kwargs):
          return render(request, 'index.html')
