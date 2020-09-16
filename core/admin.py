from django.contrib import admin
from .models import Main_content,About,Facts,Skills_left,Services,\
    Testimonials,Contact,Skills_right,Resuma_education,Resuma_professional, \
    Resuma_summery,Contact_form,Table_content,Project_pattern_trading


# Register your models here.

admin.site.register(Main_content),
admin.site.register(About),
admin.site.register(Facts),
admin.site.register(Skills_left),
admin.site.register(Skills_right),
admin.site.register(Services),
admin.site.register(Testimonials),
admin.site.register(Contact),
admin.site.register(Resuma_education),
admin.site.register(Resuma_professional),
admin.site.register(Resuma_summery),
admin.site.register(Contact_form),
admin.site.register(Table_content),
admin.site.register(Project_pattern_trading)