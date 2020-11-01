numletdict = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10,
    'k' : 11,
    'l' : 12,
    'm' : 13,
    'n' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26
}
wordfile = r'C:\Users\charl\Downloads\words.txt'
words = open(wordfile, "r")
words = words.read()

def trinumgen(n):
    # generates the first n triangular numbers
    array = []
    num = 0
    for i in range(1,n+1):
        num += i
        array.append(num)
    return array

trinums = trinumgen(40)

def triwordcheck(word):
    total = 0
    word = word.lower()
    for char in word:
        total += numletdict[char]
    if total in trinums:
        return True
    else:
        return False

wordarray = []
while not(words == ''):
    start = words.find('"')
    end = words.find('"',2)
    wordarray.append(words[start+1:end])
    words = words[end+2:]

ans = 0
for word in wordarray:
    if triwordcheck(word):
        ans += 1
print(ans)