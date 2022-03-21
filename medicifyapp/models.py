from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
import hashlib
# Create your models here.
from ckeditor.fields import RichTextField


class dynamic_theme_color(models.Model):
    class Meta:
        verbose_name_plural = 'Dynamic Theme Color'
    color_name = models.CharField(max_length=255)
    color_code = models.CharField(max_length=255)

    def __str__(self):
        return self.color_name + ' - ' + self.color_code

    def save(self, *args, **kwargs):
        dynamic_theme_color.objects.all().delete()
        super().save(*args, **kwargs)


class EmailConfirmed(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    activation_key=models.CharField(max_length=255)
    email_confirmed=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural='User Email-Confirmed'

@receiver(post_save, sender=User)
def create_user_email_confirmation(sender, instance, created, **kwargs):
    if created:
        dt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        email_confirmed_instance=EmailConfirmed(user=instance)
        user_encoded=f'{instance.email}-{dt}'.encode()
        activation_key=hashlib.sha224(user_encoded).hexdigest()
        email_confirmed_instance.activation_key=activation_key
        email_confirmed_instance.save()




class Discount_Coupon(models.Model):
    class Meta:
        verbose_name_plural = 'Discount Coupon'
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    discount_percentage = models.IntegerField(default='0')
    active_status = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Brands(models.Model):
    class Meta:
        verbose_name_plural = 'Brands'
    Brand_name = models.CharField(max_length=255)
    Brand_discription = models.TextField(default='')
    Brand_image = models.ImageField(upload_to='uploads/category_img', null=True, blank=True, default='')

    def __str__(self):
        return self.Brand_name



class Service_Table(models.Model):
    class Meta:
        verbose_name_plural = 'Service Table'
    Service_name = models.CharField(max_length=255)
    Service_discription = models.TextField(default='')
    Service_image = models.ImageField(upload_to='uploads/category_img', null=True, blank=True, default='')

    def __str__(self):
        return self.Service_name



class Service_Banner(models.Model):
    class Meta:
        verbose_name_plural = 'Service Banner'
    Banner_name = models.CharField(max_length=255)
    Service_image = models.ImageField(upload_to='uploads/service_banner', null=True, blank=True, default='')

    def __str__(self):
        return self.Banner_name



class Service_Request(models.Model):
    class Meta:
        verbose_name_plural = 'Service Request'
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Service = models.ForeignKey(Service_Table, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255, default = '', blank=True, null=True)
    company_name = models.CharField(max_length=255, default='', blank=True, null=True)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    Discription = models.TextField(blank=True, null=True)
    Attachment_files = models.FileField(upload_to='services_picture', blank=True, null=True)
    date = models.DateField(default=datetime.now(), blank=True)



class Categories(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    category_name = models.CharField(max_length=255)
    category_discription = models.TextField()
    Category_image = models.ImageField(upload_to='uploads/category_img', null=True, blank=True, default='')

    def __str__(self):
        return self.category_name

    def subcat_list(self):
        kkk = Subcategory.objects.filter(Category=self)

        return kkk



class Subcategory(models.Model):
    class Meta:
        verbose_name_plural = 'Subcategory'
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    Subcategory = models.CharField(max_length=255)
    Subcategory_discription = models.TextField()
    Subcategory_image = models.ImageField(upload_to='uploads/Subcategory_img', null=True, blank=True, default='')
    def __str__(self):
        return self.Subcategory +", "+ self.Category.category_name



class Product_Details(models.Model):
    class Meta:
        verbose_name_plural = 'Product Table'
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True, default=None)
    Brands=models.ForeignKey(Brands, on_delete=models.CASCADE, default=None, null=True, blank=True)
    # price = models.IntegerField()
    # currency_type = models.CharField(max_length=255, default='ZAR')
    Short_description = RichTextField(blank=True, null=True, default='')
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product_image', null=True, blank=True, default='')
    image2 = models.ImageField(upload_to='uploads/product_image', null=True, blank=True, default='')
    image3 = models.ImageField(upload_to='uploads/product_image', null=True, blank=True, default='')
    image4 = models.ImageField(upload_to='uploads/product_image', null=True, blank=True, default='')
    image5 = models.ImageField(upload_to='uploads/product_image', null=True, blank=True, default='')
    status = (
        ("New", "New"),
        ("In stock", "In stock"),
        ("Out stock", "Out stock"),
    )
    product_status = models.CharField(max_length=255, choices=status, default="New")
    catalogue = models.FileField(upload_to='uploads/catalogue', null=True, blank=True, default='')
    datasheets = models.FileField(upload_to='uploads/datasheets', null=True, blank=True, default='')

    def __str__(self):
        return "("+ str(self.id) + ") " +self.product_name


class contact_table(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Table'
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    message=models.TextField()

    def __str__(self):
        return self.name




class Order(models.Model):
    class Meta:
        verbose_name_plural = 'All Orders'
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=255)
    items_json = models.TextField()
    # total_bill = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, default='', blank=True, null=True)
    company_name = models.CharField(max_length=255, default='', blank=True, null=True)
    full_address = models.TextField()
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    Discount_Coupon = models.ForeignKey(Discount_Coupon, on_delete=models.CASCADE, null=True, blank=True)
    order_date = models.DateField(default=datetime.now(), blank=True)
    

    # def __str__(self):
    #     return self.user.username + ' - '+self.company_name+ ' - '+self.email+ ' - '

class bennar(models.Model):
    class Meta:
        verbose_name_plural = 'Bennar'
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/product_image')

    def __str__(self):
        return self.name




class blog_post(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Post'
    title = models.CharField(max_length=255, blank=True, null=True)
    discription = RichTextField(blank=True, null=True)
    Blog_video = models.FileField(blank=True, null=True, upload_to='Blog_video', default=None)
    img = models.ImageField(blank=True, null=True, upload_to='post_img')
    img2 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img3 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img4 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img5 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img6 = models.ImageField(blank=True, null=True, upload_to='post_img')
    time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title


class Blogs_Comments(models.Model):
    class Meta:
        verbose_name_plural = 'Blogs Comments'
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Blog = models.ForeignKey(blog_post, on_delete=models.CASCADE)
    comment_subject = models.CharField(max_length=255)
    comment_text = models.TextField()
    time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.User.email + " - "+ self.Blog.title



class Custom_Project(models.Model):
    class Meta:
        verbose_name_plural = 'Custom Project'
    Name = models.CharField(max_length=255)
    Company_Name = models.CharField(max_length=255)
    Email_Adress = models.CharField(max_length=255)
    Phone_Number = models.CharField(max_length=255, blank=True, null=True)
    Project_Name = models.CharField(max_length=255)
    Details = models.TextField(blank=True, null=True)
    Attach_File = models.FileField(blank=True, null=True, upload_to='custom_project/attach/')

    def __str__(self):
        return self.Name


class catalog(models.Model):
    class Meta:
        verbose_name_plural = 'catalog'
    name = models.CharField(max_length=255)
    catalog_url = models.TextField()
    # catalog_File = models.FileField(blank=True, null=True, upload_to='catalog/')
    def __str__(self):
        return self.name


class newsletter_table(models.Model):
    class Meta:
        verbose_name_plural = 'Newsletter Table'
    email_address = models.CharField(max_length=255)
    time = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.email_address


class Navbar_logo_text_table(models.Model):
    class Meta:
        verbose_name_plural = 'Navbar Logo Text Table'
    logo_text = models.CharField(max_length=255)
    def __str__(self):
        return self.logo_text


class Number_Table_Navbar_Footer(models.Model):
    class Meta:
        verbose_name_plural = 'Number Table Navbar Footer'
    number = models.CharField(max_length=255)
    def __str__(self):
        return self.number


class Address_text_table(models.Model):
    class Meta:
        verbose_name_plural = 'Address Text Table'
    Address = models.CharField(max_length=255)
    def __str__(self):
        return self.Address


class Table_Special_Offer(models.Model):
    class Meta:
        verbose_name_plural = 'Special Offer'
    Offer_Name = models.CharField(max_length=255)
    Offer_Text = models.TextField(null=True, blank=True, default='')
    offer_image= models.ImageField(null=True, blank=True, default=None)
    offer_expiry_date = models.DateField()

    def __str__(self):
        return self.Offer_Name

    # def save(self, *args, **kwargs):
    #
    #     super(Table_Special_Offer, self).save(*args, **kwargs)


class Table_Special_Offer_Categories(models.Model):
    class Meta:
        verbose_name_plural = 'Special Offer Categories'
    Offer_Name = models.ForeignKey(Table_Special_Offer, on_delete=models.CASCADE)
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    Percentage = models.IntegerField()


class Table_Special_Offer_Products(models.Model):
    class Meta:
        verbose_name_plural = 'Special Offer Products'
    Offer_Name = models.ForeignKey(Table_Special_Offer, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product_Details, on_delete=models.CASCADE)
    Percentage = models.IntegerField()


class Social_Links(models.Model):
    class Meta:
        verbose_name_plural = 'Social Links'

    Website = models.CharField(max_length=255, default="")
    link = models.CharField(max_length=255)
    def __str__(self):
        return self.Website


