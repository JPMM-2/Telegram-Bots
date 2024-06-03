

def restart(bot):
    # main.py
    import telebot
    from borrar import handle_borrar
    from alta import handle_alta
    from saludo import handle_saludar

    from servicios import handle_servicios 

    # Register the handlers from the modules
    handle_saludar(bot)
    handle_borrar(bot)
    handle_alta(bot)
    handle_servicios(bot)

    # Start polling
    bot.polling()


