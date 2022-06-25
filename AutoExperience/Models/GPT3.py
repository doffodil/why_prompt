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
        self.max_out_length = parameters['max_out_length']
        self.top_p = parameters['top_p']
        self.temperature = parameters['temperature']
        self.frequency_penalty = parameters['frequency_penalty']
        self.presence_penalty = parameters['presence_penalty']

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
