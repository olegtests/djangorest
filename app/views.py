from django.db.models import Count, Q
from django.http import HttpResponse
from requests import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from app.models import Post, Reaction
from app.serializers import PostSerializer, ReactionSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]

    @action(methods=['post'], detail=True)
    def react(self, request, pk=None):
        """upvote or downvote post, make the necessary logical checks"""

        post = self.get_object()
        serializer = ReactionSerializer(data=request.data, user=request.user, post=post)

        # serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False)
    def top(self, request):
        """Get list of top posts"""

        likes = Count('reaction', filter=Q(reaction__reaction=Reaction.UPVOTE))
        top_posts = Post.objects.annotate(likes=likes).order_by('-created')
        serializer = self.get_serializer(top_posts, many=True)

        page = self.paginate_queryset(top_posts)
        if page is not None:
            return self.get_paginated_response(serializer.data)

        return HttpResponse(serializer.data)
