# why_prompt


# quick start

```Python
from Parameter import Parameter
from AutoExperience.Math23K import AutoExpMath23K

# set parameters
exp_parameter = Parameter(
    prompt='', # set your prompt
)
exp = AutoExpMath23K(exp_parameter)
# 数据可选['tiny','small','large','all']
exp1_result = exp.get_experience_result(data_type='tiny')
print(exp_result) # TODO: Better display
print()
```

上述代码将使用默认的参数，和默认的prompt拼接方式，自动进行试验并返回结果

# 更改参数

直接输入参数的键值对可以覆盖默认参数，默认参数如下。值得注意的是greedy默认为TRUE，因为top-p通过投票计算精度的功能还没上。

```Python
{
    prompt, # prompt必填
    model='GPT3', # [GPT3]
    model_type='text-davinci-002', # 参照openAI的engine list
    greedy=True,
    max_out_length=200,
    top_p=0.5,
    temperature=0.5,
    frequency_penalty=0,
    presence_penalty=0,
}
```

# 更改prompt拼接方式

通过重写`AutoExpMath23K`中的`format_model_input`方法更改prompt的拼接方式

```Python
class exp_demo(AutoExpMath23K):
    def format_model_input(self, data_item, prompt):
        # data_item： 一条数据，字段与原数据相同
        # prompt： parameter中的传入参数
        model_iput = f"问题：{data_item['original_text']}\n" \
                     f"答案：{prompt}"
        return model_iput

exp = exp_demo(parameter=exp_parameter)
```

以下为示例程序

```Python
from Parameter import Parameter
from AutoExperience.Math23K import AutoExpMath23K

# set parameters
exp_parameter = Parameter(
    prompt='按照以下思路作答，',
)

class exp_demo(AutoExpMath23K):
    def format_model_input(self, data_item, prompt):
        model_iput = f"问题：{data_item['original_text']}\n" \
                     f"答案：{prompt}"
        return model_iput

exp = exp_demo(parameter=exp_parameter)

exp_result = exp.get_experience_result(data_type='tiny')
print(exp_result) # TODO: Better display
print()
```

# 返回实验结果

将以json的格式返回的实验结果，以下为简单示例

original_data：与源数据保持一致

question：问题，

ans：答案

model_input：模型输入，问题和prompt拼接好后的输入

model_output：模型输出，GPT3接口返回的输出，未作改变

model_corrent：如果ans在model_output中出现，就视为True（回答正确）

accuracy：基于该数据集，模型回答的准确率

datetime：实验运行结束的时间，和excel的名称

prompt：传入参数中的prompt，我更愿意称之为**关键提示信息**



```JSON
{
  "result_data": [
    {
      "id": 317,
      "original_data": {
        "id": 317,
        "original_text": "5年一班原有班费24.2元，同学们卖废品又得到16.4元．用这些钱可以买14根跳绳，每根跳绳多少钱？",
        "segmented_text": "5 年 一班 原有 班费 24.2 元 ， 同学 们 卖 废品 又 得到 16.4 元 ． 用 这些 钱 可以 买 14 根 跳绳 ， 每 根 跳绳 多少 钱 ？",
        "equation": "x=(24.2+16.4)/14",
        "ans": "2.9"
      },
      "question": "5年一班原有班费24.2元，同学们卖废品又得到16.4元．用这些钱可以买14根跳绳，每根跳绳多少钱？",
      "answer": "2.9",
      "model_input": "问题：5年一班原有班费24.2元，同学们卖废品又得到16.4元．用这些钱可以买14根跳绳，每根跳绳多少钱？\n答案：按照以下思路作答，",
      "model_output": "\n\n1.首先，我们知道5年一班原有班费24.2元，同学们卖废品又得到16.4元，这样我们就可以得到40.6元这个总金额；\n\n2.然后，我们知道这些钱可以买14根跳绳，那么每根跳绳就是40.6元除以14根，得到2.9元。",
      "model_corrent": true
    },
    ########此处省略18条#######
    {
      "id": 22440,
      "original_data": {
        "id": 22440,
        "original_text": "小华看一本96页的故事书，看了25%一共看了多少页．",
        "segmented_text": "小 华 看 一本 96 页 的 故事书 ， 看 了 25% 一共 看 了 多少 页 ．",
        "equation": "x=96*25%",
        "ans": "24"
      },
      "question": "小华看一本96页的故事书，看了25%一共看了多少页．",
      "answer": "24",
      "model_input": "问题：小华看一本96页的故事书，看了25%一共看了多少页．\n答案：按照以下思路作答，",
      "model_output": "可以得到答案：\n\n小华看了25%的故事书，那么小华看了故事书的1/4，也就是故事书的1/4页。\n\n所以小华看了故事书的1/4页，那么小华看了故事书的1/4×96页，也就是故事书的24页。",
      "model_corrent": true
    }
  ],
  "accuracy": 0.3,
  "datetime": "2022-06-25-11-04-17",
  "prompt": "按照以下思路作答，"
}
```

# 自动记录实验日志

实验过程中会自动生成：

- 一条实验日志，存在`all_experience_record.log`文件中
- 一个Excel文件（对应上述实验结果中的result_data，没有accuracy和prompt），通过时间命名，方便查看，复制实验记录。
- 一个json，作为返回的实验结果

# 使用建议

建议分组实验，每组实验建一个文件夹，日志和Excel会自动保存在该目录下

# TODO list
- 当greedy=False时，使用vote计算accuracy
- openai 调用限制，多次调用后会把我的key重置。加了两秒等待也不行
- 增加其他模型【opt】