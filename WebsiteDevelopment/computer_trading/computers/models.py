from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class ComputerSpecification(models.Model):
    hardDisk= (
        ('16 GB','16 GB'),
        ('32 GB','32 GB'),
        ('64 GB','64 GB'),
        ('128 GB','128 GB'),
        ('256 GB','256 GB'),
        ('500 GB','500 GB'),
        ('1 TB ','1 TB/ 1000 GB'),
    ('1.5 TB ','1.5 TB/ 1500 GB'),
    ('2 TB ','2 TB/ 2000GB'),
    ('4 TB ','4 TB/ 4000GB'),
    ('6 TB ','6 TB/ 6000GB'),
    ('8 TB ','8 TB/ 8000GB'),
   
    )
    ramSize = (
         ('LESS THAN 1GB', '<1 GB'),
  
        ('1 GB', '1 GB'),
         ('2 GB', '2 GB') ,
         ('4 GB', '4 GB'),
          ('8 GB', '8 GB'),
        ('12 GB', '12 GB'),
        ('GREATER THAN 16 GB', '>16 GB'),
        
  
    )
    statusType = ('new','new'),('slightly used','slightly used'), ('used','used')
    screenSize = ('11.6 inch','11.6 inch'),('12.5 inch','12.5 inch'),('13.3 inch', '13.3 inch'),('14 inch','14 inch'), ('15.6 inch','15.6 inch'),('17.3 inch','17.3 inch')
    coreType = ('i3','i3'),('i5','i5'),('i7','i7'),('i9','i9')
    phone_message = 'phone number must be entered in the format 09xxxxxxxx or +2519xxxxxxxx'
    phone_regex = RegexValidator(
       regex = r"^\+?\d{10,12}$",
        message= phone_message
    )
    price_regex = RegexValidator(
        regex = r"^\d",
        message ="Enter amount in number"
    ) 
    battery_life_regex = RegexValidator(
        regex = r"^\d\.\d\s(hr)",
        message ="Enter in 5.6 hr form"
    )
    processorMessage="the value must be in 5.6 GHz format"
    processorSpeed_regex = RegexValidator(
        regex = r"^\d?\.\d\s(GHz)",
        message =processorMessage ,
       
    )
    model= models.CharField(max_length=200)
    core = models.CharField(max_length=2 , choices=coreType)

    ram = models.CharField(max_length=30, choices=ramSize)
    hard_disk = models.CharField(max_length=10 , choices=hardDisk)
    processor_speed = models.CharField(validators = [processorSpeed_regex],max_length=7, help_text="the value must in 5.6 GHz format")
    status = models.CharField(choices = statusType, max_length=30)
    battery_life=models.CharField(validators=[battery_life_regex], max_length=15,default='2.5 hr')
    screen_size = models.CharField(max_length=10 , choices=screenSize)
    photo = models.ImageField(upload_to='images', default=None)
   
    phone = models.CharField(validators=[phone_regex], max_length=40 )
    phone2 = models.CharField(validators=[phone_regex], max_length=40 ,null=True,blank=True, help_text="optional")
    description = models.TextField(max_length=400, null=True, blank=True)
    price=models.CharField(help_text="inter the price in 15000 format",max_length=10 , validators=[price_regex],default=15000)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    def __str__(self):
        return self.model 
    def get_absolute_url(self):
        return  reverse('computer_detail' , args=[str(self.id)])