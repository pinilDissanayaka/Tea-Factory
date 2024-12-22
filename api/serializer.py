from django.contrib.auth.models import User



class UserSerializer():
    class Meta:
        model = User
        fields = ['username', 'email', 'password']