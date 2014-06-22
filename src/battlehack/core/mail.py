from django.core.mail import send_mail


def send_rival_email(to, url):
    msg = '\n'.join([
        'Hello!',
        '',
        'You have been intited to a challenge at Cha+Cha.',
        url,
        '',
        'Good luck!,',
    ])
    send_mail(
        'Invitation to Cha+Cha',
        msg, 'pappeldackel@googlemail.com', [to], fail_silently=False)
