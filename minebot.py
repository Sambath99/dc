from javascript import require, On, Once
from concurrent.futures import ThreadPoolExecutor

# Import the JavaScript library
mineflayer = require("mineflayer")

# Function to create and start a bot
def create_bot(bot_name):
    bot = mineflayer.createBot({
        "username": bot_name,
        "host": "makongmc.lol",
        "port": 25565,
        "version": "1.20.1",
        "hideErrors": False
    })

    @On(bot, "login")
    def on_login(this):
        print(f"{bot_name} has logged in.")

def main():
    num_bots = int(input("How many bots do you want to create? "))
    base_name = input("What is the base name for the bots? ")

    with ThreadPoolExecutor() as executor:
        futures = []
        for i in range(1, num_bots + 1):
            bot_name = f"{base_name}{i}"
            print(f"Creating bot: {bot_name}")
            future = executor.submit(create_bot, bot_name)
            futures.append(future)

        # Wait for all bots to finish
        for future in futures:
            future.result()

if __name__ == "__main__":
    main()
