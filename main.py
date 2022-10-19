import logging
from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import filters, MessageHandler, ApplicationBuilder

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.ERROR
)

# bot should only work on this chat
# Chats who use public delete service msg bots are risking privacy and they are not even efficient as they are managing
# a lot of chats at the same time
# This bot is designed to handle only one chat - Setting up a Webhook could make it even more faster and efficient
THE_GROUPS_CHAT_ID = -1271840794656  # this is a random number


async def listen_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Listen to all msgs and when a service message type of message is received delete it
    """
    # print(update)

    if update.effective_chat.type == "group" or "supergroup":
        if update.effective_chat.id == THE_GROUPS_CHAT_ID:

            # deleting name change requests
            if update.message.new_chat_title is not None:
                await context.bot.delete_message(update.effective_chat.id, update.message.message_id)

            # deleting chat member left service msg
            if update.message.left_chat_member is not None:
                await context.bot.delete_message(update.effective_chat.id, update.message.message_id)

            # deleting new join service msgs
            if len(update.message.new_chat_members) > 0:
                await context.bot.delete_message(update.effective_chat.id, update.message.message_id)

            # deleting new chat photo added service msgs
            if len(update.message.new_chat_photo) > 0:
                await context.bot.delete_message(update.effective_chat.id, update.message.message_id)

            # deleting chat photo deleted service msgs
            if update.message.delete_chat_photo:
                await context.bot.delete_message(update.effective_chat.id, update.message.message_id)


if __name__ == '__main__':
    token = ""
    application = ApplicationBuilder().token(token).build()

    main_h = MessageHandler(filters=filters.ALL, callback=listen_all)

    application.add_handler(main_h)

    application.run_polling(allowed_updates=Update.ALL_TYPES)
