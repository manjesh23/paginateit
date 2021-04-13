import pytest
from paginateit import paginateit as pg


def test_page():
    pg.page(23052, 4)
    assert pg.limit5 == 28815
    assert pg.skip1 == 0
    assert pg.count4 == 5763
    assert pg.flimit3 == '7289'
