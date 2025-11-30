# 🤖 DreamSquad AI Agent

> **Status:** Concluído 🚀 | **Stack:** FastAPI + Streamlit + Strands Agents + Llama 3.1

Uma aplicação Fullstack de IA Agêntica capaz de realizar raciocínio lógico e cálculos matemáticos complexos (Científicos), orquestrada localmente via Ollama.

O projeto demonstra a integração entre uma API robusta (Backend), um Agente Autônomo com uso de ferramentas (Function Calling) e uma Interface Moderna (Frontend) com design Glassmorphism.

---

## ✨ Funcionalidades Principais

### 🧠 Inteligência Agêntica (Backend)
- **Raciocínio Autônomo:** O agente decide sozinho quando responder com texto ou quando invocar a ferramenta matemática.
- **Calculadora Científica:** Integração completa com a biblioteca `math` do Python. Suporta trigonometria (`sin`, `cos`), logaritmos (`log10`), fatoriais e constantes (`pi`, `e`).
- **Parser Robusto (Blindagem):** Sistema avançado de tratamento de strings que limpa alucinações de JSON do modelo Llama 3.1, garantindo que o usuário receba apenas a resposta limpa.
- **Segurança:** Sanitização de inputs matemáticos para execução segura.

### 🎨 Experiência do Usuário (Frontend)
- **Interface Streamlit Customizada:** Design "Glassmorphism" (efeito de vidro) com CSS injetado.
- **Feedback Visual:** Efeito de "digitação" (streaming simulado) e indicadores de status ("Processando...").
- **Histórico de Chat:** Sessão persistente durante a conversa.

---

## 🛠️ Tech Stack

- **Linguagem:** Python 3.10+
- **LLM Engine:** [Ollama](https://ollama.com/) (Modelo: `llama3.1`)
- **Orquestração:** [Strands Agents SDK](https://strandsagents.com/)
- **API:** FastAPI & Pydantic
- **Frontend:** Streamlit
- **Testes:** Pytest & Httpx

---

## 🚀 Como Rodar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o **Ollama** instalado. Este projeto requer o modelo `llama3.1` devido ao suporte nativo a *Tool Use*.

```bash
# No seu terminal/cmd:
ollama pull llama3.1
````

### 2\. Instalação

Clone o repositório e instale as dependências:

```bash
# Clone o projeto
git clone https://github.com/allan-felipe23/dreamsquad-ai-agent.git
cd dreamsquad-ai-agent

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente (Windows)
.\venv\Scripts\activate
# Ative o ambiente (Linux/Mac)
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 3\. Execução

Você precisará de **dois terminais** abertos:

**Terminal 1: Backend (API)**

```bash
uvicorn main:app --reload
# A API iniciará em [http://127.0.0.1:8000](http://127.0.0.1:8000)
```

**Terminal 2: Frontend (UI)**

```bash
streamlit run frontend.py
# O navegador abrirá automaticamente em http://localhost:8501
```

-----

## 🧪 Testes e Validação

O projeto inclui testes automatizados para garantir a estabilidade da API.

```bash
# Rodar suite de testes
pytest
```

-----

## 📂 Estrutura do Projeto

  - **`agent.py`**: O "Cérebro". Configura o modelo Llama 3.1, define a Tool (`math_tool`) com acesso à lib `math` e estabelece o System Prompt.
  - **`main.py`**: O "Controlador". API FastAPI que recebe requisições, chama o agente e aplica Regex/Parsers para limpar a resposta técnica do LLM.
  - **`frontend.py`**: A "Cara". Interface Streamlit com injeção de CSS para o tema visual e lógica de chat.
  - **`test_main.py`**: Testes unitários com Mocking para validar a API sem depender do modelo rodando.

-----

## 💡 Destaques Técnicos

1.  **Tratamento de Output do Llama 3.1:** O modelo `llama3.1` frequentemente mistura JSON de ferramentas com texto natural. Implementei um parser híbrido no `main.py` que varre a resposta, extrai o conteúdo útil (`toolResult` ou texto) e remove artefatos de JSON usando Regex.
2.  **Extensibilidade Matemática:** A Tool não é apenas um `eval()` simples. Ela expõe a biblioteca `math` de forma controlada, permitindo cálculos como `math.sqrt(144)` ou `math.sin(30)` que modelos de linguagem puros costumam errar.
3.  **Visual Polido:** Fugi do padrão cinza do Streamlit implementando um tema vibrante e moderno via CSS, demonstrando preocupação com o produto final entregue ao usuário.

-----

### 📸 Experiência do Usuário

<img width="1916" height="969" alt="Captura de tela 2025-11-30 090402" src="https://github.com/user-attachments/assets/b9b8816c-bbd0-40a7-9595-c4f6b9337fd3" />

-----

#### 💻 Desenvolvido por **Allan Borges** para o desafio **DreamSquad**. [Meu LinkedIn](https://www.linkedin.com/in/alan-borges23/)

