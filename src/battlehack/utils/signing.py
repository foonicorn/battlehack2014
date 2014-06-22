from django.core.signing import Signer


signer = Signer(sep='.')
sign = signer.sign
unsign = signer.unsign
