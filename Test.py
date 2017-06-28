import sys, eveapi

YOUR_KEYID = 1111
YOUR_VCODE = '222222222222222222222222'


def choosen(characters):
    if not characters:
        print('You api is broken, characters not found.')
    else:
        start = 0
        for chars in characters:
            start+=1
            print(start, chars.name)

        takehime = input('Кого использовать (номер)?\n')
        if takehime.isdigit():
            char = int(takehime)
            if char in [1,2,3]:
                if char <= len(characters):
                    return char-1

        print("Oшибка выбора, вы выбрали '",takehime,"'")
        choosen(characters)


def main(args):
    eveapi.set_user_agent("eveapi.py/1.3")
    api = eveapi.EVEAPIConnection()
    auth = api.auth(keyID=YOUR_KEYID, vCode=YOUR_VCODE)
    result = auth.account.Characters()

    charnum = choosen(result.characters)

    ret = auth.character(result.characters[charnum].characterID)	
    sheet = ret.CharacterSheet()

    print(sheet.name)
    #skilltree = api.eve.SkillTree()
    #print()

    #for g in skilltree.skillGroups:


if __name__ == '__main__':
    main(sys.argv)
