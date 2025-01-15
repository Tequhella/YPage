import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Book

# Définir le type GraphQL pour le modèle Book
class BookType(SQLAlchemyObjectType):
    class Meta:
        model = Book
        interfaces = (graphene.relay.Node,)

# Requêtes (queries)
class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(self, info):
        # Récupérer tous les livres
        query = Book.query.all()
        return query

# Mutation (exemple : ajout d'un livre)
class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        genre = graphene.String(required=True)
        popularity = graphene.Int()

    book = graphene.Field(lambda: BookType)

    def mutate(self, info, title, genre, popularity=0):
        new_book = Book(title=title, genre=genre, popularity=popularity)
        db.session.add(new_book)
        db.session.commit()
        return CreateBook(book=new_book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()

# Schéma GraphQL
schema = graphene.Schema(query=Query, mutation=Mutation)
