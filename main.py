from flask import Flask, jsonify, request

app = Flask(__name__)

professores = [

]
turmas = [

]
alunos = [

]

# rotas prof
@app.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify(professores)

@app.route('/professores/<int:id_professor>', methods=['GET'])
def obter_professor(id_professor):
    professor = next((p for p in professores if p["id"] == id_professor), None)
    return jsonify(professor) if professor else (jsonify({"erro": "Professor não encontrado"}), 404)

@app.route('/professores', methods=['POST'])
def criar_professor():
    dados = request.json
    novo_professor = {
        "id": len(professores) + 1,
        "nome": dados["nome"],
        "disciplina": dados["disciplina"]
    }
    professores.append(novo_professor)
    return jsonify(novo_professor), 201

@app.route('/professores/<int:id_professor>', methods=['PUT'])
def atualizar_professor(id_professor):
    professor = next((p for p in professores if p["id"] == id_professor), None)
    if not professor:
        return jsonify({"erro": "Professor não encontrado"}), 404

    dados = request.json
    professor.update({
        "nome": dados.get("nome", professor["nome"]),
        "disciplina": dados.get("disciplina", professor["disciplina"])
    })
    return jsonify(professor)

@app.route('/professores/<int:id_professor>', methods=['DELETE'])
def excluir_professor(id_professor):
    global professores
    professores = [p for p in professores if p["id"] != id_professor]
    return jsonify({"mensagem": "Professor removido"}), 200

#turmas
@app.route('/turmas', methods=['GET'])
def listar_turmas():
    return jsonify(turmas)

@app.route('/turmas/<int:id_turma>', methods=['GET'])
def obter_turma(id_turma):
    turma = next((t for t in turmas if t["id"] == id_turma), None)
    return jsonify(turma) if turma else (jsonify({"erro": "Turma não encontrada"}), 404)

@app.route('/turmas', methods=['POST'])
def criar_turma():
    dados = request.json
    nova_turma = {
        "id": len(turmas) + 1,
        "nome": dados["nome"],
        "turno": dados["turno"]
    }
    turmas.append(nova_turma)
    return jsonify(nova_turma), 201

@app.route('/turmas/<int:id_turma>', methods=['PUT'])
def atualizar_turma(id_turma):
    turma = next((t for t in turmas if t["id"] == id_turma), None)
    if not turma:
        return jsonify({"erro": "Turma não encontrada"}), 404

    dados = request.json
    turma.update({
        "nome": dados.get("nome", turma["nome"]),
        "turno": dados.get("turno", turma["turno"])
    })
    return jsonify(turma)

@app.route('/turmas/<int:id_turma>', methods=['DELETE'])
def excluir_turma(id_turma):
    global turmas
    turmas = [t for t in turmas if t["id"] != id_turma]
    return jsonify({"mensagem": "Turma removida"}), 200

#alunos
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify(alunos)

@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def obter_aluno(id_aluno):
    aluno = next((a for a in alunos if a["id"] == id_aluno), None)
    return jsonify(aluno) if aluno else (jsonify({"erro": "Aluno não encontrado"}), 404)

@app.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.json
    novo_aluno = {
        "id": len(alunos) + 1,
        "nome": dados["nome"],
        "turma_id": dados["turma_id"]
    }
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualizar_aluno(id_aluno):
    aluno = next((a for a in alunos if a["id"] == id_aluno), None)
    if not aluno:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    dados = request.json
    aluno.update({
        "nome": dados.get("nome", aluno["nome"]),
        "turma_id": dados.get("turma_id", aluno["turma_id"])
    })
    return jsonify(aluno)

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def excluir_aluno(id_aluno):
    global alunos
    alunos = [a for a in alunos if a["id"] != id_aluno]
    return jsonify({"mensagem": "Aluno removido"}), 200

#roda essa api logo
if __name__ == '__main__':
    app.run(debug=True)
