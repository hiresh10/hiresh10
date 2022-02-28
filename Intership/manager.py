from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, username, password, **extra_fieds):
        if not username:
            raise ValueError('Username is required')

        return username

    

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff' , True)
        extra_fields.setdefault('is_superuser' , True)
        extra_fields.setdefault('is_active' , True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Super user must have is_staff true'))

        return self.create_user(username , password , **extra_fields)