from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class MyUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, date_of_birth, email, gender,
                    faculty, phone_number, city, address, password=None):
        if not email:
            raise ValueError('пользователь должен иметь email')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            gender=gender,
            faculty=faculty,
            phone_number=phone_number,
            city=city,
            address=address
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password, date_of_birth=None, gender=None,
                         faculty=None, phone_number=None, city=None, address=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            password=password,
            date_of_birth=date_of_birth,
            gender=gender,
            faculty=faculty,
            phone_number=phone_number,
            city=city,
            address=address
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    first_name = models.CharField(verbose_name='имя',
                                  max_length=100)
    last_name = models.CharField(verbose_name='фамилия',
                                 max_length=100)
    date_of_birth = models.DateField(verbose_name='день рождения', blank=True,
                                     default=None, null=True)
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    GENDER_CHOICES = (
        ('male', 'мужской'),
        ('female', 'женский'),
    )
    gender = models.CharField(max_length=20, verbose_name='пол',
                              choices=GENDER_CHOICES, blank=True,
                              default=None, null=True)
    faculty = models.ForeignKey(Faculty, verbose_name='факультет',
                                blank=True, default=None, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='номер телефона',
                                    blank=True, default=None, null=True)
    city = models.ForeignKey(City, verbose_name='город',
                             blank=True, default=None, null=True)
    address = models.CharField(max_length=100, verbose_name='адрес',
                               blank=True, default=None, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
