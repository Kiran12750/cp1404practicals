import string
from collections import Counter

def find_repeated_words(paragraph):
    # Step 1: Normalize the text (convert to lowercase and remove punctuation)
    paragraph = paragraph.lower()  # convert to lowercase
    paragraph = paragraph.translate(str.maketrans('', '', string.punctuation))  # remove punctuation

    # Step 2: Tokenize the text into words
    words = paragraph.split()  # split the text into individual words

    # Step 3: Filter words to include only those with exactly 4 characters
    words = [word for word in words if len(word) == 4]

    # Step 4: Count the occurrences of each word
    word_count = Counter(words)

    # Step 5: Find the words that are repeated exactly twice or three times
    repeated_words = {word: count for word, count in word_count.items() if count == 2 or count == 3}

    return repeated_words

# Example paragraph
paragraph = """vauxgjkzvvhtramgrmcxpvxjbqjwnbgfhychwumwdnjzvtbkamqvxfzmibqtgjcnacvfpn
owikogfdkurgkchqumvvqzkwkwkwjnvasjwnbgfhycmmcksugangkserrialweucqeaotp
txvhgpqomofopzzagviicvuqgukfzuyxqflnqfxfkfznqezfudvifcucgahhfvtvtwthzl
bbjxgvapzkmmfdvktrdkmngumsdsikqgrzrdwptzjcxctbhpyxzaihfqtavxazqnikwhfz
zcpvcebdbkhbrjgguxqlpzqhtbrbqmtloiwcixbbxsitkfwkcykqfdlrvbkhbrjmmuhiia
zaetbemolgysrropglmjrzuwgqflyqvbceygagviigoghhfrlzvekmgrdwplmjrzuklqrj
gmfisidzkvlstpzkaycinzzhxqkqzktxqpmwagkjrrdwphtkfzkkivvpomzmdimqqfxgem
dvhhfdyoqqgkyyoaqxjvpowcgoutzzutfpyimexgjymgehbugoqqgtfpvaafavrmqedspc
iktrdkgjvurgkchbqusllxwpwwkgjvcezpqzkwkszqopcmhycfmausrrgmclhrqgwpzojr
cmoxgjybmvasflzbkfsgyyqutbvvvuresfdvvwgqflyqvbceygtalstsmmggqiwkbkhbrj
bwtbhykkcdewtizgggqiwkbkhbjacmoxgymrmxxftyivqmpvsikqgrzrdwptzcwnmenfva
jurnhrrdwptzjcxctbhprcqufsrqpzglhycvuqnbkmakqfdlrvbkhbrjznhhfkpzywbfvb
wgvasscnbenficibnryemrvoxhymyavhrvdzivtgpqomotdimkwuxrrjbwtbhykdautwur
jjgvcdnpbcmwflvtnrgvapzgbtkfzxgkqvgqmfesmcgwhvcdnpbcmwflmmsnwicybqwswc
vbkmsoazmflhycxwoiikyoqqgocpzaqnftcnwhmvvftxqmvvqdagwoutzzutfpkjavhtkf
zjglhbljepvfpnowurgkchakgqlpmmpmijcvzgvcdnpbcmwflvtnrgvapzgmvvkzudxfjm
abjbgtjvautfvqjugmwdcninlctygtgwdiyxbkvocjtagviickzqoosjzagviigogcvfpn
owurgkchqulozbowdxdimqidemjcxctxwwrcmfbtwgxcnmmfdymhxokgiokmqrlwmuacnl
owdxsjqzvvbocjtiuwwwddkwehrqnwnoweevegezbljepwwwddkwehgpjjnxajsxpclwer
zogktraowtbgrrdwphfkfzkqfdlrvbkhbfdyquvfvrztqzoigopoldimqidesjcxctbhpg
nkqggzbzzgwhfzzifxelyomhhfdmnbrkotrdkceogngqethzmiaehagsoivbceygagviig
ogkgqcsymuifftvjnxgvapzkmmrqvxthdvpncdlsk"""

# Find words with exactly 4 characters that are repeated twice or three times
repeated_words = find_repeated_words(paragraph)

# Output the repeated words
print(repeated_words)
