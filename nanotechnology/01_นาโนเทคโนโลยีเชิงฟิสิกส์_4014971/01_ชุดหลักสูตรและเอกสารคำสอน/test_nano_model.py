from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model='gpt-5-mini',
    messages=[
        {'role': 'system', 'content': 'ตอบภาษาไทยอย่างกระชับ'},
        {'role': 'user', 'content': 'เขียนคำอธิบาย 3 ประโยคเกี่ยวกับพื้นที่ผิวต่อปริมาตรของอนุภาคขนาดนาโน'},
    ],
    max_completion_tokens=1500,
)
print(response)
print('choices:', response.choices)
