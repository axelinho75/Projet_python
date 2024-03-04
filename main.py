import random

def print_board(board):
    for row in board:
        print('|'.join(row))



def get_player_move(board):
    while True:
        try:
            ligne = int(input('Entrez la ligne ')) - 1
            colone = int(input('Entrez la colone ')) -1
            if ligne in range(3) and colone in range(3) and board[ligne][colone] == ' ':
                return (ligne, colone)
            else:
                print('Entrée une valeur valide')
        except ValueError:
            print('Entrée une valeur valide')


def check_win(board):
    for ligne in board:
        if ligne.count(ligne[0]) == len(ligne) and ligne[0] != ' ':
            return True
    for colone in range(len(board[0])):
        if board[0][colone] == board [1][colone] == board[2][colone] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False


def evaluate(board):
    
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return 1 if row[0] == 'O' else -1

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return 1 if board[0][col] == 'O' else -1

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return 1 if board[0][0] == 'O' else -1
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return 1 if board[0][2] == 'O' else -1

    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 1 or score == -1:
        return score
    if not any(' ' in row for row in board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def get_computer_move(board, difficulty):
    valid_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    
    if not valid_moves:  
        return None

    if difficulty == 'facile':
        move = random.choice(valid_moves)
    elif difficulty == 'moyen':
        if random.random() < 0.5:
            move = get_best_move(board)
        else:
            move = random.choice(valid_moves)
    else:  
        move = get_best_move(board)

    return move

def get_best_move(board):
    best_score = -float('inf')
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move

    
def game():
    scores = {'X': 0, 'O': 0, 'Nul': 0}  # Initialiser les scores

    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        player = 'X'

        mode = input("Choisissez le mode de jeu (1 = un joueur, 2 = deux joueurs): ")
        if mode == '1':
            difficulty = input("Choisissez le niveau de difficulté (facile, moyen, impossible): ")

        while True:
            print_board(board)

            if player == 'X':
                ligne , colone = get_player_move(board)
                board[ligne][colone] = 'X'
            else:
                if mode == '1':
                    move = get_computer_move(board, difficulty)
                    if move is not None:
                        ligne , colone = move
                        board[ligne][colone] = 'O'
                    else:
                        print("Match nul!")
                        scores['Nul'] += 1  # Mettre à jour le score
                        print_board(board)
                        break
                else:
                    ligne , colone = get_player_move(board)
                    board[ligne][colone] = 'O'

            if check_win(board):
                print("Le Joueur", player, "a gagné!")
                scores[player] += 1  # Mettre à jour le score
                print_board(board)
                break

            player = 'O' if player == 'X' else 'X'

        # Afficher les scores et les statistiques
        print("Scores :")
        print("Joueur X:", scores['X'])
        print("Joueur O:", scores['O'])
        print("Matchs nuls:", scores['Nul'])

        replay = input("Voulez-vous rejouer ? (O/N) ")
        if replay.lower() != 'o':
            break

game()






