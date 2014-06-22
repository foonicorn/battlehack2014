from django.core.mail import send_mail


def send_rival_email(to, url, title):
    msg = '\n'.join([
        'Hello!',
        '',
        'You have been intited to a challenge at Cha+Cha.',
        url,
        '',
        'Good luck!,',
    ])
    send_mail(
        'Cha+Cha: ' + title,
        msg, 'andreas.hug@moccu.com', [to], fail_silently=False)
