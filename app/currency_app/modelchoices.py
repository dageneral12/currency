
TYPE_USD = 'USD'
TYPE_EUR = 'EUR'
TYPE_UAH = 'UAH'
TYPE_RUB = 'RUB'
TYPE_GBP = 'GBP'
TYPE_CHF = 'CHF'

RATE_CHOICES = (
    (TYPE_USD, 'Dollar'),
    (TYPE_EUR, 'Euro'),
    (TYPE_UAH, 'Hryvna'),
    (TYPE_RUB, 'Ruble'),
    (TYPE_GBP, 'Pound'),
    (TYPE_CHF, 'Franc')
     )

REQUEST_METHODS = (
    ('post', 'POST'),
    ('get', 'GET')
)
