import os


def get_env():
    """
    env = dict()
    env['HUBSPOT_CLIENT_ID'] = os.environ.get('HUBSPOT_CLIENT_ID')
    env['HUBSPOT_CLIENT_SECRET'] = os.environ.get('HUBSPOT_CLIENT_SECRET')
    env['HUBSPOT_OAUTH_URL'] = os.environ.get('HUBSPOT_OAUTH_URL')
    """
    env = {
        'HUBSPOT_CLIENT_ID': '60189b5a-796b-4371-92ab-c681d3ad91ca',
        'HUBSPOT_CLIENT_SECRET': 'a242b4b9-d725-43a6-91d0-f33f0b463d2c',
        'HUBSPOT_OAUTH_URL': 'https://app.hubspot.com/oauth/authorize?client_id=60189b5a-796b-4371-92ab-c681d3ad91ca&redirect_uri=http://localhost:8000/home/&scope=crm.objects.contacts.read%20crm.objects.contacts.write',
    }
    return env
