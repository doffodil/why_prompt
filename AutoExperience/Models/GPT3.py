import openai
API_KEY = "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"

class GPT3():
    """
    default GPT3 Model(text-davinci-002)
    """

    def __init__(self, parameters):
        self.openai = openai
        self.openai.api_key = API_KEY
        self.engine = parameters['model_type']
        self.max_tokens = parameters['max_tokens']
        self.top_p = parameters['top_p']
        self.temperature = parameters['temperature']
        self.frequency_penalty = parameters['frequency_penalty']
        self.presence_penalty = parameters['presence_penalty']
        self.suffix = parameters['suffix']

    def generate_output(self, input_text):
        response = self.openai.Completion.create(
            engine=self.engine,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            suffix = self.suffix,
            prompt=input_text,
        )
        model_output = response['choices'][0]['text']
        return model_output