from rest_framework import serializers

from crud.models import User, Category


class UserCategorySerializers(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Category
        fields = ('id', 'name')


class CreateUserSerializers(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)
    category_id = serializers.IntegerField()

    class Meta:
        model = User
        fields = ('title', 'content', 'category_id')


class UserSerializers(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)
    category = UserCategorySerializers()

    class Meta:
        model = User
        fields = ('id', 'title', 'content', 'category')


class CategoryUsersSerializers(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('id', 'title', 'content')


class CategorySerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    user = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'user')

    def get_user(self, obj):
        user = User.objects.filter(category=obj)

        serializer = CategoryUsersSerializers(user, many=True)
        return serializer.data
