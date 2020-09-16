from django.db import models

# Create your models here.

class About(models.Model):
    first_about = models.TextField()
    last_about = models.TextField(default=0)
    birthday = models.DateTimeField()
    website = models.TextField(max_length=100)
    phone = models.TextField(default=0)
    city = models.TextField()
    age = models.IntegerField(default=0)
    degree = models.TextField(default=0)
    email = models.EmailField(default=0)
    freelancer = models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to='profile_image')

    def __str__(self):
        return self.first_about

class Facts(models.Model):
    facts_emog_icon = models.TextField()
    facts_numbers = models.IntegerField()
    facts_text_strong = models.TextField(max_length=100)
    facts_text_phara = models.TextField(max_length=100)
    def __str__(self):
        return self.facts_text_strong

class Skills_left(models.Model):
    skillset_left = models.TextField()
    skill_percentage_left = models.IntegerField()
    def __str__(self):
        return self.skillset_left

class Skills_right(models.Model):
    skillset_right = models.TextField()
    skill_percentage_right = models.IntegerField()
    def __str__(self):
        return self.skillset_right

class Main_content(models.Model):
    about_main = models.TextField()
    facts_main = models.TextField()
    skill_main = models.TextField()
    resume_main = models.TextField()
    project_main = models.TextField()
    service_main = models.TextField()
    testimonials_main = models.TextField()
    contact_main = models.TextField()


class Services(models.Model):
    services_emog_icon = models.TextField()
    services_heading = models.TextField(max_length=200)
    services_text_phara = models.TextField(max_length=300)

    def __str__(self):
        return self.services_heading

class Testimonials(models.Model):
    testimonials_quote = models.TextField()
    testimonials_name = models.TextField(max_length=100)
    testimonials_image = models.ImageField('testimonials_image')
    testimonials_desigination = models.TextField(max_length=100)

    def __str__(self):
        return self.testimonials_quote


class Contact(models.Model):
    contact_address = models.TextField()
    contact_email = models.EmailField()
    contact_call = models.TextField()


class Resuma_professional(models.Model):
    resuma_Professional_heading = models.TextField()
    resuma_Professional_date_till = models.TextField(blank=True)
    resuma_Professional_discription = models.TextField(blank=True)
    resuma_professional_bullet = models.TextField(blank=True, null=True)
    resuma_professional_bullet1 = models.TextField(blank=True, null=True)
    resuma_professional_bullet2 = models.TextField(blank=True, null=True)
    resuma_professional_bullet3 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.resuma_Professional_heading

class Resuma_education(models.Model):
    resuma_education_heading = models.TextField()
    resuma_education_date_till = models.TextField(blank=True)
    resuma_education_location = models.TextField(blank=True)
    resuma_education_paragraph = models.TextField(blank=True)

    def __str__(self):
        return self.resuma_education_heading


class Resuma_summery(models.Model):
    resuma_summery_name = models.TextField()
    resuma_summery_paragraph = models.TextField(blank=True)
    resuma_summery_bullet1 = models.TextField(blank=True)
    resuma_summery_bullet2 = models.TextField(blank=True)
    resuma_summery_bullet3 = models.TextField(blank=True)

    def __str__(self):
        return self.resuma_summery_name


class Contact_form(models.Model):
    contact_form_name = models.CharField(max_length=100)
    contact_form_email = models.EmailField(max_length=200)
    contact_form_subject = models.TextField(max_length=100)
    contact_form_message = models.TextField()

    def __str__(self):
        return self.contact_form_name

class Table_content(models.Model):
    table_Symbole = models.TextField()
    table_Price = models.FloatField(blank=True)
    table_Yesterday_close = models.FloatField(blank=True)
    table_Yesterday_ralley_percentage = models.FloatField(blank=True)
    table_today_open = models.FloatField(blank=True)
    table_extra = models.TextField(blank=True)
    table_chart = models.TextField(blank=True)

    def __str__(self):
        return self.table_Symbole

class Project_pattern_trading(models.Model):
    project_pattern_trading_img = models.ImageField(upload_to='project/pattern_trading')
    project_pattern_trading_redirect = models.TextField()

    def __str__(self):
        return self.project_pattern_trading_redirect



