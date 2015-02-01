__author__ = 'eric'

txt = """As a task """
counts = {}
for character in txt:
   if character in counts:
      counts[character] = counts[character] + 1
   else:
      counts[character] = 1

for character in ["e", "t", "o", "u"]:
   if character in counts:
       print ("The letter", character, "appears in the previous paragraph", counts[character], "times")
   else:
       print ("no ",character,"in text")
