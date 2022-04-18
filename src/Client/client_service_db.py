from .client_model import Client


def create(client_name, client_description, creator_id):
    # CREATE NEW CLIENT ASSIGN NAME AND CREATOR ID & RETURN
    new_client = Client(name=client_name, description=client_description,
                        creator_id=creator_id)
    new_client.save_db()
    return new_client


def update(client_id, client_name, client_description):
    # GET CLIENT BY ID AND UPDATE & RETURN
    client = Client.query.filter_by(id=client_id).first()
    client.name = client_name
    client.description = client_description
    client.update_db()
    return client


def delete(client_id, creator_id):
    # GET CLIENT BY ID AND CREATOR ID. DELETE AND RETURN
    client = Client.query.filter_by(id=client_id, creator_id=creator_id).first()
    client.delete_db()
    return client


def get_by_id(client_id):
    # GET CLIENT BY ID AND return
    client = Client.query.filter_by(id=client_id).first()
    return client


def get_by_name_creator_id(client_name, creator_id):
    # GET CLIENT BY NAME AND CREATOR ID & RETURN
    client = Client.query.filter_by(name=client_name, creator_id=creator_id).first()
    return client


def get_by_id_creator_id(client_id, creator_id):
    # GET CLIENT BY ID AND CREATOR ID & RETURN
    client = Client.query.filter_by(id=client_id, creator_id=creator_id).first()
    return client


def get_all_ids_by_creator_id(creator_id):
    # GET ALL CLIENT, ITERATE OVER ONE AT A TIME AND INSERT THE CLIENT OBJECT INTO THE ARRAY
    client_ids = []
    for client in Client.query.filter_by(creator_id=creator_id).all():
        client_ids.append(client.id)
    return client_ids


def get_by_creator_id_name_exclude_id(client_id, creator_id, name):
    # GET CLIENT BY CREATOR ID, NAME, AND EXCLUDE CLIENT ID
    client = Client.query.filter(Client.id != client_id, creator_id == creator_id, Client.name == name).first()
    return client


def get_first() -> Client:
    return Client.query.first()
