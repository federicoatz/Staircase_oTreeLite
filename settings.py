from os import environ

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0, participation_fee=0)

SESSION_CONFIGS = [
    dict(name='Global', num_demo_participants=20, app_sequence=['RiskAssessment']),
    dict(name='Lottery', num_demo_participants=None, app_sequence=['RiskAssessment']),
]

# ISO-639 code, e.g. en, de, fr, it
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

DEMO_PAGE_INTRO_HTML = ''

PARTICIPANT_FIELDS = ['icl_sure_payoffs', 'icl_switching_row', 'icl_payoff']
SESSION_FIELDS = []

ADMIN_USERNAME = 'admin'
# for security, best to set the admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# for security, best to set the secret key in an environment variable in production
SECRET_KEY = environ.get('OTREE_SECRET_KEY', 'dev-only-secret-key-change-me')

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
