from strands import Agent, tool
from strands.models.ollama import OllamaModel
from dotenv import load_dotenv
import math 

load_dotenv()

# --- CONFIGURAÇÃO DO MODELO ---
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.1",
)

# --- A FERRAMENTA CIENTÍFICA ---
@tool
def math_tool(expression: str) -> str:
    try:
        print(f"🔧 TOOL CIENTÍFICA CHAMADA COM: {expression}")
        expression = expression.replace("√", "math.sqrt").replace("π", "math.pi").replace("^", "**")
        result = eval(expression, {"__builtins__": None}, {"math": math})
        return str(result)
    except Exception as e:
        return f"Erro: {str(e)}"

# --- O CÉREBRO VERSÁTIL ---
agent = Agent(
    model=ollama_model,
    tools=[math_tool],
    system_prompt="""
    Você é um Assistente de IA Inteligente e Amigável (fala Português do Brasil).

    SUA MISSÃO:
    1. CONHECIMENTO GERAL: Você responde sobre qualquer assunto (Geografia, História, Programação, etc) de forma direta e natural. Não precisa pedir desculpas se a pergunta não for de matemática.
    2. CÁLCULOS: Se (e somente se) o usuário pedir uma conta, você TEM que usar a ferramenta 'math_tool'.
    
    COMO USAR A MATEMÁTICA:
    - Você tem acesso à lib 'math' do Python.
    - Ex: "Seno de 90" -> Use "math.sin(math.radians(90))" na ferramenta.
    - Ex: "Raiz de 81" -> Use "math.sqrt(81)".
    
    Responda sempre de forma limpa e prestativa.
    """
)

def get_agent_response(user_message: str):
    print(f"🤖 Agente Pensando: {user_message}")
    return agent(user_message)