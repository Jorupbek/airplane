from django.views.generic import TemplateView

from flight.models import Flight


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['flight_lists'] = Flight.objects.all()

        return context
