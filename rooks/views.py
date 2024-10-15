from django.shortcuts import render

def index(request):
    # This function will render the index.html file
    return render(request, 'index.html')

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    return True

def solve_rooks_util(board, col):
    if col >= 8:
        return True

    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_rooks_util(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solve_rooks(request):
    board = [[0 for _ in range(8)] for _ in range(8)]
    solve_rooks_util(board, 0)
    return render(request, 'rooks/index.html', {'board': board})
