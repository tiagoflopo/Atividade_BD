from fastapi import FastAPI

from http import HTTPStatus

from atividade2_bd1.schema import UserID, UserInfos, UserList, UserPublic


app = FastAPI( #Descrição na documentação
    title='Atividade 2 BD1 - Tiago Ferreira Lopo',
    description=(
        'Aqui temos 3 funções, uma para realizar um cadastro simples de usuário. '
        'Podemos realizar a leitura de todos os usuários do BD,'
        'e também podemos realizar a consulta de um usuário específico através do seu ID.'
    ),
)

database = []

@app.post( #Criar o usuário
    '/criar_usuario/',
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
    tags=['Cadastro de Usuário'],
)
def create_user(user: UserInfos):
    db_user = UserID(
        id=len(database) + 1,
        nome = user.nome,
        cpf = user.cpf,
        data_nascimento = user.data_nascimento,
    )

    database.append(db_user)

    return db_user

@app.get( #Ler a lista dos usuários
    '/ler_usuarios/',
    status_code=HTTPStatus.OK,
    response_model=UserList,
    tags=['Ler usuário'],
)
def read_users():
    return {'users': database}


@app.get( #Ler um usuário pelo ID
    '/ler_usuario_id/',
    status_code=HTTPStatus.OK,
    response_model=UserPublic,
    tags=['Ler usuário'],
)
def read_user(user_id: int):
    if user_id > 0 and user_id <= len(database):
        db_user = database[user_id - 1]

        return db_user
    else: #Retornar erro caso o usuário n seja encontrado
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )