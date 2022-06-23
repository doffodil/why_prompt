import openai

class GPT3():
    """
    GPT3 API
    """

    def __init__(self,
                 engine="text-davinci-002",
                 max_out_length=200,
                 top_p=1.0,
                 # top_k=3,
                 temperature=0.9,
                 frequency_penalty=0.0,
                 presence_penalty=0.0, ):
        self.openai = openai
        self.openai.api_key = "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"
        self.engine = engine
        self.max_out_length = max_out_length
        self.top_p = top_p
        # self.top_k = top_k
        self.temperature = temperature
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

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