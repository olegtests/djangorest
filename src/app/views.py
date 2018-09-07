from django.db.models import Count, Q
from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from src.app.models import Post, Reaction
from src.app.serializers import PostSerializer, ReactionSerializer


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
        # add aggrigation  :: post.reaction__set_.filter

        likes = Count('reaction', filter=Q(reaction__reaction=Reaction.UPVOTE))
        posts = Post.objects.annotate(likes=likes)
        top_posts = Post.objects.all().order_by('-created')

        page = self.paginate_queryset(top_posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(top_posts, many=True)
        return Response(serializer.data)
