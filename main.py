from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

# Configurazione
TOKEN = os.getenv("TELEGRAM_TOKEN")  # Legge il token da Render

# Logica delle risposte (personalizzala come vuoi)
def get_response(user_message: str, user_name: str = None) -> str:
    user_message = user_message.lower()
    
    if "ciao" in user_message:
        return f"Ciao {user_name}! 😊 Sono VoxAssistant. Come posso aiutarti?" if user_name else "Ciao! Sono VoxAssistant. Dimmi pure!"
    elif "che tempo fa" in user_message:
        return "Non posso controllare il meteo, ma posso consigliarti di usare un'app come Meteo.it!"
    elif "qiro" in user_message:
        return "QIRO è un bravo assistente, ma io sono specializzato in risposte personalizzate! 😎"
    elif "grazie" in user_message:
        return "Di nulla! Sono qui per aiutarti."
    else:
        return "Non ho capito. Prova a chiedermi qualcos'altro!"

# Comando /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("🔊 Ciao! Sono **VoxAssistant**, il tuo bot personalizzato. Scrivimi qualcosa!")

# Gestione messaggi
def handle_message(update: Update, context: CallbackContext):
    user_name = update.message.from_user.first_name
    response = get_response(update.message.text, user_name)
    update.message.reply_text(response)

# Avvio bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    updater.start_polling()
    print("✅ Bot avviato!")
    updater.idle()

if __name__ == "__main__":
    main()