import aminofix 
import random

list = ["щуку", "змееголова", "карпа", "осëтра", "сома", "сазана", "окуня речного", "леща", "карася", "пескаря", "лина", "красноперку", "налима", "ёрша", "толстолобика", " кафельника", "маринку", "османа", "храмулю", "усача"]

items = ["комок грязи", "комок бумаги", "сундучок", "палку", "камень"]

drop = ["браслет", "кулон", "мусор", "монеты", "кунай", "маленький свиток", "свиток с техникой", "труп рыбки", "бутылочка с жидкостью", "маленький артефакт" ]

client = aminofix.Client()
client.login(email= "fish.ryba01@gmail.com", password= "Rbanray02")

sub_client = aminofix.SubClient(comId="67770833", profile=client.profile)


def catch():
    rand_num = random.randint(0,100)
    if rand_num <=70:
        return True 
    else:
        return False 
    
def fishings():
    if catch():
        rand_num = random.randint(1,100)
        if rand_num <=30:
            random_items = random.choice(items)
            return random_items
        else:
            random_fish = random.choice(list)
            return random_fish
    else:
        return None

def message_processing(data):
    content = data.message.content
    chatId = data.message.chatId
    print(content)
    if content.lower() == "начать рыбалку":
        booty = fishings()
        item = random.choice(drop)
        
        if booty == "сундучок":
            print(booty)
            sub_client.send_message(message=f"Поздравляю, вы выловили {booty}, в котором был {item}!", chatId=chatId)
            
        elif booty == None:
            sub_client.send_message(message="Поздравляю, речка сожрала вашу удочку!", chatId=chatId)
        else:
            sub_client.send_message(message = f"Вы поймали {booty}.", chatId=chatId)  
 
    elif content.lower() == "_помощь":
                      sub_client.send_message(message = "Я бот для рп рыбалки!\nЧто бы начать рыбачить, напиши в чат \"начать рыбалку\".\nЯ пока что не имею хранилища, поэтому запоминай что тебе попадается :]", chatId=chatId)   
		                    
for x in client.chat_methods:
    client.event(client.chat_methods[x].__name__)(message_processing)