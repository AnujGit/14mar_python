from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    house_no = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=30)
    pic = models.FileField(upload_to="media/images",default="media/images/user.png")

    def __str__(self):
        return self.firstname + ' ' + self.lastname

class SocietyMember(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    house_no = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=30)
    blood_group = models.CharField(max_length=5)
    job_description = models.CharField(max_length=60)
    work_address = models.TextField()
    no_of_family_address = models.CharField(max_length=30)
    vehicle_details = models.CharField(max_length=60)
    pic = models.FileField(upload_to="media/images",default="media/images/user.png")

    def __str__(self):
        return self.firstname + ' ' + self.lastname

class EventGallery(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    media_type = models.CharField(max_length=30)
    video = models.FileField(upload_to="media/videos", null=True, blank=True,verbose_name="")
    pic = models.FileField(upload_to="media/images",null=True, blank=True)