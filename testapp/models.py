from django.db import models

# Create your models here.
class Post(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=80)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default="0")
    quantity=models.IntegerField(default="0")
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    images=models.ImageField(upload_to="media\images",default="")
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
def __str__(self):
    return self.product_name
