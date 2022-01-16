def game(numbers):
    game_state = 'on'
    moves = 0
    while game_state != 'done':
        
        print(moves)
        board(numbers)
        player_one = int(input('choose your cell: '))
        player_one_index = player_one - 1

        if numbers[player_one_index] != 'x' and numbers[player_one_index] != 'o':
        
            if player_one:
                numbers[player_one_index] = 'x'
                moves += 1
                if moves == 9:
                    print('draw')
                    break
                if winner(numbers):
                    game_state = 'done'
                    board(numbers)
                    print('winner')
                    break

            board(numbers)
            player_two = int(input('choose your cell: '))
            player_two_index = player_two - 1

            if player_two:
                numbers[player_two_index] = 'o'
                moves += 1
                if winner(numbers):
                    game_state = 'done'
                    board(numbers)
                    print('winner')
                    break
        
        print('cell is taken')




    


def board(numbers):
    print(f"""
___________
   |   |
 {numbers[0]} | {numbers[1]} | {numbers[2]} 
___|___|___
   |   |
 {numbers[3]} | {numbers[4]} | {numbers[5]}
___|___|___
   |   |  
 {numbers[6]} | {numbers[7]} | {numbers[8]} 
___|___|___    
""")

def winner(numbers):
    return (numbers[0] == numbers[1] == numbers[2] or
            numbers[3] == numbers[4] == numbers[5] or
            numbers[6] == numbers[7] == numbers[8] or
            numbers[0] == numbers[3] == numbers[6] or
            numbers[1] == numbers[4] == numbers[7] or
            numbers[2] == numbers[5] == numbers[8] or
            numbers[0] == numbers[4] == numbers[8] or
            numbers[2] == numbers[4] == numbers[6]) 



def main():
    numbers = ['1','2','3','4','5','6','7','8','9']
    game(numbers)

if __name__ == '__main__':
    main()