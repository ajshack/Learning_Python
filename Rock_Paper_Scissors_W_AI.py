from random import randint
print('....rock....')
print('....paper....')
print('....scissors....')

player = input('Enter your move: ').lower()
rand_num = randint(0, 2)
if rand_num == 0:
    computer = 'rock'
elif rand_num == 1:
    computer = 'paper'
else:
    computer = 'scissors'
print(f'Computer plays {computer}')
print('SHOOT!')

if player == computer:
    print('TIE!!!')
elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') \
        or player == 'scissors' and computer == 'paper':
    print('Player Wins!!')
else:
    print('Computer Wins!!')

    # if player == 'rock' and computer == 'scissors':
#     print('Player One Wins!!')
# elif P1Choice == 'paper' and P2Choice == 'rock':
#     print('Player One Wins!!')
# elif P1Choice == 'scissors' and P2Choice == 'paper':
#     print('Player One Wins!!')
# elif P1Choice == P2Choice:
#     print('TIE!!!')
# else:
#     print('Player Two Wins!!')
