client = OpenAI(api_key=os.getenv("CHAT_GPT_TOKEN"))

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "developer", "content": "разговаривай максимально просто и коротко"},
            {"role": "user", "content": "Что делать в баскетболе, если я лось"},
        ],
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=response.output_text
    )