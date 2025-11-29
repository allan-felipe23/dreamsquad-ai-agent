from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import get_agent_response
import re

app = FastAPI(title="DreamSquad AI Agent API")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        print(f"📩 Recebendo: {request.message}")
        raw_response = get_agent_response(request.message)
        
        final_text = ""

        try:
            # Normaliza para lista
            if hasattr(raw_response, 'message') and hasattr(raw_response.message, 'content'):
                content_list = raw_response.message.content
            elif isinstance(raw_response, dict):
                content_list = raw_response.get('message', {}).get('content', [])
            else:
                content_list = []

            # Varre os itens
            for item in content_list:
                # Se for objeto, vira dict
                if not isinstance(item, dict) and hasattr(item, '__dict__'):
                    item = item.__dict__
                
                # Pega texto normal
                if 'text' in item and item['text']:
                    final_text += item['text'] + "\n"
                
                # Pega resultado de ferramenta (se houver)
                if 'toolResult' in item:
                    tr_content = item['toolResult'].get('content', [])
                    for sub in tr_content:
                        if 'text' in sub:
                            final_text += f"\n✅ Resultado do cálculo: {sub['text']}\n"

            # Fallback
            if not final_text:
                final_text = str(raw_response)

        except Exception as e:
            print(f"⚠️ Erro Parser: {e}")
            final_text = str(raw_response)

        # Aqui removemos qualquer "sujeira" de JSON que o modelo tenha deixado escapar
        # O padrão procura por: {"name": "alguma_coisa", ... }
        
        clean_text = re.sub(r'\{"name":\s*".*?",\s*"parameters":\s*\{.*?\}\}', '', final_text, flags=re.DOTALL)
        
        # Remove espaços vazios extras que podem ter sobrado
        clean_text = clean_text.strip()

        return {"response": clean_text}
    
    except Exception as e:
        print(f"🔥 Erro Crítico: {e}")
        raise HTTPException(status_code=500, detail=str(e))