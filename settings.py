from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0, participation_fee=0)
SESSION_CONFIGS = [dict(name='Global', num_demo_participants=20, app_sequence=['RiskAssessment']), dict(name='Lottery', num_demo_participants=None, app_sequence=['RiskAssessment'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['icl_sure_payoffs', 'icl_switching_row', 'icl_payoff']
SESSION_FIELDS = []
ROOMS =

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


