# this file aims to help you to get motivated in python by showing you some quotes
# and some tips to continue learning python and become a better programmer

# we create a list of quotes
quotes = ['Do the best you can, where you are, with what you have.',
          'If you can dream it, you can do it.',
          'If you set your goals ridiculously high and it\'s a failure, you will fail above everyone else\'s success.',
          'The only way to do great work is to love what you do.',
          'The only person you are destined to become is the person you decide to be.',
          'The best and most beautiful things in the world cannot be seen, nor touched, nor heard, but are felt in the heart.',
          'The best is yet to come.',
          'I find that the harder I work, the more luck I seem to have.',
          'If you don\'t stand for something you will fall for anything.',
          'I have not failed. I\'ve just found 10,000 ways that won\'t work.',
          'There is no failure except in no longer trying.',
          'I have not failed. I\'ve just found 10,000 ways that won\'t work.',
          'Do not fear failure, do not worry about it. You will be successful.',
          'There is no such thing as failing. It is an extremely dull and irritating time for most people.',
          'If you think you can do a thing or think it cannot be done, you\'re right.',
          'I can\'t change the direction of the wind, but I can adjust my sails to always reach my destination.',
          'I\'m the biggest success on the planet.',
          'Don\'t worry about failure, worry about the chances you miss when you don\'t even try.',
          'The best way to predict your future is to create it.',
          'If you don\'t like something, change it. If you can\'t change it, change your attitude.',
          'I don\'t know the key to success, but the key to failure is trying to please everybody.',
          'If you are not willing to risk the usual you will have to settle for the ordinary.',
          'If you can\'t explain it simply, you don\'t understand it well enough.',
          'If you don\'t know where you are going, you will probably end up'
]


# we create a function to show a random quote
def show_quote():
    # we use the random module to select a random quote
    import random
    print(random.choice(quotes))

# ask the user if he wants to see a quote
answer = input('Do you want to see a quote? (y/n) ')
# if the user wants to see a quote
if answer == 'y':
    # we show a random quote
    show_quote()
# if the user doesn't want to see a quote
else:
    # we show a message saying goodbye
    print('Goodbye!')
