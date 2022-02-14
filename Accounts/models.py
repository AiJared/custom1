from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class customManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_admin=False, is_active=True, is_student=False, is_teacher=False, is_staff=False):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have a username")
        if not password:
            raise ValueError("Users must have a password")

        user_obj = self.model(
            email=self.normalize_email(email), username=username
        ) 
        user_obj.set_password(password)
        user_obj.is_active = is_active
        user_obj.is_admin = is_admin
        user_obj.is_staff = is_staff
        user_obj.is_student = is_student
        user_obj.is_teacher = is_teacher
        user_obj.save(using=self._db)
        return user_obj

    def create_staff(self, email, username, password=None):
        user = self.create_user(
            email, username, password, is_active=True,
            is_staff=True, is_admin=False, is_student=False, is_teacher=False
        )
        return user

    def create_super_user(self, email, username, password=None):
        user = self.create_user(
            email, username, password, is_active=True,
            is_admin=True, is_staff=True, is_student=False, is_teacher=False
        )
        return user
class User(AbstractBaseUser):
    username = models.CharField(max_length=63, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = customManager()

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True


    @property
    def staff(self):
        return self.staff

    @property
    def admin(self):
        return self.admin

    @property
    def active(self):
        return self.active

    @property
    def student(self):
        return self.student
    
    @property
    def teacher(self):
        return self.teacher

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to = "profilePictures/%y/%m/%d", default="default.png"
    )
    # You can add your own fields
    class Meta:
        Abstract = True

class Teacher(Profile):
    pass # You can add teacher's fields

    def __str__(self):
        return self.user.uername

class Student(Profile):
    pass # You can Also add student's fields

    def __str__(self):
        return self.user.username