import requests

# get the word from api with letter of 6 or less
def get_word():
    url = "https://random-word-api.herokuapp.com/word"
    try:
        response = requests.get(url, timeout=5)
    except:
        print("Connection to API failed")
        return "errorxxz"
    
    if response.status_code == 200:
        word = response.json()[0]
        return word
    else:
        print(f"Request failed with status code {response.status_code}")
        return "errorxxz"

def get_definiton():
    final_d = []
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+word
    try:
        response = requests.get(url, timeout=5)
    except:
        return "404"
    
    if response.status_code == 200:
        definition = response.json()[0]["meanings"][0]["definitions"]
        # print(definition)
        for d in definition:
            # print(d["definition"])
            final_d.append(d["definition"])
        return final_d
    else:
        return "404"



print('''
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
*           Welcome to Helenawordl
*      This program will find a word
*       and its definition as a hint
*
*    ->  E_xaMPLE_
*        This signifies :
*    - Uppercase means right letter
*    - Lowercase means right letter but wrong placement
*    - blank means, you know, blank.
* 
*                 Have fun!
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
''')


word = "abcdefg"
definiton = "404"
while definiton == "404":
    print("*\n* Finding word")
    while len(word) > 6:        
        word = get_word().lower()
        print("*")
    print("* Finding definiton\n* ")
    definiton = get_definiton()
    if definiton == "404":
        word = "abcdefg"


print(f"* It is a {len(word)} letter word, ", end="")
print("hints : ")
for d in definiton:
    print(f"* > {d}")
print("")

#game starts
game_count = 4
tries = game_count
while game_count != 0:
    guess = ""
    print("* * * * * * * * * * * * * * * * * ")
    print(f"*\n* You have {game_count} out of {tries} tries\n*")
    user_input = input("* Input your word guess : ").lower()

    i = 0
    for w in word:
        try:
            if w == user_input[i]:
                guess += user_input[i].upper()
            else:
                if user_input[i] in word:
                    guess += user_input[i]
                else:
                    guess += "_"
        except:
            guess += "_"
        i +=1

    print("*\n* * * * * * * * * * * * * * * * * ")
    print(f"*\n* Your guess : {guess} \n*")
    game_count -=1
    if guess.lower() == word:
        print("* You won! \n*")
        break
    if game_count == 2:
        print("*\n!==================================!")
        print("         BIG HINTS : ", end="")
        ixz = 0
        for w in word:
            if ixz == 2:
                print("_", end="")
            elif ixz == 5:
                print("_", end="")
            else:
                print(w.upper(), end="")
            ixz+=1
        print("")
    elif game_count == 0:
        print(f"* The answer : {word.upper()}")
        print(f"* \n* You lost! \n*")
