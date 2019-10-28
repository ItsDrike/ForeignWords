import random
import operator
from os import system

words = {
    # 'akutny': 'acute',
    # 'hanba': 'shame',
    # 'sok, sokovat': 'shock',
    # '(vy)riesit': 'solve',
    # 'ulozit, uchovat': 'store',
    # 'trpiet': 'suffer',
    # 'operacia': 'surgery',
    # 'konat sa': 'take place',
    # 'clovek zraneny alebo zabity vo vojde, alebo pri nehode': 'casualty',
    # 'zahanbeny': 'ashamed',
    # 'sanitka': 'ambulance',
    # 'oznam': 'announcement',
    # 'zakazat (co)': 'ban',
    # 'kamarat': 'comrade',
    # 'konflikt': 'conflict',
    # 'skluceny': 'depressed',
    # 'vzdialeny': 'distant',
    # 'tuziaci po domove': 'homesick',
    # 'incident': 'incident',
    # 'nervozny': 'nervous',
    # 'chodec': 'pedestrian',
    # 'fyzicky': 'physical',
    # 'zdvihnut, zobrat': 'pick up',
    # 'vztah': 'relationship',
    # 'nastastie': 'fortunately',
    # 'boj': 'battle',
    # 'stav nudze': 'emergency',


    'obavat sa (coho)': 'afraid',
    'strata pamati': 'amnesia',
    'poteseny, pobaveny': 'amused',
    'vyrocie': 'anniversary',
    'zurit sa, zlyhat': 'break down',
    'vychov(av)at': 'bring up',
    'oslava': 'celebration',
    'pripominat si': 'commemorate',
    'urobit zaver, zhrnut': 'conclude',
    'poskodit': 'damage',
    'nadseny/poteseny': 'delighted',
    'napriek (comu)': 'despite',
    'sklamany': 'disappointed',
    'pochybnost': 'doubt',
    'dramaticky, napinavy': 'dramatic',
    'v rozpakoch': 'embarrassed',
    'zavist': 'envy',
    'odovzdat, venovat': 'give away',
    'odist': 'go off',
    'dojaty': 'impressed',
    'trvat na (com)': 'insist on',
    'urazit (koho)': 'insult',
    'nahnevany, podrazdeny': 'irritated',
    'ziarlivy': 'jealous',
    'posudzovat': 'judge',
    'zachranar': 'paramedic',
    'spokojny': 'pleased',
    'mak': 'poppy',
    'hrdy': 'proud',
    'obliect si': 'put on',
    'uvedomit si': 'realise',
    'spomenut si, rozpametat': 'recall',
    'spoznat': 'recognise',
    'uzdravenie': 'recovery',
    'zmiernit, ulahcit': 'relieve',
    'sviatok, v ktorom si v Britanii primominaju vojakov, ktori zahynuli vo vojde': 'remembrance day',
    'pripomenut si': 'remind',
    'zachranit': 'rescue',
    'spokojny': 'satisfied',
    'zmysel pre humor': 'sense of humor',
    'uviest situaciu': 'set the scene',
    'objavit sa': 'turn up',
    'v bezvedomi': 'unconscious',
    'nespravodlivy': 'unfair',
    'znepokojeny': 'upset',
}


def sort_by_values_len(dct):
    def rotate_list(l, n):
        return l[n:] + l[:n]

    temp_dct = {key: len(dct[key]) for key in dct}
    inverted_sorted_dct = sorted(
        temp_dct.items(), key=operator.itemgetter(1))
    sorted_list = [i for i in reversed(inverted_sorted_dct)]
    sorted_dict = {element[0]: dct[element[0]] for element in sorted_list}
    return sorted_dict


problem_words = {key: [] for key in words}

mistakes = 0

system('cls')
while len(words) > 0:
    keys = words.keys()
    word = random.choice(list(words.keys()))
    ln = 0
    raw_word = word.replace(' *', '').replace('*', '')
    for wrd in words:
        if raw_word in wrd:
            ln += 1
    inp = input(f'[{len(words)}]({ln}) -> {word}: ').lower()
    if words[word] == inp:
        words.pop(word)
        ln -= 1
        if ln == 0:
            input(f'Correct (No more same words)')
        else:
            input(f'Correct, {ln} same words more.')
        system('cls')
    elif inp == '*':
        inp = input('Skipping...')
        system('cls')
    else:
        mistakes += 1
        problem_words[raw_word].append(inp)
        stars = ln * '*'
        words[f'{raw_word} {stars}'] = words[word]
        input(
            f'Incorrect -> {words[word]} ({ln} mistakes logged)')
        system('cls')
else:
    print('You\'re Awesome, You did it.')
    print(f'You made {mistakes} mistakes')
    problem_words1 = {key: val for key,
                      val in problem_words.items() if val != []}
    print(f'Your problem words:')
    for key, val in sort_by_values_len(problem_words1).items():
        print(f'{key} -> {val}')
