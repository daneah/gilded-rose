import pytest

from gilded_rose import GildedRose


class TestNormalItem:
    def test_before_sell_date(self):
        item = GildedRose("normal", 10, 5)
        item.tick()
        assert item.quality == 9
        assert item.days_remaining == 4

    def test_on_sell_date(self):
        item = GildedRose("normal", 10, 0)
        item.tick()
        assert item.quality == 8
        assert item.days_remaining == -1

    def test_after_sell_date(self):
        item = GildedRose("normal", 10, -10)
        item.tick()
        assert item.quality == 8
        assert item.days_remaining == -11

    def test_zero_quality(self):
        item = GildedRose("normal", 0, 5)
        item.tick()
        assert item.quality == 0
        assert item.days_remaining == 4


class TestBrie:
    def test_before_sell_date(self):
        item = GildedRose("Aged Brie", 10, 5)
        item.tick()
        assert item.quality == 11
        assert item.days_remaining == 4

    def test_with_max_quality(self):
        item = GildedRose("Aged Brie", 10, 5)
        item.tick()
        assert item.quality == 11
        assert item.days_remaining == 4

    def test_on_sell_date(self):
        item = GildedRose("Aged Brie", 10, 0)
        item.tick()
        assert item.quality == 12
        assert item.days_remaining == -1

    def test_on_sell_date_with_max_quality(self):
        item = GildedRose("Aged Brie", 50, 0)
        item.tick()
        assert item.quality == 50
        assert item.days_remaining == -1

    def test_after_sell_date(self):
        item = GildedRose("Aged Brie", 10, -10)
        item.tick()
        assert item.quality == 12
        assert item.days_remaining == -11

    def test_after_sell_date_with_max_quality(self):
        item = GildedRose("Aged Brie", 50, -10)
        item.tick()
        assert item.quality == 50
        assert item.days_remaining == -11


class TestSulfuras:
    def test_before_sell_date(self):
        item = GildedRose("Sulfuras, Hand of Ragnaros", 80, 5)
        item.tick()
        assert item.quality == 80
        assert item.days_remaining == 5

    def test_on_sell_date(self):
        item = GildedRose("Sulfuras, Hand of Ragnaros", 80, 0)
        item.tick()
        assert item.quality == 80
        assert item.days_remaining == 0

    def test_after_sell_date(self):
        item = GildedRose("Sulfuras, Hand of Ragnaros", 80, -10)
        item.tick()
        assert item.quality == 80
        assert item.days_remaining == -10


class TestBackstagePasses:
    def test_long_before_sell_date(self):
        item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 11)
        item.tick()
        assert item.quality == 11
        assert item.days_remaining == 10

    def test_long_before_sell_date_with_max_quality(self):
        item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 50, 11)
        item.tick()
        assert item.quality == 50
        assert item.days_remaining == 10

    def test_near_sell_date_upper_bound(self):
        item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 10)
        item.tick()
        assert item.quality == 12
        assert item.days_remaining == 9

    def test_near_sell_date_with_max_quality_upper_bound(self):
        item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 50, 10)
        item.tick()
        assert item.quality == 50
        assert item.days_remaining == 9

    def test_near_sell_date_lower_bound(self):
        item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 6)
        item.tick()
        assert item.quality == 12
        assert item.days_remaining == 5

    def test_near_sell_date_with_max_quality_lower_bound(self):
        item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 50, 6)
        item.tick()
        assert item.quality == 50
        assert item.days_remaining == 5

    def test_close_sell_date_upper_bound(self):
        item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 5)
        item.tick()
        assert item.quality == 13
        assert item.days_remaining == 4

    def test_close_sell_date_with_max_quality_upper_bound(self):
        item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 50, 5)
        item.tick()
        assert item.quality == 50
        assert item.days_remaining == 4

    def test_close_sell_date_lower_bound(self):
        item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 1)
        item.tick()
        assert item.quality == 13
        assert item.days_remaining == 0

    def test_close_sell_date_with_max_quality_lower_bound(self):
        item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 50, 1)
        item.tick()
        assert item.quality == 50
        assert item.days_remaining == 0

    def test_on_sell_date(self):
        item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, 0)
        item.tick()
        assert item.quality == 0
        assert item.days_remaining == -1

    def test_after_sell_date(self):
        item = GildedRose("Backstage passes to a TAFKAL80ETC concert", 10, -10)
        item.tick()
        assert item.quality == 0
        assert item.days_remaining == -11


@pytest.mark.skip
class TestConjuredManaCake:
    def test_before_sell_date(self):
        item = GildedRose("Conjured Mana Cake", 10, 5)
        item.tick()
        assert item.quality == 8
        assert item.days_remaining == 4

    def test_before_sell_date_with_zero_quality(self):
        item = GildedRose("Conjured Mana Cake", 0, 5)
        item.tick()
        assert item.quality == 0
        assert item.days_remaining == 4

    def test_on_sell_date(self):
        item = GildedRose("Conjured Mana Cake", 10, 0)
        item.tick()
        assert item.quality == 6
        assert item.days_remaining == -1

    def test_on_sell_date_with_zero_quality(self):
        item = GildedRose("Conjured Mana Cake", 0, 0)
        item.tick()
        assert item.quality == 0
        assert item.days_remaining == -1

    def test_after_sell_date(self):
        item = GildedRose("Conjured Mana Cake", 10, -10)
        item.tick()
        assert item.quality == 6
        assert item.days_remaining == -11

    def test_after_sell_date_at_zero_quality(self):
        item = GildedRose("Conjured Mana Cake", 0, -10)
        item.tick()
        assert item.quality == 0
        assert item.days_remaining == -11
