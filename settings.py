from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0, participation_fee=6)
SESSION_CONFIGS = [dict(name='Global', num_demo_participants=20, app_sequence=['RiskAssessment']), dict(name='Lottery', num_demo_participants=None, app_sequence=['RiskAssessment'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['icl_sure_payoffs', 'icl_switching_row', 'icl_payoff']
SESSION_FIELDS = []
ROOMS = [dict(name='Demo', display_name='Demo', participant_label_file='_rooms/Demo.txt'), dict(name='SESSION1', display_name='SESSION1', participant_label_file='_rooms/SESSION1.txt'), dict(name='SESSION2', display_name='SESSION2', participant_label_file='_rooms/SESSION2.txt'), dict(name='SESSION3', display_name='SESSION3', participant_label_file='_rooms/SESSION3.txt'), dict(name='SESSION4', display_name='SESSION4', participant_label_file='_rooms/SESSION4.txt'), dict(name='SESSION5', display_name='SESSION5', participant_label_file='_rooms/SESSION5.txt')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


