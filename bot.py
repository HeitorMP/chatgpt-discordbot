import	discord
from	discord.ext import commands
import	openai

openai.api_key = "YOUR APU KEY HERE"

def chatgpt_response(prompt):
	prompt_response = None
	response = openai.Completion.create(
		model="text-davinci-003",
		prompt=prompt,
		temperature=1,
		max_tokens=100
	)
	print(response)
	response_dict = response.get("choices")
	print(response_dict)
	if response_dict and len(response_dict) > 0:
		prompt_response = response_dict[0]["text"]
	return prompt_response

def run_discord_bot():
	TOKEN = 'YOUR BOT TOKEN HERE'
	intents = discord.Intents.all()
	bot = commands.Bot(command_prefix='/', intents = intents)

	@bot.event
	async def on_ready():
		print('Bot is online!')

	@bot.command()
	async def chat(ctx):
		user_message = ctx.message.content
		bot_response = chatgpt_response(prompt=user_message)
		print(bot_response)
		await ctx.send(f'{bot_response}')

	bot.run(TOKEN)
