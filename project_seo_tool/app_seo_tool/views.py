
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from global_login_required import login_not_required

from app_seo_tool import forms as app_seo_tool_forms

# Sign-In / Sign-Up / Activation / Reset Password
def activation(request, uidb64, token):
    """
    """

    print("activation function")

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print(user)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        print("exception")
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        print("user is not None")
        user.is_active = True
        user.save()

        return redirect('cms:custom_login')

    else:
        print("user is None")
        print('Activation link is invalid!')
        return redirect('cms:home')


def password_reset(request):
    """
    """

    print("password reset function")

    if request.method == 'POST':
        print("post")

        form = cms_forms.ResetForm(request.POST)
        if form.is_valid():
            print("valid form")
            data = form.cleaned_data
            print(data['username'])

            user = User.objects.get(
                Q(username=data['username']) |
                Q(email=data['username']))

            if user is not None:
                print("user exist")
                if user.is_active:
                    print("user active")

                    current_site = get_current_site(request)
                    subject = 'Restablecer contraseña - Salamanca CMS'
                    from_email = settings.EMAIL_HOST_USER
                    to_email = [user.email,]
                    message = render_to_string('email_password_reset.txt', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                        'token': account_activation_token.make_token(user),
                    })
                    send_mail(subject, message, from_email, to_email, fail_silently=False,)

                else:
                    print("user not active")
            else:
                print("user not exist")
        else:
            print(form.errors)

        return redirect('cms:home')

    else:
        print("get")
        form = cms_forms.ResetForm()

    return render(request, 'password_reset.html', {
        'form': form,
    })


def password_reset_form(request, uidb64=None, token=None):
    """
    """

    print("passwrod reset form function")

    user = None

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        print(user)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        print("user not existe")
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'GET':
            print("get")
            form = cms_forms.ResetPasswordForm(initial={'username': user.username})

    else:
        if request.method == 'POST':
            print("post")

            form = cms_forms.ResetPasswordForm(request.POST)
            if form.is_valid():
                print("valid form")
                data = form.cleaned_data
                user = User.objects.get(username=data['username'])

                if data['password1'] == data['password2']:
                    print(data['password1'])
                    user.set_password(data['password1'])
                    user.save()

                current_site = get_current_site(request)
                subject = 'Confirmación - Salamanca CMS'
                from_email = settings.EMAIL_HOST_USER
                to_email = [user.email,]
                message = render_to_string('email_activation.txt', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    'token': account_activation_token.make_token(user),
                })
                send_mail(subject, message, from_email, to_email, fail_silently=False,)

                return redirect('cms:home')

            else:
                print(form.errors)

    print(user)

    return render(request, 'password_reset_form.html', {
        'form': form,
    })


@login_not_required
def custom_login(request):
    """
    """

    title = 'Acceso'
    if request.method == 'POST':
        form = app_seo_tool_forms.LoginForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return redirect('panel:result_list')

    else:
        form = app_seo_tool_forms.LoginForm()

    return render(request, 'login.html', {
        'title': title,
        'form': form,
    })


# General Views
@login_not_required
def home(request):
    """
    """

    return render(request, 'home.html', {})


def result_list(request):
    """
    """

    return render(request, 'list.html', {})


def search_list(request):
    """
    """

    return render(request, 'list.html', {})




#
