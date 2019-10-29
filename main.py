import random
from os import system

words = {
    # 'akutny': 'acute',
    'hanba': 'shame',
    # 'sok, sokovat': 'shock',
    '(vy)riesit': 'solve',
    # 'ulozit, uchovat': 'store',
    'trpiet': 'suffer',
    # 'operacia': 'surgery',
    # 'konat sa': 'take place',
    # 'clovek zraneny alebo zabity vo vojde, alebo pri nehode': 'casualty',
    # 'zahanbeny': 'ashamed',
    # 'sanitka': 'ambulance',
    # 'oznam': 'announcement',
    'zakazat (co)': 'ban',
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
    # 'zmysel pre humor': 'sense of humor',
    # 'strata pamati': 'amnesia',
    # 'poteseny, pobaveny': 'amused',
    # 'vyrocie': 'anniversary',
    # 'vychov(av)at': 'bring up',
    # 'oslava': 'celebration',
    # 'urobit zaver, zhrnut': 'conclude',
    # 'poskodit': 'damage',
    # 'pochybnost': 'doubt',
    # 'dramaticky, napinavy': 'dramatic',
    # 'v rozpakoch': 'embarrassed',
    # 'odovzdat, venovat': 'give away',
    # 'odist': 'go off',
    # 'urazit (koho)': 'insult',
    # 'ziarlivy': 'jealous',
    # 'posudzovat': 'judge',
    # 'zachranar': 'paramedic',
    # 'mak': 'poppy',
    # 'hrdy': 'proud',
    # 'uvedomit si': 'realise',
    # 'spomenut si, rozpametat': 'recall',
    # 'sviatok, v ktorom si v Britanii primominaju vojakov, ktori zahynuli vo vojde': 'remembrance day',
    # 'uviest situaciu': 'set the scene',
    # 'v bezvedomi': 'unconscious',
    # 'nespravodlivy': 'unfair',
    # 'znepokojeny': 'upset',


    # 'obavat sa (coho)': 'afraid',
    # 'zurit sa, zlyhat': 'break down',
    # 'pripominat si': 'commemorate',
    # 'nadseny/poteseny': 'delighted',
    # 'napriek (comu)': 'despite',
    # 'sklamany': 'disappointed',
    # 'zavist': 'envy',
    # 'dojaty': 'impressed',
    # 'trvat na (com)': 'insist on',
    # 'nahnevany, podrazdeny': 'irritated',
    # 'spokojny': 'pleased',
    # 'obliect si': 'put on',
    # 'spoznat': 'recognise',
    # 'uzdravenie': 'recovery',
    # 'zmiernit, ulahcit': 'relieve',
    # 'pripomenut si': 'remind',
    # 'zachranit': 'rescue',
    # 'spokojny': 'satisfied',
    # 'objavit sa': 'turn up',

}

initial_words = words.copy()
initial_word_amt = len(words)


def sort_dict_by_list_len(dct):
    sorted_list = sorted(
        dct.items(), key=lambda x: len(x[1]), reverse=True)
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
    problem_words_no_blanks = {key: val for key,
                               val in problem_words.items() if val != []}
    sorted_problem_words_no_blanks = sort_dict_by_list_len(
        problem_words_no_blanks).items()
    success_rate = 1 - len(problem_words_no_blanks.keys()) / initial_word_amt

    print('You\'re Awesome, You did it.')
    print(
        f'Success rate: {success_rate*100}% ({initial_word_amt - len(problem_words_no_blanks.keys())}/{initial_word_amt}, {len(problem_words_no_blanks.keys())} more word(s) to learn) ')
    print(f'You made {mistakes} total mistakes')

    if len(sorted_problem_words_no_blanks) > 0:
        print(f'Your problem words [{len(sorted_problem_words_no_blanks)}]:')
        for key, val in sorted_problem_words_no_blanks:
            print(f'    {key} -> {initial_words[key]} ({len(val)}: {val})')
    else:
        print('Yey, You have no problem words - You seem to know it all')
