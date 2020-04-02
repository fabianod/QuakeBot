# credits - CoffeePanda0 for the awful code
import sys, os.path, sqlite3, random, discord, datetime

client = discord.Client()
logfile = open("quakemod.log", "a+")

def log(type, content):
	logfile.write("%s - %s: %s \n" % (type, datetime.datetime.now(), content))
	logfile.flush()

try:
	db = sqlite3.connect("quakemod")
	cursorDB = db.cursor()
except:
	print("An error occured whilst connecting to the database.")
	log("Fatal Error", "Database connection failed")
	sys.exit("A connection to the database could not be established.")
try:
	cursorDB.execute("CREATE TABLE IF NOT EXISTS users (id, score)")
	db.commit()
except:
	print("An error creating the database occured")
	log("Fatal error", "Could not create database")

@client.event
async def on_ready():
	print("Bot is ready")
	log("Status", "Bot succesfully started")
	await client.change_presence(activity=discord.Game(name="THETA: A MOD FOR QUAKE"))

@client.event
async def on_message(message):
	cursorDB.execute("SELECT * FROM users WHERE id = ?", (message.author.id,))
	q = cursorDB.fetchall()
	if !q:
		cursorDB.execute("INSERT INTO users (id, score) VALUES (?, ?)", (message.author.id, 0))
		db.commit()
		log("Users", "Added user to database")
	try:
		if message.author == client.user:
			return
		if "quake" in message.content.lower():
			if message.content.lower() != "$quakemodgood":
				await message.channel.send("QUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\nQUAKE MOD\n")
		if message.content.startswith("$"):
			if message.content.lower() == "$help":
				await message.channel.send("""
```
  ____              _        ____        _
  / __ \            | |      |  _ \      | |
 | |  | |_   _  __ _| | _____| |_) | ___ | |_
 | |  | | | | |/ _` | |/ / _ \  _ < / _ \| __|
 | |__| | |_| | (_| |   <  __/ |_) | (_) | |_
  \___\_\\__,_|\__,_|_|\_\___|____/ \___/ \__|
Commands list for quake bot:\n
$help - Displays this message
$coin - Flip a coin
$credits - Shows your credits
$QUAKEMODGOOD - Gives you credits
$server - Shows best server invite
       ```""")
			
			elif message.content.lower() == "$server":
				await message.channel.send("https://discord.gg/uc9tsDV")
			elif message.content.lower() == "$ping":
				await message.channel.send("Sorry for the ping @everyone")
			elif message.content.lower() == "$coin":
				if random.choice([True, False]) == True:
					await message.channel.send("Heads!")
				else:
					await message.channel.send("Tails!")
			elif message.content.lower() == "$secretshutdown":
				if message.author.id == 377930084490936320:
					await message.channel.send("Restarting...")
				else:
					await message.channel.send("You can't do that!")
					cursorDB.execute("SELECT score FROM users WHERE id = ?", (message.author.id,))
					q = cursorDB.fetchall()
					newscore = int(q[0][0]) - 1000
					cursorDB.execute("UPDATE users SET score = ? WHERE id = ?", (newscore, message.author.id))
					await message.channel.send("Your Credits are: %s" % (newscore))
			elif message.content.lower() == "$quakemodgood":
				cursorDB.execute("SELECT score FROM users WHERE id = ?", (message.author.id,))
				q = cursorDB.fetchall()
				newscore = int(q[0][0]) + 100
				cursorDB.execute("UPDATE users SET score = ? WHERE id = ?", (newscore, message.author.id))
				db.commit()
				await message.channel.send("Your Credits are: %s" % (newscore))
			elif message.content.lower() == "$credits":
				cursorDB.execute("SELECT score FROM users WHERE id = ?", (message.author.id,))
				q = cursorDB.fetchall()
				await message.channel.send("Your Credits are: %s" % (q[0][0]))
			else:
				await message.channel.send("Sorry, no command was found. Maybe try ```$help```")
	except Exception as e:
    		log("Error", e)

client.run("uwu")
logfile.close()

