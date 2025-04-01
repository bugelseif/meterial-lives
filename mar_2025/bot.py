# Import for the Desktop Bot
from botcity.core import DesktopBot


def main():
    bot = DesktopBot()

    # Searching for element 'extensao'
    if not bot.find("extensao", matching=0.97, waiting_time=10000):
        not_found("extensao")
    bot.click()
    
    # degita "botcity"
    bot.paste("botcity")
    bot.enter()
    

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()