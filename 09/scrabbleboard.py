TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

def make_scrabble_board():
    board=[]
    for i in range(15):
        line=[]
        for i in range(15):
            line.append('_')
        board.append(line)

    for r,c in TRIPLE_WORD_SCORE:
        board[r][c] = 'T'

    for r,c in DOUBLE_WORD_SCORE:
        board[r][c] = 'D'

    for r,c in TRIPLE_LETTER_SCORE:
        board[r][c]='t'

    for r,c in DOUBLE_LETTER_SCORE:
        board[r][c] = 'd'
    return board

def score(w):
    score = 0
    sc_dict = {'one':'aeioulnrst', 'two':'dg', 'three':'bcmp', 'four':'fhvwy', 'five':'k','eight':'jx','ten':'qz'}
    for i in w:
        if i in sc_dict['one']:
            score += 1
        if i in sc_dict['two']:
            score += 2
        if i in sc_dict['three']:
            score += 3
        if i in sc_dict['four']:
            score += 4
        if i in sc_dict['five']:
            score += 5
        if i in sc_dict['eight']:
            score += 8
        if i in sc_dict['ten']:
            score += 10
    return score

def add_word_across(board, word, r, c):
    newboard = board
    global newscore
    newscore = 0
    for i in range(len(word)):
        if board[r-1][c+i-1] == 't':
            newscore += 3 * score(word[i])
        elif board[r-1][c+i-1] == 'd':
            newscore += 2 * score(word[i])
        else:
            newscore += score(word[i])
        if 'T' in board[r-1][c-1:c-1+len(word)]:
            newscore = newscore * 3
        elif 'D' in board[r-1][c-1:c-1+len(word)]:
            newscore = newscore * 2
        newboard[r-1][c+i-1] = word[i]
    print_board(newboard)
    return newscore

def add_word_down(board, word, r, c):
    newboard = board
    global newscore
    newscore = 0
    for i in range(len(word)):
        for j in range(len(board)):
            if board[j][c] == 't':
                newscore += 3 * score(word[i])
            elif board[j][c] == 'd':
                newscore += 2 * score(word[i])
            else:
                newscore += score(word[i])
            newboard[r+i-1][c-1] = word[i]
        for j in range(len(board)):
            if board[j][c] == 'T':
                newscore = newscore * 3
            elif board[j][c] == 'D':
                newscore = newscore * 2
    print_board(newboard)
    return newscore
        
def print_board(b):
    for line in b:
        print ( ' '.join(line))
        
board = make_scrabble_board()
print_board(board)

