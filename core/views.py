from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import loader
from django.template.context import RequestContext
from shops.forms import ShopProfileForm
from users.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
# from users.models import FbUser

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



def RegistrationView(request, usertype):
    if usertype in ["consumer", "shopadmin"]:
        context = {"userType": usertype}
        registered = False
        if request.method == 'POST':
            user_form = UserProfileForm(data=request.POST)
            context['user_form'] = user_form
            if user_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                g = Group.objects.get(name=usertype)
                g.user_set.add(user)
                user.save()
                registered = True
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


# def cart_context_processor(request):
#     cart = Cart(request)
#     return { 'cart_item_count' : cart.item_count }

@login_required
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:login'))