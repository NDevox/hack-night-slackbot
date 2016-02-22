import datetime
import time

from slacker import Slacker

SLACK = Slacker('xoxp-22553246598-22551165396-22557262081-2adaa923c5')

quotes = {'Groucho Marx': ['A likely story — and probably true.', "Although it is generally known, I think it's about time to announce that I was born at a very early age.",
                           "I sent the club a wire stating, 'PLEASE ACCEPT MY RESIGNATION. I DON'T WANT TO BELONG TO ANY CLUB THAT WILL ACCEPT PEOPLE LIKE ME AS A MEMBER'",
                           "I never forget a face, but in your case I'll be glad to make an exception.", "From the moment I picked your book up until I laid it down I was convulsed with laughter. Someday I intend on reading it.",
                           'I find television very educational. Every time someone switches it on I go into another room and read a good book.',
                           "Die, my dear? Why that's the last thing I'll do!"],
          'Winston Churchill': ['I may be drunk, Miss, but in the morning I will be sober and you will still be ugly.', 'Courage is what it takes to stand up and speak; courage is also what it takes to sit down and listen.',
                                'Success is not final, failure is not fatal: it is the courage to continue that counts.', 'To improve is to change; to be perfect is to change often.',
                                'Attitude is a little thing that makes a big difference.'],
          'Mark Twain': ["If you tell the truth, you don't have to remember anything.", "Good friends, good books, and a sleepy conscience: this is the ideal life",
                         "The man who does not read has no advantage over the man who cannot read.", "Never put off till tomorrow what may be done day after tomorrow just as well.",
                         "I have never let my schooling interfere with my education.", "′Classic′ - a book which people praise and don't read.",
                         "The fear of death follows from the fear of life. A man who lives fully is prepared to die at any time.",
                         "Never tell the truth to people who are not worthy of it."],
          'Albert Einstein' : ["You can't blame gravity for falling in love.",
                               "Insanity: doing the same thing over and over again and expecting different results.",
                               "You have to learn the rules of the game. And then you have to play better than anyone else.",
                               "Learn from yesterday, live for today, hope for tomorrow. The important thing is not to stop questioning.",
                               "The true sign of intelligence is not knowledge but imagination.",
                               'Look deep into nature, and then you will understand everything better.',
                               'The true sign of intelligence is not knowledge but imagination.',
                               "When you are courting a nice girl an hour seems like a second. When you sit on a red-hot cinder a second seems like an hour. That's relativity.",
                               "Try not to become a man of success, but rather try to become a man of value."]}


def search_messages():
    oldest = (datetime.datetime.now() - datetime.datetime.utcfromtimestamp(0)).total_seconds() - 5
    return SLACK.channels.history('C0NG2P3SQ', oldest=oldest)


def get_username(user):
    return SLACK.users.info(user).body['user']['name']


def get_groups(msg):
    words = msg.split(' ')

    options = []

    if len(words) > 2:
        for x in range(len(words) - 2):
            options.append(' '.join(words[x:x+3]))

    return options


def main():

    for message in search_messages().body['messages']:
        for grouping in get_groups(message['text']):
            for person in quotes:
                for quote in quotes[person]:
                    if grouping.lower() in quote.lower():
                        user = get_username(message['user'])
                        SLACK.chat.post_message('#general', '@' + user + ': ' + quote + ' - ' + person,
                                                as_user=True)

if __name__ == '__main__':
    while True:
        main()

        time.sleep(5)