from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class slider(models.Model):
    
    slider_link=models.CharField(max_length=50)
    slider_des=models.CharField(max_length=50)
    slider_name=models.CharField(max_length=50)
    slider_image=models.ImageField(upload_to="slider")
    slider_deal=models.CharField(max_length=50)
    slider_discount=models.CharField(max_length=50)
    def __str__(self):
      return self.slider_name
class banner(models.Model):
    
   banner_link=models.CharField(max_length=50)
   banner_des=models.CharField(max_length=50)
   banner_name=models.CharField(max_length=50)
   banner_image=models.ImageField(upload_to="topsell")
   banner_discount=models.CharField(max_length=50)
   def __str__(self):
       return self.banner_name



       
class banner1(models.Model):
    
  banner1_name=models.CharField(max_length=50)
  banner1_link=models.CharField(max_length=50)
  
  banner1_image=models.ImageField(upload_to="banner1")
  banner1_des=models.CharField(max_length=50)
  banner1_title=models.CharField(max_length=50)
  def __str__(self):
       return self.banner1_name
  
class selling(models.Model):
    
  selling_name=models.CharField(max_length=50)
  selling_price=models.CharField(max_length=50)
  
  selling_image=models.ImageField(upload_to="selling")
  selling_discount=models.CharField(max_length=50)
  def __str__(self):
       return self.selling_name

class feature(models.Model):
    
  feature_name=models.CharField(max_length=50)
  feature_price=models.CharField(max_length=50)
  
  feature_image=models.ImageField(upload_to="feature")
  feature_discount=models.CharField(max_length=50)
  feature_oprice=models.CharField(max_length=50)
  feature_list1=models.CharField(max_length=50)
  feature_list2=models.CharField(max_length=50)
  feature_list3=models.CharField(max_length=50)
  feature_list4=models.CharField(max_length=50)
  def __str__(self):
       return self.feature_name


class feature1(models.Model):
    
  feature1_name=models.CharField(max_length=50)
  feature1_price=models.CharField(max_length=50)
  
  feature1_image=models.ImageField(upload_to="feature1")
  feature1_discount=models.CharField(max_length=50)
  feature1_oprice=models.CharField(max_length=50)
  
  def __str__(self):
       return self.feature1_name
      
class moving(models.Model):
  moving_first=models.CharField(max_length=100)
  moving_second=models.CharField(max_length=100)
  moving_third=models.CharField(max_length=100)


class banner3(models.Model):
  banner3_link=models.CharField(max_length=100)
  banner3_image=models.ImageField(upload_to="banner3")
  banner3_deal=models.CharField(max_length=100)


class banner4(models.Model):
  banner4_name=models.CharField(max_length=100)
  banner4_image=models.ImageField(upload_to="banner4")
  banner4_deal=models.CharField(max_length=100)
  banner4_des=models.CharField(max_length=100)

class banner5(models.Model):
  banner5_name=models.CharField(max_length=100)
  banner5_image=models.ImageField(upload_to="banner5")
 
  banner5_des=models.CharField(max_length=100)


class banner6(models.Model):
  banner6_name=models.CharField(max_length=100)
  banner6_image=models.ImageField(upload_to="banner6")
  banner6_deal=models.CharField(max_length=100)
  
class recommended1(models.Model):
    
  recommended1_name=models.CharField(max_length=50)
  recommended1_price=models.CharField(max_length=50)
  
  recommended1_image=models.ImageField(upload_to="recommended1")
  recommended1_discount=models.CharField(max_length=50)


class brand(models.Model):
    
 
  
  brand_first=models.ImageField(upload_to="brand")
  brand_second=models.ImageField(upload_to="brand")
  brand_three=models.ImageField(upload_to="brand")
  brand_four=models.ImageField(upload_to="brand")
  brand_five=models.ImageField(upload_to="brand")
  brand_six=models.ImageField(upload_to="brand")


class main(models.Model):
  
   name=models.CharField(max_length=50)
  
   def __str__(self):
       return self.name


class sub_main(models.Model):
   main=models.ForeignKey(main,on_delete=models.CASCADE)
   name=models.CharField(max_length=50)
  
   def __str__(self):
       return self.main.name+'---'+self.name

class sub_sub(models.Model):
   main=models.ForeignKey(sub_main,on_delete=models.CASCADE)
   name=models.CharField(max_length=50)
  
   def __str__(self):
       return self.main.main.name+'---'+self.main.name+'---'+self.name


class section(models.Model):
  name=models.CharField(max_length=50)
  def __str__(self):
       return self.name



class products(models.Model):
  name= models.CharField(max_length=100)
  image=models.ImageField(upload_to="product/%Y/%m/%d")
  product_details=RichTextUploadingField()
  price = models.IntegerField()
  product_discount=models.IntegerField()
  product_category=models.ForeignKey(sub_main,on_delete=models.CASCADE)
  quantity=models.IntegerField()
  product_availability=models.IntegerField()
  product_des=RichTextUploadingField()
  product_tag=models.CharField(max_length=100)
  product_section=models.ForeignKey(section,on_delete=models.DO_NOTHING)
  product_slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
  def __str__(self):
       return self.name

class threeimag1(models.Model):
  products=models.ForeignKey(products,on_delete=models.CASCADE)
  image=models.ImageField(upload_to="product/%Y/%m/%d")
  

class additional1(models.Model):
  product=models.ForeignKey(products,on_delete=models.CASCADE)
  specification=models.CharField(max_length=100)
  details=models.CharField(max_length=100)






