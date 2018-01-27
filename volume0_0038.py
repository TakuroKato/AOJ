# -*- coding:utf-8 -*-
def hand(card):
    m = 0
    n = [0]*13
    val = 0
    for i in range(13):
        n[i] = card.count(str(i+1))
    for i in range(13):
        if n[i] == 4:
            return 'four card'
    for i in range(13):
        if n[i] == 3:
            for j in range(13):
                if n[j] == 2:
                    return 'full house'
            return 'three card'

    for i in range(13):
        if n[i] == 2:
            for j in range(i+1,13):
                if n[j] == 2:
                    return 'two pair'
            return 'one pair'
    for i in range(len(card)):
        card[i] = int(card[i])
    card.sort()
    
    if card == [1,10,11,12,13]:
        return 'straight'
    for i in range(4):
        if card[4-i] - card[4-i-1] != 1:
            return 'null'
    return 'straight'

while True:
    try:
        card = input().split(',')
        print(hand(card))
            
    except:
        break
