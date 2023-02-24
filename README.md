# Gilded Rose kata

This is a version of the Gilded Rose kata in Python that uses pytest for testing.

## Install dependencies

```shell
$ python -m pip install -r requirements.txt
```

## Run tests

```shell
$ python -m pytest
```

## Complexity

```shell
$ radon cc -s gilded_rose.py
gilded_rose.py
    M 7:4 GildedRose.tick - C (18)
    C 1:0 GildedRose - C (11)
    M 2:4 GildedRose.__init__ - A (1)

$ radon cc -s gilded_rose_refactored.py
gilded_rose_refactored.py
    C 48:0 BackstagePasses - B (6)
    M 49:4 BackstagePasses.tick - A (5)
    C 18:0 Normal - A (4)
    C 28:0 AgedBrie - A (4)
    C 38:0 ConjuredManaCake - A (4)
    M 19:4 Normal.tick - A (3)
    M 29:4 AgedBrie.tick - A (3)
    M 39:4 ConjuredManaCake.tick - A (3)
    C 1:0 Item - A (2)
    C 72:0 GildedRose - A (2)
    M 2:4 Item.__init__ - A (1)
    M 7:4 Item.quality - A (1)
    M 11:4 Item.days_remaining - A (1)
    M 14:4 Item.tick - A (1)
    M 74:4 GildedRose.for_item - A (1)
    M 78:4 GildedRose.class_for - A (1)
```
