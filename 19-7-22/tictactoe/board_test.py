from board import Board
from cell import Cell

board = Board.createBoard()

def test_setCellX():
    board.setCell(0, 0, 'o')
    setSymbol = board.getCell(0, 0)
    assert setSymbol == 'o'

def test_setCellO():
    board.setCell(0, 0, 'o')
    setSymbol = board.getCell(0, 0)
    assert setSymbol == 'o'

def test_rowWinningIndexes():
    row = board.rowWinningIndexes()
    assert row == [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)]]

def test_colWinningIndexes():
    col = board.colWinningIndexes()
    assert col == [
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)]]

def test_diagWinningIndexes():
    diag = board.diagWinningIndexes()
    assert diag == [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]]

def test_isWinningStateReachedO():
    board.cells = [
        [Cell('_'), Cell('_'), Cell('_')],
        [Cell('_'), Cell('_'), Cell('_')],
        [Cell('_'), Cell('_'), Cell('_')]
    ]

    assert board.isWinningStateReached() == (False, None)

    board.cells = [
        [Cell('o'), Cell('o'), Cell('o')],
        [Cell('_'), Cell('_'), Cell('_')],
        [Cell('_'), Cell('_'), Cell('_')]
    ]

    assert board.isWinningStateReached() == (True, 'o')

    board.cells = [
        [Cell('o'), Cell('_'), Cell('_')],
        [Cell('o'), Cell('_'), Cell('_')],
        [Cell('o'), Cell('_'), Cell('_')]
    ]

    assert board.isWinningStateReached() == (True, 'o')

    board.cells = [
        [Cell('o'), Cell('_'), Cell('_')],
        [Cell('_'), Cell('o'), Cell('_')],
        [Cell('_'), Cell('_'), Cell('o')]
    ]

    assert board.isWinningStateReached() == (True, 'o')

def test_isWinningStateReachedX():
    board.cells = [
        [Cell('_'), Cell('_'), Cell('_')],
        [Cell('_'), Cell('_'), Cell('_')],
        [Cell('_'), Cell('_'), Cell('_')]
    ]

    assert board.isWinningStateReached() == (False, None)

    board.cells = [
        [Cell('_'), Cell('_'), Cell('_')],
        [Cell('x'), Cell('x'), Cell('x')],
        [Cell('_'), Cell('_'), Cell('_')]
    ]

    assert board.isWinningStateReached() == (True, 'x')

    board.cells = [
        [Cell('-'), Cell('_'), Cell('x')],
        [Cell('-'), Cell('_'), Cell('x')],
        [Cell('-'), Cell('_'), Cell('x')]
    ]

    assert board.isWinningStateReached() == (True, 'x')

    board.cells = [
        [Cell('_'), Cell('_'), Cell('x')],
        [Cell('_'), Cell('x'), Cell('_')],
        [Cell('x'), Cell('_'), Cell('_')]
    ]

    assert board.isWinningStateReached() == (True, 'x')

def test_isBoardFull():
    board.cells = [
        [Cell('o'), Cell('o'), Cell('x')],
        [Cell('o'), Cell('x'), Cell('_')],
        [Cell('x'), Cell('_'), Cell('_')]
    ]

    assert board.isBoardFull() == False

    board.cells = [
        [Cell('o'), Cell('o'), Cell('x')],
        [Cell('o'), Cell('x'), Cell('x')],
        [Cell('x'), Cell('o'), Cell('o')]
    ]

    assert board.isBoardFull() == True





