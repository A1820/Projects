import random
from time import sleep

def magic_8_ball():
    question = input("please enter your question:\n")

    responses = ['As I see it, yes.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.',
                 'Concentrate and ask again.', 'Don\'t count on it.', 'It is certain.',' It is decidedly so.',
                'Most likely.' ' My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.',
                 'Reply hazy, try again.', 'signs point to yes.','Very doubtful.', 'Without a doubt.', 'Yes',
                 'Yes - definitely.', 'You may rely on it']
    if len(question) < 3:
        print("processing.....")
        print('Input a valid question')
    else:
        print("processing.....")
        sleep(3)
        response = random.choice(responses)
        print("Answer: " + response)

    next = input("Will you like to ask another question or quit? (Input Ask or Quit):\n")

    if next == "Ask":
        magic_8_ball()
    else:
        print("Thank you for playing with us")

magic_8_ball()
