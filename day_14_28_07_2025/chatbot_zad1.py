import os

from openai import OpenAI


# pip install openai

class ChatBot:
    def __init__(self, model="gpt-3.5-turbo"):
    # def __init__(self, model="gpt-4-0613"):
    # def __init__(self, model="gpt-4.1"):
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)
        self.message = []
        self.model = model

    def add_message(self, role, content):
        if role in ["user", "assistant"]:
            self.message.append(
                {"role": role, "content": content}
            )
        else:
            raise ValueError("Role must be 'user' or 'assistant'!")

    def get_models(self):
        print([m.id for m in self.client.models.list().data])

    def get_response(self, user_message):
        self.add_message("user", user_message)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.message
        )
        # print(response)

        model_message = response.choices[0].message.content
        self.add_message("assistant", model_message)
        return model_message


bot = ChatBot()

if __name__ == '__main__':
    print("Starting")
    # print(bot.get_response("Opisz Comarch"))
    # ChatCompletion(id='chatcmpl-Bxv7W7sm1w2ZUiAy6jCsQp3t4TARg', choices=[
    #     Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(
    #         content='Comarch to międzynarodowa firma informatyczna, która specjalizuje się w dostarczaniu rozwiązań IT dla przedsiębiorstw z różnych branż. Firma została założona w 1993 roku przez prof. Janausz Filipiak, a jej główna siedziba znajduje się w Krakowie, Polsce.\n\nComarch oferuje kompleksowe oprogramowanie i usługi IT, takie jak systemy zarządzania relacjami z klientami (CRM), systemy zarządzania magazynem (WMS), systemy zarządzania łańcuchem dostaw (SCM), oprogramowanie do zarządzania zasobami ludzkimi (HR), rozwiązania do e-handlu, usługi chmurowe oraz wiele innych.\n\nFirma obsługuje klientów na całym świecie, a jej produkty i usługi są wykorzystywane przez przedsiębiorstwa z różnych sektorów, takich jak finanse, telekomunikacja, handel detaliczny, zdrowie, przemysł, energetyka, sektor publiczny i wiele innych.\n\nComarch jest uznawany za jednego z wiodących dostawców rozwiązań IT w Europie i na świecie, a jej innowacyjne podejście do technologii i silne zaangażowanie w rozwój produktów sprawiają, że firma jest ceniona przez klientów z całego świata.',
    #         refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))],
    #                created=1753620622, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier='default',
    #                system_fingerprint=None, usage=CompletionUsage(completion_tokens=360, prompt_tokens=11, total_tokens=371,
    #                                                               completion_tokens_details=CompletionTokensDetails(
    #                                                                   accepted_prediction_tokens=0, audio_tokens=0,
    #                                                                   reasoning_tokens=0, rejected_prediction_tokens=0),
    #                                                               prompt_tokens_details=PromptTokensDetails(audio_tokens=0,
    #                                                                                                         cached_tokens=0)))
    # None

    # print(bot.get_response("Opisz Comarch").choices[0].message.content)
    # Comarch został założony w 1993 roku w Krakowie i od tego czasu odniósł duży sukces, zdobywając szerokie uznanie klientów na całym świecie. Firma zatrudnia ponad 6 000 pracowników i ma biura w 30 krajach. Comarch jest znany z zaawansowanych technologicznie rozwiązań, dbałości o jakość produktów oraz profesjonalnego podejścia do klientów.
    #
    # Jednym z głównych celów Comarch jest stałe rozwijanie swoich produktów oraz pozyskiwanie nowych klientów na całym świecie. Firma stawia na innowacyjność, dbałość o jakość oraz dostosowanie swoich rozwiązań do indywidualnych potrzeb i oczekiwań klientów.
    #

    # bot.get_models()
    print(bot.get_response("Opisz Comarch"))
    print(bot.get_response("Kto jest jego włascicielem"))
