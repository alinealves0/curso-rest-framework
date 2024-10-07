from django.contrib.auth import get_user_model #type:ignore
from rest_framework.permissions import IsAuthenticated #type:ignore
from rest_framework.viewsets import ReadOnlyModelViewSet #type:ignore


from ..serializers import AuthorSerializer #type:ignore

class AuthorViewSet(ReadOnlyModelViewSet):
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, ]
    def get_queryset(self):
        User = get_user_model()
        qs = User.objects.filter(username=self.request.user.username)
        return qs