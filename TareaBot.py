
#Nota: Para ver el chatbot en Telegram se puede encontrar con el nombre de "Mi_bot_Patrick_Castro"
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def help(update, context):
    update.message.reply_text('Puede usar los comandos: ')
    update.message.reply_text('/start')
    update.message.reply_text('Para iniciar el bot')

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def start(update, context):
    update.message.reply_text('Hola, este es un bot inmobiliario. ')
    update.message.reply_text('Puede usar el comando "/venta" para ir a la sección de ventas')
    update.message.reply_text('Puede usar el comando "/alquiler" para ir a la sección de alquiler')


def alquiler(update, context):
    if(update.message.text.upper().find("ALQUILER") > 0):
        update.message.reply_text("No hay Stock")


def venta(update, context):
    update.message.reply_text('Puede usar el comando "/tipo" para ver los tipos de inmuebles disponibles')      

def  tipo(update, context):
        update.message.reply_text("Le ofrecemos los siguientes inmuebles: ")
        update.message.reply_text("/Apartamento")
        update.message.reply_text("/Local")
        update.message.reply_text("/Bodega")
        update.message.reply_text("/Casa")

def apartamento(update, context):
        update.message.reply_text("¿En qué lugar de Guatemala desea su apartamento?")
        update.message.reply_text("/Capital")
        update.message.reply_text("/Quetzaltenango")
        update.message.reply_text("/Totonicapan")
        update.message.reply_text("/Progreso")
        update.message.reply_text("/Sacatepequez")  

def local(update, context):
        update.message.reply_text("¿En qué lugar de Guatemala desea su local?")
        update.message.reply_text("/Capital")
        update.message.reply_text("/Quetzaltenango")
        update.message.reply_text("/Totonicapan")
        update.message.reply_text("/Progreso")
        update.message.reply_text("/Sacatepequez")  

def bodega(update, context):
        update.message.reply_text("¿En qué lugar de Guatemala desea su bodega?")
        update.message.reply_text("/Capital")
        update.message.reply_text("/Quetzaltenango")
        update.message.reply_text("/Totonicapan")
        update.message.reply_text("/Progreso")
        update.message.reply_text("/Sacatepequez")  

def casa(update, context):
        update.message.reply_text("¿En qué lugar de Guatemala desea su caasa?")
        update.message.reply_text("/Capital")
        update.message.reply_text("/Quetzaltenango")
        update.message.reply_text("/Totonicapan")
        update.message.reply_text("/Progreso")
        update.message.reply_text("/Sacatepequez")                        

def capital(update, context):
        update.message.reply_text("En la Capital hay 3 inmuenbles disponibles")

def quetzaltenango(update, context):
        update.message.reply_text("En Quetzaltenango hay 2 inmuebles disponibles")

def totonicapan(update, context):
        update.message.reply_text("En Totonicapan hay 2 inmuebles disponibles")        

def progreso(update, context):
        update.message.reply_text("En El Progreso hay 3 inmuebles disponibles")

def sacatepequez(update, context):
        update.message.reply_text("En Sacatepéquez hay 2 inmuebles disponibles")


def main():
    updater = Updater("5148207681:AAEnHDj3uZpYMT5dXeMWmcDfl-B_QkM92-M", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("venta", venta))
    dp.add_handler(CommandHandler("tipo", tipo)) 
    dp.add_handler(CommandHandler("apartamento", apartamento))
    dp.add_handler(CommandHandler("local", local))
    dp.add_handler(CommandHandler("bodega", bodega))
    dp.add_handler(CommandHandler("casa", casa))
    dp.add_handler(CommandHandler("capital", capital))
    dp.add_handler(CommandHandler("quetzaltenango", quetzaltenango))
    dp.add_handler(CommandHandler("totonicapan", totonicapan))
    dp.add_handler(CommandHandler("progreso", progreso))
    dp.add_handler(CommandHandler("sacatepequez", sacatepequez))

    dp.add_handler(MessageHandler(Filters.text, alquiler))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()