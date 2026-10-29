VORTEXSMP DISCORD SETUP KIT
===========================

WHAT THIS KIT DOES
------------------
The setup script creates/reuses:
- Roles: Owner, Admin, Moderator, Support, Developer, VIP, Member, Newcomer, Muted
- Categories and text channels for information, community, support, and staff
- Voice channels: General, Minecraft, AFK
- Basic category/channel permissions
- Starter messages for welcome, rules, server-info, announcements, help, giveaways, suggestions, and ticket information

IMPORTANT LIMITATIONS
---------------------
- This does NOT create a Discord server in your account.
- First create a blank server in Discord.
- It does NOT create a hosted Discord Server Template URL. Discord generates that URL from an existing server after you build it.
- Bot integrations (Ticket Tool, Carl-bot, DiscordSRV) must be configured separately.
- Review all permissions and rules before inviting people.
- Do not run this on a server you don't own or administer.
- The script is designed to reuse matching roles/channels where possible, but review before rerunning.

REQUIREMENTS
------------
Python 3.10 or newer is recommended.
A Discord bot application with a bot token.
The bot must be invited to your server with these permissions:
- Manage Roles
- Manage Channels
- View Channels
- Send Messages
- Read Message History
- Embed Links

The bot's highest role must be above the roles it creates in Server Settings > Roles.
Only use a bot token from your own application. Never share it.

STEP 1 — CREATE YOUR DISCORD SERVER
-----------------------------------
In Discord, click the + button in the server list and create a server named VortexSMP.

STEP 2 — CREATE A BOT
---------------------
1. Visit https://discord.com/developers/applications
2. Click New Application and name it VortexSMP Setup.
3. Open the Bot tab and create a bot if prompted.
4. Reset/copy its token. Keep it private.
5. Open OAuth2 > URL Generator.
6. Select the bot scope.
7. Select the permissions listed above (Manage Roles, Manage Channels, View Channels, Send Messages, Read Message History, Embed Links).
8. Open the generated URL and invite the bot to your VortexSMP server.
9. In Discord, open Server Settings > Roles and move the bot's role above the roles the script will create.

STEP 3 — GET THE SERVER ID
--------------------------
1. Discord Settings > Advanced > enable Developer Mode.
2. Right-click your VortexSMP server icon or use the server menu.
3. Click Copy Server ID.

STEP 4 — INSTALL PYTHON PACKAGE
-------------------------------
Open Terminal in the folder containing setup_vortexsmp.py and run:

  python3 -m pip install -U discord.py

STEP 5 — SET ENVIRONMENT VARIABLES AND RUN
------------------------------------------
macOS / Linux (replace values; don't include angle brackets):

  export DISCORD_BOT_TOKEN="PASTE_YOUR_BOT_TOKEN_HERE"
  export DISCORD_GUILD_ID="PASTE_NUMERIC_SERVER_ID_HERE"
  python3 setup_vortexsmp.py

Windows PowerShell:

  $env:DISCORD_BOT_TOKEN="PASTE_YOUR_BOT_TOKEN_HERE"
  $env:DISCORD_GUILD_ID="PASTE_NUMERIC_SERVER_ID_HERE"
  py setup_vortexsmp.py

The script should print the channels and roles it creates. It closes after setup.

STEP 6 — FINISH MANUALLY
------------------------
1. Edit #server-info and replace YOUR_SERVER_IP and YOUR_VERSION.
2. Review #rules and adjust the gameplay rules to match your SMP.
3. Give yourself the Owner role if appropriate, and assign Member/Newcomer roles as desired.
4. Check permissions using a normal test account.
5. Configure Ticket Tool for private support tickets.
6. Configure Carl-bot for moderation, logs, and optional welcome automation.
7. Install DiscordSRV on the Paper server and configure the Discord bot/chat channel.
8. When ready, generate a template: Server Settings > Server Templates > Generate Template.
   Discord's template URL is generated from the actual server, not from this zip.

SECURITY
--------
- Never share your bot token or commit it to GitHub.
- If a token leaks, reset it in the Developer Portal immediately.
- Don't grant Administrator to general-purpose bots unless absolutely necessary.
- This setup script grants the Owner role Administrator. Assign that role only to your own account.
- Verify role order, channel permissions, and staff access before launch.
