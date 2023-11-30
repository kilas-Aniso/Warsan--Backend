
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from location.models import Location
from datetime import date


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)
STATUS_CHOICES = (
    ('A', 'Active'),
    ('I', 'Inactive'),
)

class Child(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    guardian= models.ForeignKey("Guardian", on_delete=models.SET_NULL,null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,null=True)
    phone_number = PhoneNumberField(region='IR')
   
    def save(self, *args, **kwargs):
        if self.guardian:
            self.location = self.guardian.location
            self.phone_number = self.guardian.phone_number
        super().save(*args, **kwargs)


    def  deactivate_child(self,child_detail):
        child = Child.objects.get(pk=child_detail)
        child.status = 'I'
        child.save()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def age(self):
        today = date.today()
        age_in_months = (today.year - self.date_of_birth.year) * 12 + (today.month - self.date_of_birth.month)
        return age_in_months 
    class Meta:
        unique_together = ('first_name', 'last_name', 'guardian')
    


from django.db import models
 
from location.models import Location



class Guardian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,null=True)
    phone_number = PhoneNumberField(unique=True, region='IR')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A') 
  

    def  deactivate_guardian(self,guardian_detail):
        # Guardian = Child.objects.get(pk=guardian_detail)
        self.status = 'I'
        self.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def register_child(self):
        child = Child.objects.create(
            first_name=self.first_name,
            last_name=self.last_name,
            guardian=self,


            )
        return child

    def get_children(self):
        return self.children.all()
    
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} (Guardian)"