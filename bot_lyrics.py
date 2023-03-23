import telebot
from telebot import types

from time import sleep
from lyricsgenius import Genius
import textwrap


token = '5979685133:AAE1ciAqk800SNOsjtd91udbVdzFeQjWtz4'
g = Genius("HcAgpKN4LvM3-BkegBAT2qYW_nPiiQ2PEAv5Nt4KU4l2CrwET91NrfiyhUbIkg2z")\


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi! It is a Genius.com! \n To find your lyurics of your favourite music type "/search" ')

@bot.message_handler(commands=['search'])
# def search(message):
#     def search_lyrics(message):
#         msg1 = bot.send_message(message.chat.id, 'Name of song: ')
#         bot.register_next_step_handler(msg1, answer)
        
#     msg = bot.send_message(message.chat.id, 'Name of artist: ')
#     bot.register_next_step_handler(msg, search_lyrics)



def search(message):
    def search_lyrics(message):
        # Save the user's response to the "Name of artist" prompt
        artist_name = message.text

        def process_song(message, artist_name):
            def get_lyrics(artist_name, song_name):
                song = g.search_song(song_name, artist_name)
                if song is not None:
                    return song.lyrics
                else:
                    return None
            song_name = message.text
            lyrics = get_lyrics(artist_name, song_name)
            if lyrics:
                answer(message, artist_name, lyrics)
            else:
                bot.send_message(message.chat.id, f"Sorry, I could not find lyrics for {song_name} by {artist_name}.")

        msg1 = bot.send_message(message.chat.id, 'Name of song: ')
        bot.register_next_step_handler(msg1, lambda message: process_song(message, artist_name))




    msg = bot.send_message(message.chat.id, 'Name of artist: ')
    bot.register_next_step_handler(msg, search_lyrics)

def answer(message, artist_name, lyrics):
    MAX_MESSAGE_LENGTH = 4000
    if len(lyrics) > MAX_MESSAGE_LENGTH:
        # Split lyrics into smaller chunks
        chunks = [lyrics[i:i+MAX_MESSAGE_LENGTH] for i in range(0, len(lyrics), MAX_MESSAGE_LENGTH)]
        for i, chunk in enumerate(chunks):
            bot.send_message(message.chat.id, f"Here are the lyrics for {message.text} by {artist_name} (part {i+1}/{len(chunks)}):\n\n{chunk}")
    else:
        bot.send_message(message.chat.id, f"Here are the lyrics for {message.text} by {artist_name}:\n\n{lyrics}")


        

    

    # artist = g.search_artist(artist_name, max_songs=1)
    # if artist is None:
    #     bot.send_message(message.chat.id, 'Artist not found.')
    #     return
    # song = g.search_song(message.text, artist.name)
    # if song is None:
    #     bot.send_message(message.chat.id, 'Song not found.')
    #     return
    
    # max_length = 4096
    # while len(song.lyrics) > 0:
    #     chunk = song.lyrics[:max_length]
    #     song.lyrics = song.lyrics[max_length:]
    #     bot.send_message(message.chat.id, chunk)
    


@bot.message_handler(content_type=['text'])
def text(message):
    bot.send_message(message.chat.id, 'You want something? ')






    


bot.infinity_polling()