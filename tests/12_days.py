import pytest


class Song:
    def __init__(self):

        self.days = [
            "first",
            "second",
            "third",
            "forth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
            "ninth",
            "tenth",
            "eleventh",
            "twelfth",
        ]
        self.gifts = [
            "And a partridge in a pear tree. ",
            "Two turtle doves, ",
            "Three French hens, ",
            "Four calling birds, ",
            "Five golden rings, ",
            "Six geese a-laying, ",
            "Seven swans a-swimming, ",
            "Eight maids a-milking, ",
            "Nine ladies dancing, ",
            "Ten lords a-leaping, ",
            "Eleven pipers piping, ",
            "Twelve drummers drumming, ",
        ]
        self.result = ""

    def start_of_verse(self, verse_num):

        self.result += (
            f"On the {self.days[verse_num-1]} day of Christmas \n"
            "My true love sent to me: \n"
        )

    def body_of_verse(self, verse_num):
        if verse_num == 1:
            self.result += "A partridge in a pear tree. \n"
        else:
            while verse_num > 0:
                self.result += f"{self.gifts[verse_num -1]}\n"
                verse_num -= 1
        return self.result

    def sing_song(self, verse_num):
        i = 1
        while i <= verse_num:
            self.start_of_verse(i)
            self.body_of_verse(i)
            self.result += "\n"
            i += 1
        return self.result


# song = Song()
# print(song.sing_song(12))


@pytest.fixture
def song_class():
    song = Song()
    yield song


def test_first_2_lines_of_verse_1(song_class):
    song_class.start_of_verse(1)
    assert (
        song_class.result == "On the first day of Christmas \n"
        "My true love sent to me: \n"
    )


def test_first_2_lines_of_verse_2(song_class):
    song_class.start_of_verse(2)
    assert (
        song_class.result == "On the second day of Christmas \n"
        "My true love sent to me: \n"
    )


def test_first_2_lines_of_any_verse(song_class):
    song_class.start_of_verse(4)
    assert (
        song_class.result == "On the forth day of Christmas \n"
        "My true love sent to me: \n"
    )


def test_first_gift_with_verse_1(song_class):
    song_class.body_of_verse(1)
    assert song_class.result == "A partridge in a pear tree. \n"


def test_correct_gift_with_verse_2(song_class):
    song_class.body_of_verse(2)
    assert (
        song_class.result == "Two turtle doves, \n" "And a partridge in a pear tree. \n"
    )


def test_correct_gift_with_any_verse(song_class):
    song_class.body_of_verse(6)
    assert (
        song_class.result == "Six geese a-laying, \n"
        "Five golden rings, \n"
        "Four calling birds, \n"
        "Three French hens, \n"
        "Two turtle doves, \n"
        "And a partridge in a pear tree. \n"
    )


def test_sing_verse_returns_the_complete_verse_1(song_class):
    verse = 1
    song_class.start_of_verse(verse)
    song_class.body_of_verse(verse)
    assert (
        song_class.result == "On the first day of Christmas \n"
        "My true love sent to me: \n"
        "A partridge in a pear tree. \n"
    )


def test_sing_verse_returns_the_complete_verse_2(song_class):
    verse = 2
    song_class.start_of_verse(verse)
    song_class.body_of_verse(verse)
    assert (
        song_class.result == "On the second day of Christmas \n"
        "My true love sent to me: \n"
        "Two turtle doves, \n"
        "And a partridge in a pear tree. \n"
    )


def test_sing_verse_returns_the_complete_verse_of_any_verse(song_class):
    verse = 12
    song_class.start_of_verse(verse)
    song_class.body_of_verse(verse)
    assert (
        song_class.result == "On the twelfth day of Christmas \n"
        "My true love sent to me: \n"
        "Twelve drummers drumming, \n"
        "Eleven pipers piping, \n"
        "Ten lords a-leaping, \n"
        "Nine ladies dancing, \n"
        "Eight maids a-milking, \n"
        "Seven swans a-swimming, \n"
        "Six geese a-laying, \n"
        "Five golden rings, \n"
        "Four calling birds, \n"
        "Three French hens, \n"
        "Two turtle doves, \n"
        "And a partridge in a pear tree. \n"
    )


def test_sing_multiple_verses_in_the_correct_order(song_class):
    assert (
        song_class.sing_song(2) == "On the first day of Christmas \n"
        "My true love sent to me: \n"
        "A partridge in a pear tree. \n"
        "\n"
        "On the second day of Christmas \n"
        "My true love sent to me: \n"
        "Two turtle doves, \n"
        "And a partridge in a pear tree. \n"
        "\n"
    )
