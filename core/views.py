from django.shortcuts import render
from .models import Facts,Skills_left,Main_content,Skills_right,\
    Services,Testimonials,Contact,About,Resuma_education,Resuma_professional,\
    Resuma_summery,Contact_form,Project_pattern_trading


def index(request):
    main_content = Main_content.objects.all()
    print(main_content[0:8])
    about = About.objects.all()
    facts = Facts.objects.all()
    skills_left = Skills_left.objects.all()
    skills_right = Skills_right.objects.all()
    services = Services.objects.all()
    testimonials = Testimonials.objects.all()
    contact = Contact.objects.all()
    resuma_education =Resuma_education.objects.all()
    resuma_professional =Resuma_professional.objects.all()
    resuma_summery = Resuma_summery.objects.all()
    projects_data = Project_pattern_trading.objects.all()
    contact_form = Contact_form()

    if request.method == 'POST':
        contact_form_name = request.POST.get('contact_form_name')
        print(contact_form_name)
        print(request.POST.get('contact_form_name'))
        contact_form_email = request.POST.get('contact_form_email')
        contact_form_subject = request.POST.get('contact_form_subject')
        contact_form_message = request.POST.get('contact_form_message')
        contact_form.contact_form_name = contact_form_name
        contact_form.contact_form_email = contact_form_email
        contact_form.contact_form_subject = contact_form_subject
        contact_form.contact_form_message = contact_form_message
        contact_form.save()



    return render(request, 'index.html', {'about':about, 'facts':facts, 'skills_left':skills_left,
                                                              'skills_right':skills_right, 'main_content':main_content,
                                                              'services':services, 'testimonials':testimonials, 'contact':contact,
                                                              'resuma_education':resuma_education,'resuma_professional':resuma_professional,
                                                              'resuma_summery':resuma_summery,'projects_data':projects_data})


#
# def form(request):
#     contact_form = Contact_form()
#     if request.method == 'POST':
#         contact_form_name = request.POST.get('contact_form_name')
#         print(contact_form_name)
#         print(request.POST.get('contact_form_name'))
#         contact_form_email = request.POST.get('contact_form_email')
#         contact_form_subject = request.POST.get('contact_form_subject')
#         contact_form_message = request.POST.get('contact_form_message')
#         contact_form.contact_form_name = contact_form_name
#         contact_form.contact_form_email = contact_form_email
#         contact_form.contact_form_subject = contact_form_subject
#         contact_form.contact_form_message = contact_form_message
#         contact_form.save()
#
#     return render(request,'contact_form.html',{})

