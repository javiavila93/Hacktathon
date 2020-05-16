from telegram.ext import Updater, CommandHandler

def main():
    # arreglar open token
    updater = Updater(token = '1223807853:AAEiP4ROcd0FzNY1QcdvYIElCdKA9aZ8jTg', use_context=True)
    
    # Añadimos un manejador de compando
    updater.dispatcher.add_handler(CommandHandler('start', start))

    # Añadimos un manejador de compando
    updater.dispatcher.add_handler(CommandHandler('reply', reply))

     # Añadimos un manejador de compando
    updater.dispatcher.add_handler(CommandHandler('suma', suma))

    # Pedir notificaciones a telegram
    updater.start_polling()

    # Capturamos señadoles
    updater.idle()

   

def start(update, context):
    update.message.reply_text("hola, soy un bot")


def reply(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    resultado = int(context.args[0]) + int(context.args[1])
    resultador = str(resultado)
    print(resultador)
    update.message.reply_text('El resultado es ' + resultador)


main()