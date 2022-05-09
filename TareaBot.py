
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
    if(update.message.text.upper().find("VENTA") > 0):
        update.message.reply_text("Si hay Stock")
        
def  tipo(update, context):
    if(update.message.text.upper().find("TIPO") > 0):
        update.message.reply_text("/Apartamento")
        update.message.reply_text("/Local")
        update.message.reply_text("/Bodega")
        update.message.reply_text("/Casa")

def apartamento(update, context):
    if(update.message.text.upper().find("APARTAMENTO") > 0):
        update.message.reply_text("/ubicacion")

def local(update, context):
    if(update.message.text.upper().find("LOCAL") > 0):
        update.message.reply_text("/ubicacion")

def bodega(update, context):
    if(update.message.text.upper().find("BODEGA") > 0):
        update.message.reply_text("/ubicacion")

def casa(update, context):
    if(update.message.text.upper().find("CASA") > 0):
        update.message.reply_text("/ubicacion")

def ubicacion(update, context):
    if(update.message.text.upper().find("UBICACION") > 0):
        update.message.reply_text("/Capital")
        update.message.reply_text("/Quetzaltenango")
        update.message.reply_text("/Totonicapan")
        update.message.reply_text("/Progreso")
        update.message.reply_text("/Sacatepéquez")                      

def capital(update, context):
    if(update.message.text.upper().find("CAPITAL") > 0):
        update.message.reply_text("")

def quetzaltenango(update, context):
    if(update.message.text.upper().find("QUETZALTENANGO") > 0):
        update.message.reply_text("")

def totonicapan(update, context):
    if(update.message.text.upper().find("TOTONICAPAN") > 0):
        update.message.reply_text("")        

def progreso(update, context):
    if(update.message.text.upper().find("PROGRESO") > 0):
        update.message.reply_text("")

def sacatepequez(update, context):
    if(update.message.text.upper().find("SACATEPEQUEZ") > 0):
        update.message.reply_text("")

def main():
    updater = Updater("5148207681:AAEnHDj3uZpYMT5dXeMWmcDfl-B_QkM92-M", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, alquiler))
    dp.add_handler(MessageHandler(Filters.text, venta))
    dp.add_handler(MessageHandler(Filters.text, tipo))
    dp.add_handler(MessageHandler(Filters.text, apartamento))
    dp.add_handler(MessageHandler(Filters.text, local))
    dp.add_handler(MessageHandler(Filters.text, bodega))
    dp.add_handler(MessageHandler(Filters.text, casa))
    dp.add_handler(MessageHandler(Filters.text, ubicacion))
    dp.add_handler(MessageHandler(Filters.text, capital))
    dp.add_handler(MessageHandler(Filters.text, quetzaltenango))
    dp.add_handler(MessageHandler(Filters.text, totonicapan))
    dp.add_handler(MessageHandler(Filters.text, progreso))
    dp.add_handler(MessageHandler(Filters.text, sacatepequez))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()