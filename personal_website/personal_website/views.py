"""Views for personal_website."""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home View."""

    template_name = 'personal_website/home.html'

    def get_context_data(self):
        """Get context data."""
        return {}


class AboutView(TemplateView):
    """Home View."""

    template_name = 'personal_website/about.html'

    def get_context_data(self):
        """Get context data."""
        return {}


class ContactView(TemplateView):
    """Contact View."""

    template_name = 'personal_website/contact.html'

    def get_context_data(self):
        """Get context data."""
        return {}
