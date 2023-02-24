import time

from gilded_rose import GildedRose


if __name__ == "__main__":
    item = GildedRose("Aged Brie", 20, 5)
    while True:
        item.tick()
        print(item.quality)
        time.sleep(1)
