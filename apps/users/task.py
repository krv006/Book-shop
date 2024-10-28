import time

from celery import shared_task
from django.core.mail import send_mail
from django.core.cache import cache
from root.settings import EMAIL_HOST_USER


@shared_task
def delete_cache_task(cache_key):
    cache.delete(cache_key)
    print(f"Cache key {cache_key} successfully deleted.")
    return f"Cache key {cache_key} successfully deleted."


@shared_task
def send_activation_email_task(subject, message, recipient_list, html_message):
    for recipient in recipient_list:
        cache_key = f'activation_email:{recipient}'
        cache.set(cache_key, message, timeout=60)
        cached_message = cache.get(cache_key)
        print(f"Cache set for {recipient}: {cached_message}")
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], html_message=html_message)
        print(f"Email sent to {recipient}.")
        delete_cache_task.apply_async((cache_key,), countdown=60)
    return f"Emails sent to {', '.join(recipient_list)} and cache keys created."


# todo for high(is_premium for user)
@shared_task
def send_activation_email_task1(subject, message, recipient, html_message):
    print(f"({recipient}) ga yuborish BOSHLANDI")
    time.sleep(3)
    send_mail(subject, message, EMAIL_HOST_USER, [recipient], html_message=html_message)
    time.sleep(3)
    print(f"({recipient}) ga yuborish TUGADI")
    return f"Emails sent to recipient"

# def delete_cache_task(cache_key):
#     cache.delete(cache_key)
#     return f"Cache key {cache_key} successfully deleted."
#
#
# @shared_task
# def send_activation_email_task(subject, message, recipient_list, html_message):
#     for recipient in recipient_list:
#         cache_key = f'activation_email:{recipient}'
#         cache.set(cache_key, message, timeout=60)
#         send_mail(subject, message, EMAIL_HOST_USER, [recipient], html_message=html_message)
#         delete_cache_task.apply_async((cache_key,), countdown=60)
#     return f"Emails sent to {', '.join(recipient_list)} and cache keys created."
