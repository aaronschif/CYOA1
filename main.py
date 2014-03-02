

# response = None
#
# while not response ==


story = {
    'Intro':
    (
        '''
        Many generations ago, the evil warlord Tyra pillaged many villages and conquered many lands in
        the name of evil. She was defeated by an uncommonly small hobbit named Tallin. This hobbit is your ancestor.
        In the present day, thou art a small hobbit. You are reading up on the aspects of quantum physics, because the apple falls
        uncommonly far from the tree in this universe. You hear a knock on the door. What do you do?
        ''',
        ["Go back to reading physics. It's getting to the good part!", 'Answer the door.']
    ),
    'Answer the door.':
    (
        '''
        It is a old man in a pointy hat. He yells at you unintelligibly while waving his hands wildly. Just as you are
        about to close the door, an attractive she-hobbit sprinting down the lane calls to the both of you. "There you are,
        grandfather!", she reaches you. "Thank you so much for finding him!"
        ''',
        ["Go back to reading physics. It's getting to the good part!"]
    ),
    "Go back to reading physics. It's getting to the good part!":
    (
        '''

        ''',
        None
    )
}

response = 'Intro'

while not response == 'Quit':
    body = story[response][0]
    print body
    response = raw_input('> ')

'''
Tell me something.
print> Fish are aquatic.
Fish are aquatic? How interesting! Why?
> Because they like to be.
Oh. Well that's boring.
>Yeah
'''