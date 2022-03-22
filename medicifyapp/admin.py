from django.contrib import admin
from .models import Product_Details, Categories,Order, EmailConfirmed, bennar, contact_table, Subcategory, Discount_Coupon, blog_post, Blogs_Comments, Brands, Custom_Project, catalog, newsletter_table, Navbar_logo_text_table, Number_Table_Navbar_Footer, Address_text_table, Table_Special_Offer, Table_Special_Offer_Categories, Social_Links, Table_Special_Offer_Products, Service_Table, Service_Request, Service_Banner, dynamic_theme_color, footer_dynamic_theme_color

# Register your models here.


class EmailConfirmedAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'activation_key', 'email_confirmed']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

admin.site.register(EmailConfirmed, EmailConfirmedAdmin)



class show_order(admin.ModelAdmin):
    list_display = ['id', 'user', 'company_name', 'email', 'order_date']

class show_dynamic_theme_color(admin.ModelAdmin):
    list_display = ['color_name', 'color_code']


class show_footer_dynamic_theme_color(admin.ModelAdmin):
    list_display = ['color_name', 'color_code']


class show_service_request(admin.ModelAdmin):
    list_display = ['id', 'user', 'Service','full_name', 'company_name', 'country','email', 'date']


class show_Custom_Project(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Company_Name', 'Email_Adress', 'Project_Name']


class show_newsletter(admin.ModelAdmin):
    list_display = ['id', 'email_address', 'time']



class show_product(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'category', 'subcategory', 'Brands', 'product_status']


class show_Special_Offer_Categories(admin.ModelAdmin):
    list_display = ['Offer_Name', 'Category', 'Percentage']



class show_Special_Offer_Products(admin.ModelAdmin):
    list_display = ['Offer_Name', 'Product', 'Percentage']


class show_Social_link(admin.ModelAdmin):
    list_display = ['Website', 'link']


admin.site.register(footer_dynamic_theme_color, show_footer_dynamic_theme_color)
admin.site.register(dynamic_theme_color, show_dynamic_theme_color)
admin.site.register(Service_Table)
admin.site.register(Service_Banner)
admin.site.register(Service_Request, show_service_request)
admin.site.register(Social_Links, show_Social_link)
admin.site.register(Table_Special_Offer_Products, show_Special_Offer_Products)
# admin.site.register(Table_Special_Offer_Categories, show_Special_Offer_Categories)
admin.site.register(Table_Special_Offer)
admin.site.register(Custom_Project, show_Custom_Project)
admin.site.register(newsletter_table, show_newsletter)
admin.site.register(Product_Details, show_product)
admin.site.register(Categories)
admin.site.register(Order, show_order)
admin.site.register(bennar)
admin.site.register(contact_table)
admin.site.register(Subcategory)
admin.site.register(Discount_Coupon)
admin.site.register(blog_post)
admin.site.register(Blogs_Comments)
admin.site.register(Brands)
admin.site.register(catalog)
admin.site.register(Navbar_logo_text_table)
admin.site.register(Number_Table_Navbar_Footer)
admin.site.register(Address_text_table)