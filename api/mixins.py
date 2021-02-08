from rest_framework import mixins, viewsets


class GetPostMixClasses(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet,
                        ):
    pass
