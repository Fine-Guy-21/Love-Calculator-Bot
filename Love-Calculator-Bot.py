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

@bot.on_message(filters.command("start"))
def Greetuser(bot,message):
    text = f"""💌 Dear {message.from_user.mention(f"{message.from_user.first_name}")}, 
Welcome to the Love Calculator Bot! Enter two names, and the bot will generate a love percentage between them. 💘 It's a fun way to gauge potential romantic connections.

✨ Let's find out the love percentage between you and your special someone! ✨

💑 Simply enter their names, and our magical algorithm will do the rest! 💫

🔥 Get ready for an exciting journey of love, laughter, and surprises! 🎉

💖 Discover your love compatibility and share the results with your friends! 🌟

🌹 Love is in the air! Start exploring now and uncover your love percentage! 🌈

😊 If you have any suggestions, feel free to reach out to me at @Fine_guy_21. 😊

Happy matching! 😄"""
    bot.send_message(message.chat.id,text )

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
            

    except:
        message.reply("Sorry, the name couldn't be found. Please refer to the /help command for instructions on how to use this command.")

@bot.on_message(filters.group & filters.command("love"))
def LoveCommand (bot,message):    
    if message.reply_to_message:
        try:
            name = message.reply_to_message.from_user.first_name
            myname = message.from_user.first_name
            result = SentenceGenerator(name,myname)
            result2 = SentenceGenerator(myname,name)
            mes = message.reply("🔄 Gathering Names from the input . . .")
            time.sleep(2)
            bot.edit_message_text(message.chat.id,mes.id, "Calculating Love 💌 . . .")
            time.sleep(5)
            bot.delete_messages(message.chat.id,mes.id)
            fir = int(re.findall(r'\b(\d+)%', result)[0]) 
            sec = int(re.findall(r'\b(\d+)%', result2)[0])
        except:
            message.reply("Apologies, the name couldn't be found. Please ensure that both you and the user have provided a first name.")   
    else:
        message.reply("reply to a user that you want")

@bot.on_message(filters.command("help"))
def HelpCommand(bot, message):

    text = f"""Dear {message.from_user.mention(f"{message.from_user.first_name}")}, Welcome to <b><u>Love Calculator Bot!</u></b> 🌟\nCalculate your love percentage with your loved ones using our bot 💑💖

Command: `/love` <i>(just reply to a user in a group)</i> 💌💬

Command: `/match First Second` 💞

The result will be displayed in the following format:
    The result is:
        First loves Second: 52%.
        Second loves First: 61%. 💕

We appreciate your support in using our bot and sharing it with others. Together, let's spread love and positivity in the world. If you have any suggestions or feedback, feel free to reach out to me(@Fine_Guy_21). Happy calculating and may love always be in your favor! ✨🌈💞
"""
    message.reply(text)
    
print("Love Calculator Bot is working ")
bot.run()