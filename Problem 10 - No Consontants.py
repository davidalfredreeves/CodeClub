# Problem 10 - No Consonants

Consonants = ["b", "B", "c", "C", "d", "D", "f", "F", "g", "G", "h", "H",
              "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "p", "P",
              "q", "Q", "r", "R", "s", "S", "t", "T", "v", "V", "w", "W",
              "x", "X", "y", "Y", "z", "Z"]

sentence = "The quick brown fox jumped over the lazy dog into a pit of fiery death..."

for c in Consonants:
    sentence = sentence.replace(c, "")

print (sentence)
