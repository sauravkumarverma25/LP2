import random


responses = {
    'hello': ['Hi there!', 'Hello!', 'Hey!', 'Greetings!'],
    'how are you': ['I\'m doing well, thank you!', 'I\'m fine, thanks for asking.', 'I\'m great!'],
    'what is your name': ['My name is ChatBot.', 'I\'m ChatBot!', 'I\'m your personal ChatBot.'],
    'default': ['Sorry, I didn\'t understand what you said.', 'Could you please rephrase that?', 'I\'m not sure what you mean.']
}


def generate_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses['default'])


def main():
    print('Hello! I\'m ChatBot. How can I help you today?')
    while True:
        user_input = input('> ')
        if user_input == 'bye':
            print('Goodbye!')
            break
        response = generate_response(user_input)
        print(response)


if __name__ == '__main__':
    main()
