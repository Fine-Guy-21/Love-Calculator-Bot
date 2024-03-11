import re
import time
from pyrogram import Client , filters


bot = Client("Love Calculator Bot",api_id=21832338, 
              api_hash="3d11dad763458ea9b7ab106d6fc5e7ce",
              bot_token="7067695785:AAERBgE31NNB-si_CLRQ3cemfWlGSwIxPvQ")





# Functions 


def calculator(word):
    result = ""
    if len(word) > 2 :
        if len(word) % 2 == 0:
            max = int(len(word)/2) 
            for i in range(0,max):
                res = int(word[i]) + int(word[len(word)-1-i])
                result = result + str(res)
            return calculator(result)      
            
        else:
            max = int(len(word)/2)
            for i in range(0,max):
                res = int(word[i]) + int(word[len(word)-1-i])
                result = result + str(res) 
                if i == max-1:
                    result = result + str(word[max])
            return calculator(result)
            
    else:
        return (word)

def appearance(sentence):  
    Numbers = ""
    checked_letters = []
    for x in sentence:
        counter = 0
        if x == " ":          
            continue
        elif x not in checked_letters:
            for y in sentence:                      
                if y == " ":
                    continue
                elif y == x :
                    counter += 1
                else:
                    continue
            Numbers = Numbers + str(counter)
            checked_letters.append(x)
        else:
            continue
    return Numbers  

def SentenceGenerator(male , female):
    male= male.lower()
    female= female.lower()
    Sentence = f"{male} loves {female}" 
    sentence2 = f"{male.capitalize()}  <b>Loves</b>  {female.capitalize()}"
    result = calculator(appearance(Sentence))
    mes = ( f"{sentence2} : `{result}% ` .")
    
    return mes



@bot.on_message(filters.command("match"))
def MatchCommand (bot, message):
    text = message.text 
    try:
        male = text.split(" ")[1]
        female = text.split(" ")[2]
        result = SentenceGenerator(male,female)
        result2 = SentenceGenerator(female,male)
        mes = message.reply("🔄 Gathering Names from the input . . .")
        time.sleep(2)
        bot.edit_message_text(message.chat.id,mes.id, "Calculating Love 💌 . . .")
        time.sleep(5)
        bot.delete_messages(message.chat.id,mes.id)
        fir = int(re.findall(r'\b(\d+)%', result)[0]) 
        sec = int(re.findall(r'\b(\d+)%', result2)[0])
        if fir > sec:
            message.reply(f"The result is : \n\t {result}💕 \n\t {result2}")
        elif sec > fir:
            message.reply(f"The result is : \n\t {result} \n\t {result2}💕")
        else:
            message.reply(f"The result is : \n\t {result}💕 \n\t {result2}💕")

    except:
        message.reply("Sorry, the name couldn't be found. Please refer to the /help command for instructions on how to use this command.")

@bot.on_message(filters.group & filters.command("love"))
def LoveCommand (bot,message):
    print("love")


@bot.on_message(filters.command("help"))
def MatchCommand (bot, message):
    text = f"""Dear {message.from_user.first_name}, Welcome to <b><u>Love Calculator Bot!</u></b> 🌟  \nCalculate your love percentage with your loved ones using our bot 💑💖
\n\nCommand: `/love` <i> just reply to a user in a group </i> 💌💬
\nCommand: `/match First Second` 💞
\n
The result will be displayed in the following format:
`\tThe result is:
\t\tFirst loves Second: 52%.
\t\tSecond loves First: 61%.`



"""
    message.reply(text)

    


print("Love Calculator Bot is working ")
bot.run()