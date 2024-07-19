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

