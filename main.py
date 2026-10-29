from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="API Inteligente de Solicitações",
    description="API para gerenciar solicitações de uma empresa.",
    version="1.0.0"
)

class Solicitacao(BaseModel):
    titulo: str
    descricao: str
    prioridade: str = "Normal"

solicitacoes = {}
proximo_id = 1

@app.get("/")
def inicio():
    return {"mensagem": "API funcionando!"}

@app.post("/solicitacoes")
def criar_solicitacao(solicitacao: Solicitacao):
    global proximo_id

    solicitacoes[proximo_id] = solicitacao
    resultado = {
        "id": proximo_id,
        **solicitacao.model_dump()
    }
    proximo_id += 1
    return resultado

@app.get("/solicitacoes")
def listar_solicitacoes():
    return [
        {"id": id, **item.model_dump()}
        for id, item in solicitacoes.items()
    ]

@app.get("/solicitacoes/{solicitacao_id}")
def consultar_solicitacao(solicitacao_id: int):
    item = solicitacoes.get(solicitacao_id)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Solicitação não encontrada"
        )

    return {"id": solicitacao_id, **item.model_dump()}

@app.delete("/solicitacoes/{solicitacao_id}")
def excluir_solicitacao(solicitacao_id: int):
    if solicitacao_id not in solicitacoes:
        raise HTTPException(
            status_code=404,
            detail="Solicitação não encontrada"
        )

    del solicitacoes[solicitacao_id]
    return {"mensagem": "Solicitação excluída"}