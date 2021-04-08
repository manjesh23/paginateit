import pytest


def page(count, max_workers=2):
    ndiv = int(count/max_workers)
    sk = 0
    lm = ndiv
    # Loop based on count and calcuates the end values required for pagination
    for mw in range(1, (max_workers+2)):
        globals()[f"skip{mw}"] = sk
        globals()[f"limit{mw}"] = lm
        globals()[f"flimit{mw}"] = str(lm)[1:].lstrip("0")
        globals()[f"count{mw}"] = lm - sk
        sk = sk + ndiv
        lm = lm + ndiv


def test_page():
    page(23052, 4)
    assert page.limit5 == 28815
    assert page.skip1 == 0
    assert page.count4 == 5763
    assert page.flimit3 == '7289'
