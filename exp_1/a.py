import os
import openai
openai.api_key = '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'
response = openai.Completion.create(
  model="text-davinci-insert-002",
  prompt='姐妹两人同时从相距630米的两地相向而行，妹妹每分钟走60米，姐姐每分钟走80米，经过多少分钟姐妹两人在途中相遇？求解过程：',
  suffix = '所以答案是',
  max_tokens=512,
  top_p=1,
  temperature=0.5,
)

print(response['choices'][0]['text'])