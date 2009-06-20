"""
PyTextMagicSMS
==============

This module provides a convenient interface to the TextMagic HTTPS API for
sending SMS messages.

To use the service, you need to create an account at http://www.textmagic.com/
to get a username. Once you are registered, you can retrieve your API password
from https://www.textmagic.com/app/wt/account/api/cmd/password

The TextMagic HTTPS API is described at http://api.textmagic.com/https-api

Currently implemented commands are:
    send
    account
    message_status
    receive
    delete_reply

Outstanding functionality (coming soon) is:
    send_time parameter for send command
    check_number command

Getting started
===============

To send a message:
    client = textmagic.client.TextMagicClient('username', 'password')
    result = client.send("A test message", "9991234444")
    message_id = result['message_id']

Use the message_id to get the delivery status of your message:
    response = client.message_status(message_id)
    status = response['status']

You can receive reply messages from your TextMagic Inbox:
    response = client.receive("0")
    for message in response['messages']:
        from_number = message['from']
        text = message['text']

"""

def import_json():
    try:
        import simplejson as json
    except ImportError:
        try:
            import json
        except ImportError:
            try:
                from django.utils import simplejson as json
            except:
                raise ImportError("Requires either simplejson, Python 2.6 or django.utils!")
    return json
