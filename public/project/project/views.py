from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView

from photologue.models import Photo


class IndexView(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        try:
            photos = Photo.objects.all()
        except ObjectDoesNotExist as e:
            photos = None

        return self.render_to_response(
            self.get_context_data(
                request=self.request,
                photos=photos,
            )
        )
