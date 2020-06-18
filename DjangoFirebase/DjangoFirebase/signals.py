from django.db.models.signals import post_save
from django.dispatch import receiver
from firebase_admin import messaging
from firebase_admin.messaging import ApiCallError

from pager.firebase import firebase_app
from pager.models import Alarm, Device

'''
https://github.com/kvn-stgl/openPagerServer/blob/060306b90b34165a4fd87c53eba8b9f85edc0f00/pager/signals.py
'''



@receiver(post_save, sender=Alarm)
def send_alarm(sender, instance, created, **kwargs):
    if created:
        devices = Device.objects.filter(owner_id__in=instance.organization.members.all())
        message = messaging.Message(
            notification=messaging.Notification(
                title=instance.title,
                body=instance.message,
            )
        )

        error_tokens = []

        for device in devices:
            message.token = device.fcm_token

            try:
                messaging.send(message, app=firebase_app, dry_run=False)
            except ApiCallError as err:
                code = err.code

                # Old error list
                # error_list = ['MissingRegistration', 'MismatchSenderId', 'InvalidRegistration', 'NotRegistered']

                error_list = ['invalid-registration-token',
                              'registration-token-not-registered',
                              'invalid-package-name',
                              'invalid-recipient',
                              'invalid-argument']
                if code in error_list:
                    error_tokens.append(device.fcm_token)

        # delete all devices with invalid recipients
        if error_tokens:
            Device.objects.filter(fcm_token__in=error_tokens).delete()