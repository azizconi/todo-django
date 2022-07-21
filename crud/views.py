from rest_framework.response import Response
from rest_framework.views import APIView

from crud.models import User, Category
from crud.serializers import UserSerializers, CategorySerializers, CreateUserSerializers


class UserApiView(APIView):
    def get(self, request):
        getUsers = User.objects.all()

        return Response({'posts': UserSerializers(getUsers, many=True).data})

    def post(self, request):
        # serializer = CreateUserSerializers(data=request.data)
        # serializer.is_valid(raise_exception=True)

        createUser = User.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )
        return Response({'user': CreateUserSerializers(createUser).data})


class CategoryApiView(APIView):
    def get(self, request):
        getCategory = Category.objects.all()

        return Response({'category': CategorySerializers(getCategory, many=True).data})
