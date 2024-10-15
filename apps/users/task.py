from celery import shared_task
from django.core.mail import send_mail
from django.core.cache import cache
from root.settings import EMAIL_HOST_USER


@shared_task
def delete_cache_task(cache_key):
    cache.delete(cache_key)
    return f"Cache key {cache_key} successfully deleted."


@shared_task
def send_activation_email_task(subject, message, recipient_list, html_message):
    for recipient in recipient_list:
        cache_key = f'activation_email:{recipient}'
        cache.set(cache_key, message, timeout=60)
        cached_message = cache.get(cache_key)
        print(f"Cache set for {recipient}: {cached_message}")
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], html_message=html_message)
        delete_cache_task.apply_async((cache_key,), countdown=60)

    return f"Emails sent to {', '.join(recipient_list)} and cache keys created."

# @shared_task
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
