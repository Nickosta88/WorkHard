import telebot

token = '794563519:AAGE1rAbWaSsY1pglqz7CNg52H0PDd-dvh4'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def Welcome(message):
    bot.reply_to(message, """
Hello, send me a message, and I will return it to you<3\
""")


@bot.message_handler(content_types=['sticker'])
def Repeat_Sticker(message):
    bot.send_sticker(message.chat.id , message.sticker.file_id)

@bot.message_handler(content_types=['text'])
def Repeat_Text(message):
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['photo'])
def Repeat_Photo(message):
    bot.send_photo(message.chat.id, message.photo[len(message.photo)-1].file_id)

@bot.message_handler(content_types=['video'])
def Repeat_Video(message):
    bot.send_video(message.chat.id, message.video.file_id)

@bot.message_handler(content_types=['audio'])
def Repeat_Audio(message):
    bot.send_audio(message.chat.id, message.audio.file_id)

@bot.message_handler(content_types=['document'])
def Repeat_Document(message):
    bot.send_document(message.chat.id, message.document.file_id)


if __name__ == '__main__':
    bot.polling(none_stop=True)
