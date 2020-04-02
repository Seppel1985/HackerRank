def is_vowel(char):
    return char.lower() in 'aeiou'
    
def minion_game(string):
    player1 = 0
    player2 = 0
    for length in range(1,len(string)+1):
        for i in range(len(string)-length+1):
            rel_text = string[i:i+length]
            if (is_vowel(rel_text[0])):
                player2 = player2 +1
            else:
                player1 = player1 +1
    if (player1 > player2):
        print ("Stuart " + str(player1))
    elif (player2 > player1):
        print ("Kevin " + str(player2))
    else:
        print ("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)