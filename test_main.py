from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

# Cria um cliente "falso" que simula requisições sem precisar subir o servidor
client = TestClient(app)

def test_chat_endpoint_sucesso():
    """
    Testa se o endpoint /chat responde 200 OK e o JSON correto
    quando tudo vai bem.
    """
    # 'Mockamos' a função get_agent_response para não chamar o Ollama de verdade
    # Isso faz o teste rodar em milissegundos e isola a API do modelo.
    fake_response = "Esta é uma resposta simulada para teste."
    
    with patch('main.get_agent_response') as mock_agent:
        mock_agent.return_value = fake_response
        
        # O payload que vamos enviar
        payload = {"message": "Olá, teste!"}
        
        # Faz a requisição POST simulada
        response = client.post("/chat", json=payload)
        
        # 1. O status code deve ser 200 (Sucesso)
        assert response.status_code == 200
        
        # 2. A resposta deve ser o JSON esperado
        assert response.json() == {"response": fake_response}

def test_chat_endpoint_validacao():
    """
    Testa se a API rejeita requisições inválidas (ex: JSON vazio).
    Isso testa se o Pydantic está funcionando.
    """
    # Enviamos um JSON vazio, faltando o campo 'message'
    response = client.post("/chat", json={})
    
    # Deve retornar erro 422 (Unprocessable Entity) do FastAPI
    assert response.status_code == 422