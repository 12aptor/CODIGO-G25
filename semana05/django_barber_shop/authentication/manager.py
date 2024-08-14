from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email required')
        
        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email = email,
            password = password
        )
        user.is_superuser = True
        user.save(using=self._db)

        return user