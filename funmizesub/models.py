from django.db import models
from datetime import datetime
from .utilis import refcode
from django.contrib.auth.models import User


from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings

import datetime
from datetime import timedelta
from datetime import datetime as dt

today = datetime.date.today()

### Custom User Model Used Here

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of username.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


#### This is User Profile
class User(AbstractUser):
    user_gender = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    username = models.CharField(_('Username'), max_length=100, default='', unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=10, default='', choices=user_gender)
    # mobile = models.CharField(max_length=200, null=True)
    photo = models.ImageField(upload_to='users', default="/static/images/profile1.png", null=True, blank=True)
    country = models.CharField(max_length=200, null=True)
    bio = models.TextField(default='', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


#### This is user settings
class UserSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    account_verified = models.BooleanField(default=False)
    verified_code = models.CharField(max_length=100, default='', blank=True)
    verification_expires = models.DateField(default=dt.now().date() + timedelta(days=settings.VERIFY_EXPIRE_DAYS))
    code_expired = models.BooleanField(default=False)
    recieve_email_notice = models.BooleanField(default=True)


#### Membership
class Membership(models.Model):
    MEMBERSHIP_CHOICES = (
    	('Extended', 'Extended'), # Note that they are all capitalize//
    	('Advanced', 'Advanced'),
    	('Medium', 'Medium'),
        ('Basic', 'Basic'),
        ('Free', 'Free')
    )
    PERIOD_DURATION = (
        ('Days', 'Days'),
        ('Week', 'Week'),
        ('Months', 'Months'),
    )
    slug = models.SlugField(null=True, blank=True)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default='Free', max_length=30)
    duration = models.PositiveIntegerField(default=7)
    duration_period = models.CharField(max_length=100, default='Day', choices=PERIOD_DURATION)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
       return self.membership_type

#### User Membership
class UserMembership(models.Model):
    user = models.OneToOneField(User, related_name='user_membership', on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, related_name='user_membership', on_delete=models.SET_NULL, null=True)
    reference_code = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
       return self.user.username






































class Contactinfo(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = models.CharField(max_length = 11)
    subject = models.CharField(max_length= 250)
    message = models.TextField()
    date = models.DateTimeField(default=datetime, blank=True)

    def __str__ (self):
        return self.name

class Networkplan(models.Model):
    network_name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.network_name


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    email = models.EmailField()
    phone_number = models.CharField(max_length=70)
    status = models.CharField(max_length=70)
    referral_id = models.CharField(max_length=70)
    bankname = models.CharField(max_length=70)
    acct_name = models.CharField(max_length=70)
    acct_number = models.CharField(max_length=70)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'customers'
        managed = True
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    walletID = models.CharField(max_length=100, default='')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'UserWallet'
        managed = True
        verbose_name = 'UserWallet'
        verbose_name_plural = 'UserWallets'


class Transhistory(models.Model):
    card_number = models.CharField(max_length=20)
    volume = models.CharField(max_length=50)
    amount = models.IntegerField(null=True, blank=True)
    reference_id = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='Success')
    service = models.CharField(max_length=50)
    prebal = models.IntegerField(null=True, blank=True)
    postbal = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference_id

    class Meta:
        db_table = 'Transhistory'
        managed = True
        verbose_name = 'Transhistory'
        verbose_name_plural = 'Transhistorys'


class PayHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    paystack_charge_id = models.CharField(max_length=100, default='', blank=True)
    paystack_access_code = models.CharField(max_length=100, default='', blank=True)
    payment_for = models.CharField(max_length=70, null=True, default='wallet funding')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


















# 
# class Planamount(models.Model):
    # network_type = models.ForeignKey(Networkplan, on_delete=models.CASCADE)
    # volume = models.CharField(max_length=20)
    # amount = models.IntegerField()
    # is_available = models.BooleanField(default=True)
# 
    # def __str__(self):
        # return self.volume

# class Addbalancetouser(models.Model):
    ##username = models.CharField(max_length=300, default='lolodef')
    # email = models.ForeignKey(User, on_delete=models.CASCADE)
    # amount_to_add = models.IntegerField()
    # refcode = models.CharField(max_length=30, default=refcode)
# 
    # def __str__(self):
        # return self.user.email



# class Wallet(models.Model):
    # new_balance = models.FloatField()
    # old_balance = models.FloatField()
    # amount_added = models.FloatField()
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # active = models.BooleanField(default=False)
    # date = models.DateTimeField(default=datetime.now, blank=True)
# 
    # def __str__(self):
        # return self.customer.email
# 
    # class Meta:
        # db_table = 'wallets'
        # managed = True
        # verbose_name = 'Wallet'
        # verbose_name_plural = 'Wallets'



























































# class Customerprofile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, default=2)
    # username = models.CharField(max_length=70)
    # email = models.EmailField()
    # phone_number = models.CharField(max_length=70)
    # status = models.CharField(max_length=70)
    # referral_id = models.CharField(max_length=70)
    # bankname = models.CharField(max_length=70)
    # acct_name = models.CharField(max_length=70)
    # acct_number = models.CharField(max_length=70)
# 
    # def __str__(self):
        # return self.username

# class Userwallet(models.Model):
    # customer = models.ForeignKey(Customerprofile, on_delete=models.DO_NOTHING, null=True, default='12')
    # previous_balance = models.IntegerField(default=200)
    # new_balance = models.IntegerField(default=6500)
    # current_balance = models.IntegerField(default= 9500)
    # date = models.DateTimeField(default=datetime.now, blank=True)
# 
    # def __str__(self):
        # return self.customer

