<h1 align=center>💜 EthelMC Discord Bot 💜</h1>
<div align=center>
    <a href="https://discord.gg/QRUUvEaEaM"><img src="https://uce9f44d94788e5fcbe3b31c09e4.previews.dropboxusercontent.com/p/thumb/ACNJxQlIX697ulDpi_Qj6PRQukvzzJeGbm1K0A_of_eENIg9fusj5ou6EIIObfIY4CzrtgQKXRhyh9qXhrmqCHy6MuL41KxGWOgIaNxp-DmbdLKqrfcU_LF9Ki3S6DIXk_XhFsf91hulqvzLCTbBanAQcd0RbRBp_KjJAhD7COBVxcka8oHvAKeiSXFwmZu3FhYQ3aYUGw9lWGPqMkLdQ3bPQr7wWXXPeBDbn2n6S9AqqQivT-dao1In6PIDkZvapysJ3QrsmC_Eu0_VOv-ECy5EKQpYrkjkdEp_EME07gSK42Qd4epbBqUnCnfdQzwkdEu7Wsg-zrlIidDb-AMX3fmZAfEPQ2CbCXeMhpT0uwlHdn6vezv0vobrBwdNG09NXq75p3497vOiYeifBu4YsW2j/p.png"></a>
</div>
EthelMC Discord Bot is a feature-rich Discord bot built with python to enhance the experience on the EthelMC server. This bot provides useful commands, server status monitoring, moderation capabilities, and more.
<br>
<br>

***Learn more about [EthelMC](https://discord.gg/QRUUvEaEaM) by scrolling down to the bottom of the page <3***

## Features 😸

- **Server status** - Get realtime server status and latency directly from within Discord
- **Player lookups** - View currently online players and basic player data
- **Info commands** - Lookup server IP, store links, voting links, etc.
- **Moderation** - Admin commands like purge, clearall, say, sync, etc.
- **Logging** - Logs various events like command usage, violations, bot status, bot errors, etc.
- **And more!** - View all commands with `!commands` or `/commands`

# Commands and Events 📜

> [!NOTE]
> All commands function properly with either the ! prefix or the / prefix :shipit:
## Bot Events 🎉
- **Welcome Message** - Sends a welcome message to new members. Useful for greeting new people.
- **Banned Words** - This event effectively identifies, records, and removes any banned words utilized by users within the Discord server.
- **Reaction on Ping** - This fun and quirky addition to our bot will automatically react with a funny emoji whenever someone pings the users specified.

## Public Commands 👥

- `!ip` - Returns the IP address and port to connect to the Minecraft server. 
- `!status` - Checks the status of the Minecraft server and returns info like online players, latency, etc.
- `!vote` - Provides links to vote for the Minecraft server on voting websites.
- `!store` - Returns a link to the Minecraft server's web store.
- `!colors` - Shows images of all the Minecraft chat color codes.
- `!skin` - Provides instructions on how to change your skin on the Minecraft server.
- `!avatar` - Fetches and displays a user's Discord avatar image.
- `!membercount` - Returns the current member count of the Discord server.
- `!commands` - Lists all the bot's commands.
- `!ping` - Checks the bot's latency and API response time.
- `invite` - Generates a temporary invite link to the server
- `!help` - Explains how to get help/support for the Minecraft server. 
- `!about` - Provides info about the Discord bot.

## Moderator Commands 👨🏻‍💻

- `!admin` - Shows a list of Moderator commands.
- `!say <message>` - Makes the bot say the given message in the channel.
- `!purge <count>` - Purges/deletes the given number of messages in the channel.
- `!kick @user <Reason(Optional)>` - Kicks a member from the server. 
- `!sync` - Syncs the bot's slash commands with Discord.
- `!clearall` - Clears all messages in the current channel.
- `!joinvc1` - Makes the bot join the first voice channel.
- `!joinvc2` - Makes the bot join the second voice channel.
- `!leavevc` - kicks out the bot from the voice channel that has been joined in.

### To Do List 📝

- `embed` - Allows sending a rich embed message with formatted text, images, links, etc. This could be used for announcements, help information, or displaying data.
- `giveaway` - Starts a giveaway event where members can react to enter. Parameters like duration, winners, and prize can be configured. Useful for community engagement.
- `warn` - Warns a member by logging an infraction to their account. Repeated warnings could trigger automatic punishment. Useful for moderation.
- ~~`kick` - Kicks a member from the server. Useful for moderating and removing problematic members.~~ ✅
- `ban` - Permanently bans a user from the server. More severe than a kick. Useful for removing toxic members.
- `unban` - Unbans a previously banned user, allowing them to rejoin the server. Useful if a ban was too harsh or is no longer warranted.
- `restart` - Restarts the bot process. Useful for applying updates or refreshing state.
- `mute` - Temporarily mutes a member from sending messages. Useful as a lighter punishment than a ban.
- `poll` - Starts a poll where members can vote. Useful for gauging community opinions.
- ~~`invite` - Generates a temporary invite link to the server. Useful for recruiting new members.~~ ✅
- `event` - Schedules a recurring event like a game night. Useful for community engagement.
- `backup` - Backs up important data from an specific channel or all channels available in the server.
- ~~`welcome` - Sends a welcome message to new members. Useful for greeting new people.~~
- `goodbye` - Bids farewell to members who left the server. Useful for showing appreciation.

<h1 align=center>🍄 Getting Started 🍄</h1>

## Creating a Discord Bot 🤖

1. To create your own bot in Discord, begin by visiting the [Discord Developer Portal](https://discord.com/developers/applications). Click on the "New Application" button and give your bot a name before creating it. Once your bot is created, navigate to the Bot tab on its page and click on the "Reset Token" button to obtain your bot's Token. Remember to keep this token private and never share it publicly.

2. In the "Privileged Gateway Intents" section, ensure that "SERVER MEMBERS INTENT" and "MESSAGE CONTENT INTENT" are toggled on. Next, head to the OAuth2 tab and switch the "AUTHORIZATION METHOD" to "In-app Authorization." Toggle on "bot" and "applications.commands" under "SCOPES," and select "Administrator" under BOT PERMISSIONS before saving your changes.

3. To generate an OAuth2 URL, move to the OAuth2 URL Generator section. Toggle on "applications.commands" and "bot" under "SCOPES," and ensure that "Administrator" is selected under BOT PERMISSIONS. Scroll down to find the generated URL, open it in a new tab, and choose the server where you want to add your bot.

**That's all it takes to create your bot on Discord!**

## Installation 💻

**Requirements**

- **Python 3.8+**
- discord.py
- aiohttp
- asyncio
- requests
- mcstatus
- youtube_dl
- discord
- discord.py
- discord.ui
- python-dotenv

simply run the command `pip install -r requirements.txt` to install all necessary dependencies.

## Configuration ⚙️

After successfully installing the bot's requirements, navigate to the main file of the bot, `app.py`. Scroll down to where the **Configuration** of the bot begins. Here, you will find various variables that need to be filled with your specific inputs.

For instance, your bot's Token should be assigned to the **BOT_TOKEN** variable using `environment variables` or by adding it to a `.env` file. Additionally, make sure to input the Owner user IDs, server name, address port, server's store website URL, and other relevant details accurately for the bot to function effectively. Review and input all necessary information before running the bot.

## Running the Bot 🚀

You are now ready to run the bot. Simply enter the command below to start the bot:

`python app.py`

The bot is now up and running! Test it out by joining it to your server and using the commands.

## Deployment 🙄

If you are considering deploying this bot on a cloud host to ensure it runs 24/7, simply **fork this repository** and connect it to your hosting service. Insert a custom run command for the bot as `python app.py`.

To avoid potential unhealthy app errors on some hosting platforms due to the bot not responding to any ports, I have included an HTTP server to respond to a specific port. This will allow the bot to pass the health check successfully and prevent any further issues. Please note to set the application's port as `8080` in your hosting service settings.

```python
class HealthCheckHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

health_server = http.server.HTTPServer(('', 8080), HealthCheckHandler)

health_thread = threading.Thread(target=health_server.serve_forever)
health_thread.daemon = True
health_thread.start()
```

## Contributing 😻

Contributions are welcomed! Feel free to open issues or pull requests.

When contributing:

- Open an issue before starting work on any major additions
- Follow existing code style and conventions
- Add/update documentation for new features
- Add tests to ensure functionality and prevent regressions

## Issues and Bugs 🐛
If you encounter any problems, bugs, or errors while using this bot, please feel free to open an issue on the GitHub repository. Providing details on the problem and steps to reproduce it are greatly appreciated!

Feature requests and ideas for improvements are also welcome. Consider opening a pull request if you have a solution to contribute. Your feedback helps make the bot better for everyone!

Let's work together to improve EthelMC Bot and offer the best experience possible for our community. Don't hesitate to speak up if something isn't working as expected. Thanks for your understanding and support!

## License ⚖️
> [!IMPORTANT]
> This project is licensed under the MIT License, granting you the freedom to use, modify, and distribute the software. You are not required to share your modifications, but it is appreciated if you include the original copyright notice and disclaimer. Whether for commercial or non-commercial purposes, feel free to utilize the application as you see fit. And if you make any improvements or changes, please consider giving credit by mentioning my github page in your fork. <3

# Side Note 😇 🎮

If you're curious about **EthelMC**, it's a vibrant and laid-back Minecraft server with a diverse range of exciting plugins. Our community is growing rapidly, filled with friendly and engaging people and staff. I handle the development side of things, ensuring a smooth and enjoyable experience for all. Join our Discord server using the invite link below to connect with other players and have a blast! 💜
<br>
## [EthelMC Discord Server - Click to Join!](https://discord.gg/QRUUvEaEaM)

<div align=center>
    <a href="https://discord.gg/QRUUvEaEaM"><img src="https://uc83766ad7c6fd4eea57919b0f18.previews.dropboxusercontent.com/p/thumb/ACNQjvG32uXqaNMIYUoneIMaqlrUQJQrJSx1sZ1FcQ8iJgdHFkOoD-Lruc_HXR3r5u0AsAx0tce-mz7nbLM2kmm5oVZO7ygViPXC5_BEKSc7U8woiCk1jwU0DL3uTy3Z5EFWS7jU3yfxkNj9qm9NSv_dsFpc31VYgxVyjnI1nWyEDUc2s79t-bNGKL73-QuFJG9HU3CJ8ZqasYFcVaH4n9ashQw1qlcvjD0j9B4l0q1oc2bK4K2CARcjPNvlODY6wATKUG6jWhQ0GX2fEqD-gsQp_grEEpGY4prUjPukEdJ7NLduoWu6Ch2eZY7IF_smus50Yar4fPGIlB4wxwUWJxdVxIwdhCyvi104wiD1EipnxZYv-ERw55sGYsJIB9qqckzs8KT00QTx-72bHn5oK1Ag/p.gif"></a>
</div>