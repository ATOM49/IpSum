__author__ = 'abhilash.mirji'

from twilio.util import TwilioCapability

def build_twilio_token(client_name):

    account_sid = 'AC9dbcad82b20275e6e1854351444f13c3'
    auth_token = 'd5eb94487e911314e5620b4ea18e6d74'

    capability = TwilioCapability(account_sid, auth_token)
    app_sid = 'AP4679912e15024febe5d6d1fc814e7c7d'

    capability.allow_client_outgoing(app_sid)
    capability.allow_client_incoming(client_name)

    return capability.generate()