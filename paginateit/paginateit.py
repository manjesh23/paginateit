"""Main module."""

# Paginateit

def page(count, max_workers=2):
    ndiv = int(count/max_workers)
    sk = 0
    lm = ndiv
    for mw in range(1, (max_workers+2)):
            globals()[f"skip{mw}"] = sk
            globals()[f"limit{mw}"] = lm
            globals()[f"flimit{mw}"] = str(lm)[1:].lstrip("0")
            globals()[f"count{mw}"] = lm - sk
            sk = sk + ndiv
            lm = lm + ndiv
