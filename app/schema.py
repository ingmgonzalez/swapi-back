import graphene

# from django.db.models import q
from django.db.models import Q
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from graphql_relay.node.node import from_global_id

from .models import Planet, People, Film, Director, Producer
from .mutations import CreatePlanet, CreatePeople
from .types import PlanetType, PeopleType, FilmType, DirectorType, ProducerType


class Query(graphene.ObjectType):
    # planets = graphene.List(PlanetType)
    planet = graphene.relay.Node.Field(PlanetType)
    all_planets = DjangoFilterConnectionField(PlanetType)

    people = graphene.relay.Node.Field(PeopleType)
    all_people = DjangoFilterConnectionField(PeopleType)

    film = graphene.relay.Node.Field(FilmType)
    all_films = DjangoFilterConnectionField(FilmType)

    director = graphene.relay.Node.Field(DirectorType)
    all_directors = DjangoFilterConnectionField(DirectorType)

    producer = graphene.relay.Node.Field(ProducerType)
    all_producers = DjangoFilterConnectionField(ProducerType)

class Mutation(graphene.ObjectType):
    create_planet = CreatePlanet.Field()
    create_people = CreatePeople.Field()


# schema = graphene.Schema(query=Query, mutation=Mutation)
