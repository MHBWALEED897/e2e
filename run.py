import waleede2enew

if __name__ == "__main__":
    try:
        waleede2enew.main()
    except AttributeError:
        # Agar main function direct access na ho raha ho class initialize karein
        bot = waleede2enew.FacebookFirefoxBot()
        bot.run()
