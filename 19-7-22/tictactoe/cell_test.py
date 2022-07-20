from cell import Cell

cell = Cell('')

def test_empty():
    assert cell.isMarked() == False

def test_x():
    cell.setSymbol('x')
    assert cell.isMarked() == True

def test_o():
    cell.setSymbol('o')
    assert cell.isMarked() == True

def test_wrong():
    cell.setSymbol('anything')
    assert cell.isMarked() == False

