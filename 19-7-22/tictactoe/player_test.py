from board import Board
from player import Player
from cell import Cell

board = Board.createBoard()
player = Player('player1', 'x')

def test_placeMove():
    board.cells = [
        [Cell('o'), Cell('o'), Cell('x')],
        [Cell('o'), Cell('x'), Cell('x')],
        [Cell('x'), Cell('o'), Cell('o')]
    ]

    assert player.placeMove(board.cells[0][0]) == (False, "Position occupied.")

    board.cells = [
        [Cell('_'), Cell('o'), Cell('x')],
        [Cell('o'), Cell('x'), Cell('x')],
        [Cell('x'), Cell('o'), Cell('o')]
    ]

    assert player.placeMove(board.cells[0][0]) == (True, "Cell marked.")