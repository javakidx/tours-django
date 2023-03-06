class TourQuerysetMixin:
    user_field = 'tours'

    def get_queryset(self, *args, **kwargs):
        if hasattr(self.request, 'tour'):
            lookup_data = {self.user_field: self.request.tour}
        else:
            lookup_data = {}
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**lookup_data)
