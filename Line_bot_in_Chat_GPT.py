from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.exceptions import InvalidSignatureError
import openai

line_bot_api = LineBotApi('fjdN+8jhPC1WBqLcNmRjhEuogkn4Jl8ZBCz9H7bkJXZxtNq0F1hB2CaKoNsZBJtGWd4q1u10W/f4KihllwtqE0LpuVsQzH+skhJGMruWOnCxeenLkfxM8KAWS+nWJWanRkZ1LECPTM2GUvZ6eacykwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('33e91f047b1b433c8c2eff12d4380456')
openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=50,
        n=1,
        stop=None,
        timeout=5,
    )

    message = response.choices[0].text.strip()
    return message

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    reply_message = generate_response(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_message)
    )
