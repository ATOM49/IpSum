from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import loader
from django.template.context import RequestContext
from users.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from IpSum import settings
from twilio.rest import TwilioRestClient
import random

# Create your views here.
def IndexView(request):
    # Obtain the context from the HTTP request
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:home'))
    template_name = 'core/index.html'
    template = loader.get_template(template_name)
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def LoginView(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:home'))
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('users:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            context["error_message"] = "Invalid login details."
    return render_to_response("core/login.html", context, context_instance=RequestContext(request))


"""Registration Veiw"""
# def _get_pin(length=5):
#     """ Return a numeric PIN with length digits """
#     return random.sample(range(10**(length-1), 10**length), 1)[0]
#
# def _verify_pin(mobile_number, pin):
#     """ Verify a PIN is correct """
#     # return pin == cache.get(mobile_number)
#
# def ajax_send_pin(request):
#     """ Sends SMS PIN to the specified number """
#     mobile_number = request.POST.get('mobile_number', "")
#     if not mobile_number:
#         return HttpResponse("No mobile number", mimetype='text/plain', status=403)
#
#     pin = _get_pin()
#
#     # store the PIN in the cache for later verification.
#     # cache.set(mobile_number, pin, 24*3600) # valid for 24 hrs
#
#     client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#     message = client.messages.create(
#                         body ="%s" % pin,
#                         to=mobile_number,
#                         from_=settings.TWILIO_FROM_NUMBER,
#                     )
#     return HttpResponse("Message %s sent" % message.sid, mimetype='text/plain', status=200)

def RegistrationView(request, usertype):
    if usertype in ["consumer", "shopadmin"]:
        context = {"userType": usertype}
        registered = False
        if request.method == 'POST':
            user_form = UserProfileForm(data=request.POST)
            context['user_form'] = user_form
            if user_form.is_valid():
                # pin = int(request.POST.get("pin", "0"))
                # mobile_number = request.POST.get("mobile_number", "")
                # if _verify_pin(mobile_number, pin):
                user = user_form.save()
                user.set_password(user.password)
                g = Group.objects.get(name=usertype)
                g.user_set.add(user)
                user.save()
                registered = True
                # else:
                #     messages.error(request, "Invalid PIN!")

            #else:
                #context["user_form_errors"] = user_form.errors
        else:
            user_form = UserProfileForm()
            context['user_form'] = user_form
        context["registered"] = registered
        if registered:
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
        return render_to_response("core/registration.html", context, context_instance=RequestContext(request))
    else:
        return HttpResponse("invalid user type provided")#TODO replace with 404 error


@login_required
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:login'))