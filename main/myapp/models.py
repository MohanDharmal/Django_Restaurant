from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Table"
        
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to="categories/%y/%m/%d")
    icon = models.CharField(max_length=100,blank=True)
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
        
class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team')
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Dish(models.Model):
    name = models.CharField(max_length=250,unique=True)
    image = models.ImageField(upload_to='dishes/%y/%m/%d')
    ingredients = models.TextField()
    details = models.TextField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.FloatField()
    discounted_price = models.FloatField(blank=True)
    is_available = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Dish Table'
        
    
    
        

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles/%y/%m/%d',null=True,blank=True)
    contact_number = models.CharField(max_length=15,null=True,blank=True)
    address = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.first_name
    
    class Meta:
        verbose_name_plural = "Profile Table"
        

class Order(models.Model):
    customer = models.ForeignKey(Profile,on_delete=models.CASCADE)
    item = models.ForeignKey(Dish,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    invoice_id = models.CharField(max_length=100,blank=True)
    payer_id = models.CharField(max_length=100,null=True,blank=True)
    ordered_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.customer.user.first_name
    
    class Meta:
        verbose_name_plural = "Order Table"
        
        
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=13)
    date = models.CharField(max_length=150)
    time=models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    feedback = models.TextField()
    image = models.ImageField(upload_to='reviews',null=True,blank=True)
    
    def __str__(self):
        return self.name
    

    
        
    
    