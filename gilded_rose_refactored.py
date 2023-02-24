class Item:
    def __init__(self, quality, days_remaining):
        self._quality = quality
        self._days_remaining = days_remaining

    @property
    def quality(self):
        return self._quality

    @property
    def days_remaining(self):
        return self._days_remaining

    def tick(self):
        return


class Normal(Item):
    def tick(self):
        self._days_remaining -= 1
        if self._quality == 0:
            return
        self._quality -= 1
        if self._days_remaining <= 0:
            self._quality -= 1


class AgedBrie(Item):
    def tick(self):
        self._days_remaining -= 1
        if self._quality >= 50:
            return
        self._quality += 1
        if self._days_remaining <= 0:
            self._quality += 1


class ConjuredManaCake(Item):
    def tick(self):
        self._days_remaining -= 1
        if self._quality == 0:
            return
        self._quality -= 2
        if self._days_remaining <= 0:
            self._quality -= 2


class BackstagePasses(Item):
    def tick(self):
        self._days_remaining -= 1
        if self._quality >= 50:
            return
        if self._days_remaining < 0:
            self._quality = 0
            return
        self._quality += 1
        if self._days_remaining < 10:
            self._quality += 1
        if self._days_remaining < 5:
            self._quality += 1
        return

DEFAULT_ITEM = Item
NAME_TO_ITEM = {
    "Normal": Normal,
    "Aged Brie": AgedBrie,
    "Backstage passes to a TAFKAL80ETC concert": BackstagePasses,
    "Conjured Mana Cake": ConjuredManaCake,
}


class GildedRose:
    @classmethod
    def for_item(cls, name, quality, days_remaining):
        return cls.class_for(name)(quality, days_remaining)

    @staticmethod
    def class_for(name):
        return NAME_TO_ITEM.get(name, DEFAULT_ITEM)
