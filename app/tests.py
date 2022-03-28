import json

from graphene_django.utils.testing import GraphQLTestCase

from swapi.schema import schema


class FirstTestCase(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_people_query(self):
        response = self.query(
            '''
            query{
              allPeople{
                edges{
                  node{
                    name
                  }
                }
              }
            }
            ''',
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allPeople']['edges']), 84)

    def test_people_mutation(self):
        # This validates the status code and if you get errors
        create_response = self.query(
            '''
                mutation addNewPeople{
                    createPeople(input:{name: "C-3PO", gender: "n/a", height: "167", mass: "80", hairColor: "n/a", eyeColor: "yellow", skinColor: "gold", birthYear: "112BBY", homeWorldId: 1}){
                        people{
                            id,
                            name,
                            gender,
                            height,
                            mass,
                            hairColor,
                            eyeColor,
                            skinColor,
                            birthYear
                            homeWorld{
                                name,
                            }
                        }
                    }
                }
            ''',
        )
        self.assertResponseNoErrors(create_response)

        add_content = json.loads(create_response.content)
        add_expected_result =  {'id': 'UGVvcGxlVHlwZTo4OQ==', 'name': 'C-3PO', 'gender': 'n/a',
                                  'height': '167', 'mass': '80', 'hairColor': 'n/a', 'eyeColor': 'yellow',
                                  'skinColor': 'gold', 'birthYear': '112BBY', 'homeWorld': {'name': 'Tatooine'}}
        self.assertEqual(add_content['data']['createPeople']['people'], add_expected_result)

        udpdate_response = self.query(
            '''
                mutation crearPersona{
                    createPeople(input:{id:"UGVvcGxlVHlwZToy", name:"C-3PO" ,mass:"80"}){
                        people{
                            id,
                            name,
                            gender,
                            height,
                            mass,
                            hairColor,
                            eyeColor,
                            skinColor,
                            birthYear
                            homeWorld{
                                name,
                            }
                        }
                    }
                }
            ''',
        )
        self.assertResponseNoErrors(udpdate_response)

        update_content = json.loads(udpdate_response.content)
        update_expected_result = {'id': 'UGVvcGxlVHlwZToy', 'name': 'C-3PO', 'gender': 'n/a',
                                  'height': '167', 'mass': '80', 'hairColor': 'n/a', 'eyeColor': 'yellow',
                                  'skinColor': 'gold', 'birthYear': '112BBY', 'homeWorld': {'name': 'Tatooine'}}
        self.assertEqual(update_content['data']['CreatePeople']['people'], update_expected_result)
