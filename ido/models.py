from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Survey(models.Model):
    name = models.CharField(max_length=20)               # 이름
    major = models.CharField(max_length=20)              # 전공  
    phone_num = models.CharField(default = '',max_length=13) 
    body_temp = models.DecimalField(max_digits=5,decimal_places=3)           #체온 - 입력(5자리숫자중 소수점아래 3자리표시)
    update_time = models.DateTimeField('date published')    # 입력시간
    agree_check = models.BooleanField()                     #동의여부

    def __str__(self):
        return self.name