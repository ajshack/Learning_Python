print('....rock....')
print('....paper....')
print('....scissors....')

P1Choice = input('Enter your move: ')

print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')
print(' **** NO CHEATING *****')

P2Choice = input('Enter your move: ')

print('SHOOT!')

# if P1Choice == 'rock' and P2Choice == 'scissors':
#     print('Player One Wins!!')
# elif P1Choice == 'paper' and P2Choice == 'rock':
#     print('Player One Wins!!')
# elif P1Choice == 'scissors' and P2Choice == 'paper':
#     print('Player One Wins!!')
# elif P1Choice == P2Choice:
#     print('TIE!!!')
# else:
#     print('Player Two Wins!!')

if (P1Choice == 'rock' and P2Choice == 'scissors') or (P1Choice == 'paper' and P2Choice == 'rock') \
        or P1Choice == 'scissors' and P2Choice == 'paper':
    print('Player One Wins!!')
elif P1Choice == P2Choice:
    print('TIE!!!')
else:
    print('Player Two Wins!!')
