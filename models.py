from django.db import models
from datetime import date

# Create your models here.

class Userdata(models.Model) :
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    aadhar_number = models.BigIntegerField(max_length = 16)
    address = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 6)
    date_of_birth = models.DateField()
    mediclaim_number = models.IntegerField(max_length = 5)
    phone_number = models.BigIntegerField(max_length = 10)
    email_address = models.EmailField()
    user_name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 25)
    health_id = models.CharField(max_length = 15 , primary_key = True)

    def __str__(self) :
        def calculate_age(self):
            bd = self.date_of_birth
            if bd:
                td = date.today()
                user_age = td.year - bd.year - ((td.month, td.day) < (bd.month, bd.day))
        return f"Name : {self.first_name} {self.last_name} \n Gender : {self.gender} \n Age : {user_age}"


        
    