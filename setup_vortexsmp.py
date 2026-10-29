"""
VortexSMP Discord Setup
Creates roles, categories, text/voice channels, permissions, and starter messages.

IMPORTANT:
- Create a Discord server first.
- Create a Discord bot in the Discord Developer Portal and invite it to your server.
- Enable the bot's Server Members Intent only if you later add features that need it; this script doesn't need it.
- Give the bot Manage Roles, Manage Channels, View Channels, Send Messages, Embed Links, and Read Message History.
- The bot's highest role must be above the roles it creates.
- Set DISCORD_BOT_TOKEN and DISCORD_GUILD_ID as environment variables.
- Run this script once. It avoids duplicating matching roles/categories/channels, but review the server if rerunning.
"""

import os
import asyncio
import discord

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID_RAW = os.getenv("DISCORD_GUILD_ID")

if not TOKEN or not GUILD_ID_RAW:
    raise SystemExit(
        "Missing environment variables. Set DISCORD_BOT_TOKEN and DISCORD_GUILD_ID first. "
        "See README.txt."
    )

try:
    GUILD_ID = int(GUILD_ID_RAW)
except ValueError:
    raise SystemExit("DISCORD_GUILD_ID must be the numeric server ID.")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

ROLE_CONFIG = [
    ("Owner", 0xE74C3C, discord.Permissions(administrator=True)),
    ("Admin", 0xE67E22, discord.Permissions(
        manage_guild=True, manage_channels=True, manage_messages=True,
        kick_members=True, ban_members=True, moderate_members=True,
        view_audit_log=True, manage_nicknames=True
    )),
    ("Moderator", 0x3498DB, discord.Permissions(
        manage_messages=True, moderate_members=True, kick_members=True,
        view_audit_log=True, read_message_history=True
    )),
    ("Support", 0x2ECC71, discord.Permissions(
        view_channels=True, send_messages=True, read_message_history=True
    )),
    ("Developer", 0x9B59B6, discord.Permissions(
        view_channels=True, send_messages=True, read_message_history=True,
        attach_files=True, embed_links=True
    )),
    ("VIP", 0xF1C40F, discord.Permissions(
        view_channels=True, send_messages=True, read_message_history=True
    )),
    ("Member", 0xD6D6DE, discord.Permissions(
        view_channels=True, send_messages=True, read_message_history=True,
        add_reactions=True, attach_files=True, embed_links=True,
        connect=True, speak=True
    )),
    ("Newcomer", 0x92939F, discord.Permissions(
        view_channels=True, read_message_history=True
    )),
    ("Muted", 0x747580, discord.Permissions(
        view_channels=True, read_message_history=True
    )),
]

CATEGORY_CONFIG = [
    ("START HERE", [
        ("welcome", "Welcome and getting started", "readonly"),
        ("announcements", "Official VortexSMP announcements", "readonly"),
        ("server-info", "Minecraft server address and details", "readonly"),
        ("rules", "Community and Minecraft rules", "readonly"),
    ]),
    ("COMMUNITY", [
        ("general", "Chat with the VortexSMP community", "chat"),
        ("screenshots", "Share builds and screenshots", "chat"),
        ("trading", "Player trading discussion", "chat"),
        ("suggestions", "Suggest improvements to the server", "chat"),
        ("giveaways", "Giveaway announcements and winners", "readonly"),
    ]),
    ("SUPPORT", [
        ("help", "Ask questions and get help", "chat"),
        ("open-a-ticket", "Use the ticket bot panel to contact staff", "readonly"),
    ]),
    ("STAFF ONLY", [
        ("staff-chat", "Private staff coordination", "staff"),
        ("staff-logs", "Moderation and bot logs", "staff"),
        ("punishment-logs", "Punishment records", "staff"),
        ("ticket-transcripts", "Private ticket transcripts", "staff"),
    ]),
]

VOICE_CHANNELS = [
    ("General", "public"),
    ("Minecraft", "public"),
    ("AFK", "public"),
]

STARTER_MESSAGES = {
    "welcome": (
        "# 🌌 WELCOME TO VORTEXSMP\n\n"
        "Welcome to the community! 💜\n\n"
        "**Start here:**\n"
        "1. Read #rules before chatting.\n"
        "2. Visit #server-info for the Minecraft IP and version.\n"
        "3. Say hello in #general.\n"
        "4. Need help? Visit #open-a-ticket.\n\n"
        "Have fun, respect other players, and enjoy your adventure!\n\n"
        "**VortexSMP — Your world, your adventure.**"
    ),
    "announcements": (
        "# 📢 VORTEXSMP ANNOUNCEMENTS\n\n"
        "Official server updates, events, maintenance notices and important news will be posted here."
    ),
    "server-info": (
        "# 🎮 VORTEXSMP — SERVER INFORMATION\n\n"
        "**Server IP:** `YOUR_SERVER_IP`\n"
        "**Minecraft version:** `YOUR_VERSION`\n"
        "**Edition:** Java Edition\n"
        "**Gamemode:** Survival SMP\n\n"
        "Replace the placeholders above before inviting players.\n\n"
        "Build your base, explore the world, trade with others and take part in community events."
    ),
    "rules": (
        "# 📜 VORTEXSMP — COMMUNITY RULES\n\n"
        "**1. Respect everyone.** No harassment, bullying, discrimination or targeted abuse.\n\n"
        "**2. No cheating.** Hacks, unfair modifications and prohibited exploits are not allowed.\n\n"
        "**3. Report bugs.** Do not abuse duplication glitches or economy exploits; report them to staff.\n\n"
        "**4. No spam or advertising.** Avoid spam, malicious links and unsolicited promotions.\n\n"
        "**5. Follow the SMP rules.** Griefing, raiding, stealing and PvP rules follow the server's published gameplay policy.\n\n"
        "**6. No scamming.** Follow the server's trading policy and report suspected scams with evidence.\n\n"
        "**7. Keep content appropriate.** No explicit content, threats, doxxing or sharing private information.\n\n"
        "**8. Respect staff.** Follow reasonable moderation instructions and use support to appeal punishments.\n\n"
        "**9. No punishment evasion.** Do not use alternate accounts to evade valid restrictions.\n\n"
        "**10. Report problems responsibly.** Use support channels and do not publicly spread exploit instructions.\n\n"
        "**Possible consequences:** warning, mute, temporary ban or permanent ban depending on severity and history.\n\n"
        "Enjoy VortexSMP! 💜"
    ),
    "giveaways": (
        "# 🎁 VORTEXSMP GIVEAWAYS\n\n"
        "Giveaways and winner announcements will be posted here.\n\n"
        "**Prize:** [PRIZE]\n"
        "**Winners:** [NUMBER]\n"
        "**Closes:** [DATE AND TIME]\n\n"
        "Follow the entry instructions in each giveaway. Staff will never ask for your password or login code."
    ),
    "suggestions": (
        "# 💡 SUGGESTIONS\n\n"
        "Have an idea for VortexSMP?\n\n"
        "**Suggestion:** [Your idea]\n"
        "**Why it would help:** [Reason]\n\n"
        "Keep suggestions respectful and constructive. Staff will review ideas, but not every suggestion can be implemented."
    ),
    "open-a-ticket": (
        "# 🎫 NEED HELP?\n\n"
        "Use the support ticket panel here to contact staff privately.\n\n"
        "Once Ticket Tool is configured, its panel can be posted in this channel. "
        "Until then, contact a staff member or use #help."
    ),
    "help": (
        "# ❓ VORTEXSMP HELP\n\n"
        "Need help? Describe your question clearly and include relevant details.\n"
        "For private matters, use #open-a-ticket once tickets are enabled."
    ),
}

async def find_or_create_role(guild, name, colour, permissions):
    role = discord.utils.get(guild.roles, name=name)
    if role:
        print(f"Role exists: {name}")
        return role
    role = await guild.create_role(
        name=name, colour=discord.Colour(colour), permissions=permissions,
        reason="VortexSMP server setup"
    )
    print(f"Created role: {name}")
    return role

async def find_or_create_category(guild, name, overwrites):
    category = discord.utils.get(guild.categories, name=name)
    if category:
        print(f"Category exists: {name}")
        await category.edit(overwrites=overwrites, reason="VortexSMP permissions setup")
        return category
    category = await guild.create_category(
        name=name, overwrites=overwrites, reason="VortexSMP server setup"
    )
    print(f"Created category: {name}")
    return category

async def find_or_create_text_channel(guild, category, name, topic, overwrites):
    channel = discord.utils.get(guild.text_channels, name=name)
    if channel:
        print(f"Channel exists: #{name}")
        await channel.edit(category=category, topic=topic, overwrites=overwrites)
        return channel
    channel = await guild.create_text_channel(
        name=name, category=category, topic=topic, overwrites=overwrites,
        reason="VortexSMP server setup"
    )
    print(f"Created channel: #{name}")
    return channel

async def find_or_create_voice_channel(guild, category, name, overwrites):
    channel = discord.utils.get(guild.voice_channels, name=name)
    if channel:
        print(f"Voice channel exists: {name}")
        await channel.edit(category=category, overwrites=overwrites)
        return channel
    channel = await guild.create_voice_channel(
        name=name, category=category, overwrites=overwrites,
        reason="VortexSMP server setup"
    )
    print(f"Created voice channel: {name}")
    return channel

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    guild = client.get_guild(GUILD_ID)
    if guild is None:
        print("ERROR: Bot cannot find this server. Check DISCORD_GUILD_ID and invite the bot.")
        await client.close()
        return

    me = guild.me
    if not me.guild_permissions.manage_roles or not me.guild_permissions.manage_channels:
        print("ERROR: Bot needs Manage Roles and Manage Channels permissions.")
        await client.close()
        return

    # Create roles. Existing roles are reused.
    roles = {}
    for name, colour, perms in ROLE_CONFIG:
        roles[name] = await find_or_create_role(guild, name, colour, perms)

    everyone = guild.default_role
    member = roles["Member"]
    newcomer = roles["Newcomer"]
    owner = roles["Owner"]
    admin = roles["Admin"]
    moderator = roles["Moderator"]
    support = roles["Support"]
    developer = roles["Developer"]

    # Keep general access simple. Members can chat; newcomers can read until given Member.
    public_view = {
        everyone: discord.PermissionOverwrite(
            view_channel=True, read_message_history=True,
            send_messages=False, create_public_threads=False,
            create_private_threads=False, mention_everyone=False
        ),
        member: discord.PermissionOverwrite(
            view_channel=True, read_message_history=True,
            send_messages=True, add_reactions=True, attach_files=True,
            embed_links=True, send_messages_in_threads=True
        ),
        newcomer: discord.PermissionOverwrite(
            view_channel=True, read_message_history=True,
            send_messages=False
        ),
    }
    staff_readonly = discord.PermissionOverwrite(
        view_channel=True, send_messages=True, read_message_history=True,
        manage_messages=True
    )
    for r in [owner, admin, moderator, support]:
        public_view[r] = staff_readonly

    # Staff-only category. Explicitly deny everyone and non-staff member roles.
    staff_overwrites = {
        everyone: discord.PermissionOverwrite(view_channel=False),
        member: discord.PermissionOverwrite(view_channel=False),
        newcomer: discord.PermissionOverwrite(view_channel=False),
        roles["VIP"]: discord.PermissionOverwrite(view_channel=False),
        roles["Muted"]: discord.PermissionOverwrite(view_channel=False),
    }
    for r in [owner, admin, moderator, support, developer]:
        staff_overwrites[r] = discord.PermissionOverwrite(
            view_channel=True, read_message_history=True,
            send_messages=True, attach_files=True, embed_links=True
        )

    created_channels = {}
    for cat_name, channels in CATEGORY_CONFIG:
        category_overwrites = staff_overwrites if cat_name == "STAFF ONLY" else public_view
        category = await find_or_create_category(guild, cat_name, category_overwrites)
        for channel_name, topic, kind in channels:
            overwrites = category_overwrites
            if kind == "readonly":
                overwrites = dict(public_view)
                # @everyone can read but not post; trusted staff can post.
                for r in [owner, admin, moderator, support, developer]:
                    overwrites[r] = discord.PermissionOverwrite(
                        view_channel=True, send_messages=True, read_message_history=True
                    )
            elif kind == "staff":
                overwrites = staff_overwrites
            ch = await find_or_create_text_channel(guild, category, channel_name, topic, overwrites)
            created_channels[channel_name] = ch

    # Voice category and channels
    voice_category = await find_or_create_category(guild, "VOICE", public_view)
    for name, _ in VOICE_CHANNELS:
        voice_overwrites = dict(public_view)
        if name == "AFK":
            pass
        await find_or_create_voice_channel(guild, voice_category, name, voice_overwrites)

    # Post each starter message only if the channel is empty.
    for channel_name, message in STARTER_MESSAGES.items():
        channel = created_channels.get(channel_name)
        if channel is None:
            continue
        try:
            async for _ in channel.history(limit=1):
                break
            else:
                await channel.send(message)
                print(f"Posted starter message in #{channel_name}")
        except discord.Forbidden:
            print(f"Cannot post in #{channel_name}; check bot permissions.")
        except Exception as exc:
            print(f"Could not post in #{channel_name}: {exc}")

    print("\nSetup finished.")
    print("NEXT: replace YOUR_SERVER_IP and YOUR_VERSION in #server-info.")
    print("NEXT: configure Ticket Tool and DiscordSRV separately.")
    print("NEXT: assign the Member role to approved members, and Newcomer to new members if desired.")
    print("IMPORTANT: check role order and permissions manually before inviting players.")
    await client.close()

client.run(TOKEN)
