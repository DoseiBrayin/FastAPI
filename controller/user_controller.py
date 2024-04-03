# controllers.py
from models import user_model
def get_item(item_id: int) -> user_model.Item:
    # Aquí es donde normalmente interactuarías con la base de datos.
    # Como este es solo un ejemplo, vamos a devolver un item estático.
    return user_model.Item(name="Foo", description="A very nice Item", price=35.5)

def get_items() -> list[user_model.Item]:
    # Aquí es donde normalmente interactuarías con la base de datos.
    # Como este es solo un ejemplo, vamos a devolver una lista de items estáticos.
    return [
        user_model.Item(name="Foo", description="The prettiest Foo", price=50.2),
        user_model.Item(name="Bar", description="The most protective Bar", price=62)
    ]

def create_item(item: user_model.Item) -> user_model.Item:
    # Aquí es donde normalmente interactuarías con la base de datos.
    # Como este es solo un ejemplo, vamos a devolver el item que hemos creado.
    return item