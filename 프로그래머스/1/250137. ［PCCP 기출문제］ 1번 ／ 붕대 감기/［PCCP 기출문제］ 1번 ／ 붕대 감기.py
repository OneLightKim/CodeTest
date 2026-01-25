def solution(bandage, health, attacks):
    i = 1 #초
    current_health = health
    idx_attacks = 0
    while i <= attacks[-1][0]:
        count = 0
        for j in range(bandage[0]):
            if idx_attacks <= len(attacks)-1 and i == attacks[idx_attacks][0]:
                current_health -= attacks[idx_attacks][1]
                print('current_health: {}'.format(current_health))
                print('{}초, break'.format(i))
                idx_attacks += 1
                i += 1
                break
            else:
                count += 1
                current_health += bandage[1]
                print('current_health: {}'.format(current_health))
                print('{}초'.format(i))
                if count == bandage[0] and current_health < health:
                    current_health += bandage[2]
                if current_health > health:
                    current_health = health
                i += 1
        if current_health <= 0:
            return -1
    return current_health