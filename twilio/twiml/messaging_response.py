# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

import json
from twilio.twiml import (
    TwiML,
    format_language,
    GenericNode
)


class MessagingResponse(TwiML):
    """ <Response> TwiML for Messages """

    def __init__(self, **kwargs):
        super(MessagingResponse, self).__init__(**kwargs)
        self.name = 'Response'

    def message(self, body=None, to=None, from_=None, action=None, method=None,
                status_callback=None, **kwargs):
        """
        Create a <Message> element

        :param body: Message Body
        :param to: Phone Number to send Message to
        :param from: Phone Number to send Message from
        :param action: Action URL
        :param method: Action URL Method
        :param status_callback: Status callback URL. Deprecated in favor of action.
        :param kwargs: additional attributes

        :returns: <Message> element
        """
        return self.nest(Message(
            body=body,
            to=to,
            from_=from_,
            action=action,
            method=method,
            status_callback=status_callback,
            **kwargs
        ))

    def redirect(self, url, method=None, **kwargs):
        """
        Create a <Redirect> element

        :param url: Redirect URL
        :param method: Redirect URL method
        :param kwargs: additional attributes

        :returns: <Redirect> element
        """
        return self.nest(Redirect(url, method=method, **kwargs))


class Redirect(TwiML):
    """ <Redirect> TwiML Verb """

    def __init__(self, url, **kwargs):
        super(Redirect, self).__init__(**kwargs)
        self.name = 'Redirect'
        self.value = url


class Message(TwiML):
    """ <Message> TwiML Verb """

    def __init__(self, body=None, **kwargs):
        super(Message, self).__init__(**kwargs)
        self.name = 'Message'
        if body:
            self.value = body

    def body(self, message, **kwargs):
        """
        Create a <Body> element

        :param message: Message Body
        :param kwargs: additional attributes

        :returns: <Body> element
        """
        return self.nest(Body(message, **kwargs))

    def media(self, url, **kwargs):
        """
        Create a <Media> element

        :param url: Media URL
        :param kwargs: additional attributes

        :returns: <Media> element
        """
        return self.nest(Media(url, **kwargs))


class Media(TwiML):
    """ <Media> TwiML Noun """

    def __init__(self, url, **kwargs):
        super(Media, self).__init__(**kwargs)
        self.name = 'Media'
        self.value = url


class Body(TwiML):
    """ <Body> TwiML Noun """

    def __init__(self, message, **kwargs):
        super(Body, self).__init__(**kwargs)
        self.name = 'Body'
        self.value = message
