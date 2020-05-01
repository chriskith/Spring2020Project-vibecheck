from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, response, parsers
from .models import User, Profile, Post, Friendship
from .parsers import MultiPartJsonParser
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, ProfileSerializer, PostSerializer, FriendshipSerializer, FollowRecommendationSerializer
from knox.models import AuthToken



def index(request):
    return render(request, 'vibecheck/index.html')


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response.Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return response.Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })



# class UserView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'username'


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date')
    serializer_class = PostSerializer
    parser_classes = (MultiPartJsonParser, parsers.JSONParser)


class FriendshipView(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer


class FollowRecommendationView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = FollowRecommendationSerializer