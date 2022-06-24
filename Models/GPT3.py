import openai


class GPT3():
    """
    default GPT3 Model(text-davinci-002)
    """

    def __init__(self, api_key, top_p):
        self.openai = openai
        self.openai.api_key = api_key
        self.engine = 'text-davinci-002'
        self.max_out_length = '200'
        self.top_p = top_p
        self.temperature = 0.5
        self.frequency_penalty = 0
        self.presence_penalty = 0

    def generate_output(self, input_text):
        response = self.openai.Completion.create(
            engine=self.engine,
            max_tokens=self.max_out_length,
            top_p=self.top_p,
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            prompt=input_text,
        )
        model_output = response['choices'][0]['text']
        return model_output


class GPT3Greedy(GPT3):
    def __init__(self):
        super(GPT3Greedy, self).__init__()
        self.top_p = 0

class GPT3Topp(GPT3)
    def __init__(self, top_p):
        super(GPT3Topp, self).__init__()
        self.top_p=top_p
