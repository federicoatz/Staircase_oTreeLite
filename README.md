# Staircase_oTreeLite

A 'Staircase' risk elicitation method for oTree, based on
[felixholzmeister/icl](https://github.com/felixholzmeister/icl), reimplemented for
oTree v6.

Participants face a sequence of binary choices between a lottery ("Option A") and a
sure payment ("Option B"). The sure payment adjusts up or down after each choice,
converging on the participant's switching point between the two options. One choice
is randomly selected at the end to determine the payoff.

Note that the "indifferent" option is disabled by default (`C.INDIFFERENCE = False`
in `RiskAssessment/__init__.py`). Set it to `True` to offer that third choice.

## Project layout

```
settings.py           project settings (session configs, currency, admin credentials)
requirements.txt       Python dependencies
Procfile                process types for Heroku-style deployment
runtime.txt             Python version for Heroku-style deployment
_static/global/          project-wide static assets (style.css)
_templates/global/       project-wide template overrides (loads style.css)
RiskAssessment/           the oTree app
    __init__.py             models and page logic
    tests.py                 bot test
    Instructions.html        instructions page
    Decision.html            binary choice page
    Results.html             payoff summary page
```

## Running locally

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export OTREE_ADMIN_PASSWORD=your-password
otree devserver
```

Then open http://localhost:8000 and start a demo session ("Global" or "Lottery").

## Running the bot test

```
otree test Global 1
```

## Deployment

The repository is set up for a Heroku-style deployment (`Procfile`, `runtime.txt`,
`requirements.txt`). Set `OTREE_ADMIN_PASSWORD` and `OTREE_SECRET_KEY` as environment
variables in production rather than relying on the defaults in `settings.py`.

## License

MIT — see [LICENSE](LICENSE).
