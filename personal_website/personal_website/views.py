"""Views for personal_website."""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home View."""

    template_name = 'personal_website/home.html'

    def get_context_data(self):
        """Get the posts of all users followed by logged in user."""
        return {}
