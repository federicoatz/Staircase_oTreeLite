
from otree.api import *
c = cu

doc = 'Staircase risk task: Falk, A., et al. (2018).'
class C(BaseConstants):
    NAME_IN_URL = 'RiskAssessment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5
    NUM_CHOICES = 5
    PROBABILITY = 50
    DELTA = 80
    BUTTONS = True
    PROGRESS_BAR = True
    INDIFFERENCE = False
    LOTTERY_HI = 300
    SURE_PAYOFF = 160
    LOTTERY_LO = 0
class Subsession(BaseSubsession):
    pass
def creating_session(subsession: Subsession):
    session = subsession.session
    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.vars['icl_sure_payoffs'] = [(C.SURE_PAYOFF)]
            p.participant.vars['icl_switching_row'] = 2 ** C.NUM_CHOICES
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    random_draw = models.IntegerField()
    payoff_relevant = models.StringField()
    choice = models.StringField()
    switching_row = models.IntegerField()
    sure_payoff = models.FloatField()
def set_sure_payoffs(player: Player):
    participant = player.participant
    player.sure_payoff = participant.vars['icl_sure_payoffs'][player.round_number - 1]
    
    # determine sure payoff for next choice and append list of sure payoffs
    if not player.round_number == C.NUM_CHOICES:
        if player.choice == 'A':
            participant.vars['icl_sure_payoffs'].append(
                       (participant.vars['icl_sure_payoffs'][player.round_number - 1]
                        + C.DELTA / 2 ** (player.round_number - 1))
                    )
        elif player.choice == 'B':
            participant.vars['icl_sure_payoffs'].append(
                       (participant.vars['icl_sure_payoffs'][player.round_number - 1]
                        - C.DELTA / 2 ** (player.round_number - 1))
                    )
    else:
        pass
def update_switching_row(player: Player):
    participant = player.participant
    if player.choice == 'B':
        participant.vars['icl_switching_row'] -= 2 ** (C.NUM_CHOICES - player.round_number)
    
    elif player.choice == 'I':
        participant.vars['icl_switching_row'] /= 2
def set_payoffs(player: Player):
    session = player.session
    subsession = player.subsession
    participant = player.participant
    import random
    
    current_round = subsession.round_number
    current_choice = player.in_round(current_round).choice
    
    # set payoff if all choices have been completed or if "indifferent" was chosen
    if current_round == C.NUM_ROUNDS or current_choice == 'I':
        completed_choices = len(participant.vars['icl_sure_payoffs'])
        participant.vars['icl_choice_to_pay'] = random.randint(1, completed_choices)
        choice_to_pay = participant.vars['icl_choice_to_pay']
    
        player.in_round(choice_to_pay).random_draw = random.randint(1, 100)
    
        player.in_round(choice_to_pay).payoff_relevant = random.choice(['A','B']) \
            if player.in_round(choice_to_pay).choice == 'I' \
            else player.in_round(choice_to_pay).choice
    
    # set player's payoff
        if player.in_round(choice_to_pay).payoff_relevant == 'A':
            player.in_round(choice_to_pay).payoff = C.LOTTERY_HI \
                if player.in_round(choice_to_pay).random_draw <= C.PROBABILITY \
                else C.LOTTERY_LO
        elif player.in_round(choice_to_pay).payoff_relevant == 'B':
            player.in_round(choice_to_pay).payoff = player.participant.vars['icl_sure_payoffs'][choice_to_pay - 1]
    
    # set payoff as global variable
    
        participant.vars['icl_payoff'] = player.in_round(choice_to_pay).payoff
        player.payoff = participant.vars['icl_payoff']
        player.in_round(choice_to_pay).switching_row = participant.vars['icl_switching_row']
class Instructions(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class Decision(Page):
    form_model = 'player'
    form_fields = ['choice']
    @staticmethod
    def is_displayed(player: Player):
        previous_choices = [p.choice for p in player.in_previous_rounds()]
        return 'I' not in previous_choices
    @staticmethod
    def vars_for_template(player: Player):
        session = player.session
        subsession = player.subsession
        participant = player.participant
        total = C.NUM_CHOICES
        page = subsession.round_number
        progress = page / total * 100
        
        return {
            'page':        page,
            'total':       total,
            'progress':    progress,
            'sure_payoff': participant.vars['icl_sure_payoffs'][page - 1],
            'p_hi': "{0:.1f}".format(C.PROBABILITY) + "%",
            'p_lo': "{0:.1f}".format(100 - C.PROBABILITY) + "%",
            'hi':   (C.LOTTERY_HI),
            'lo':   (C.LOTTERY_LO)
                }
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_sure_payoffs(player)
        set_payoffs(player)
        update_switching_row(player)
class Results(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        session = player.session
        subsession = player.subsession
        return subsession.round_number == C.NUM_ROUNDS
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        choice_to_pay = participant.vars['icl_choice_to_pay']
        option_to_pay = player.in_round(choice_to_pay).choice
        payoff_relevant = player.in_round(choice_to_pay).payoff_relevant
        sure_payoff = player.participant.vars['icl_sure_payoffs'][choice_to_pay - 1]
        
        return {
            'sure_payoff':     sure_payoff,
            'option_to_pay':   option_to_pay,
            'payoff_relevant': payoff_relevant,
            'payoff':          player.in_round(choice_to_pay).payoff,
            'p_hi': "{0:.1f}".format(C.PROBABILITY) + "%",
            'p_lo': "{0:.1f}".format(100 - C.PROBABILITY) + "%",
            'hi':   C.LOTTERY_HI,
            'lo':   C.LOTTERY_LO
            }
page_sequence = [Instructions, Decision, Results]