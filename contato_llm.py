from openai import OpenAI

client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def recebe_linhas_retorna_jason(linha):
    resposta_llm = client_openai.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[{
            "role": "system",
            "content": "Você é um assistente de IA prestativo, porem direto e objetivo, sem dar informações irrelevantes"
        },{
            "role": "user",
            "content": f"""
                Você é um analista de dados.

                Analise a lista de reviews e retorne um JSON válido.

                Cada item deve possuir:
                - "Usuario"
                - "Resenha Original"
                - "Resenha em Português Brasileiro"
                - "Avaliação"

                A avaliação deve ser:
                - "Positivo"
                - "Negativo"
                - "Neutro"

                IMPORTANTE:
                - Retorne APENAS o JSON
                - Não escreva explicações
                - Não use ```json
                - Use aspas duplas
                - O retorno deve ser uma LISTA JSON
                -Retorne JSON válido em uma única linha.
                -Escape caracteres especiais corretamente.
                -Não use quebras de linha dentro dos valores.
                - Nunca escape aspas dentro dos valores de string
                - Use apenas aspas duplas para delimitar chaves e valores
                - Não inclua barras invertidas nos valores

               
                Exemplo:

                [
                    {{
                        "Usuario": "Usuario1",
                        "Resenha Original": "Texto original",
                        "Resenha em Português Brasileiro": "Texto traduzido",
                        "Avaliação": "Positivo"
                    }}
                ]
                
                REGRA IMPORTANTE: você deve retornar apenas o JSON, sem nenhum outro texto além do JSON.
                Lista de reviews:
                {linha}
                """
        }],
        temperature=0.0
    )
    
    resposta = resposta_llm.choices[0].message.content.replace("```json","").replace("```", "")
    print(resposta)
    return resposta