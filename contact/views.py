from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.mail import send_mail
from gconfs_website import settings

from .forms import ContactForm

# Create your views here.

def index(request):
    template = loader.get_template('contact/index.html')

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            try:
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                sender = form.cleaned_data['sender']

                recipients = [settings.CONTACT_EMAIL]

                if form.cleaned_data['cc_myself']:
                    recipients.append(sender)

                send_mail(settings.EMAIL_SUBJECT_PREFIX + subject, message,
                        sender, recipients)
                return HttpResponseRedirect('/contact/thanks/')

            except Exception as e:
                print(e)
                return HttpResponseRedirect('/contact/error/')

        else:
            return HttpResponseRedirect('/contact/robots/')

    else:
        form = ContactForm()
        context = RequestContext(request, {'form': form})
        return HttpResponse(template.render(context))


def thanks(request):
    template = loader.get_template('contact/thanks.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def robots(request):
    template = loader.get_template('contact/robots.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def error(request):
    template = loader.get_template('contact/error.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
