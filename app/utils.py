
def generic_model_mutation_process(model, data, id=None, commit=True):
    
    """
        Permite crear y actualizar registros basados en el modelos y el id que se le suministre.
        Parametros:
        * model: modelo de django.
        * data: Diccionario con los campos usados para crear o actualizar.
        * id: Parametro tipo Int para buscar el objeto o acyualizar.
        * commit: confirma si se guarda el objeto.
        * return: retorna una isntancia del modelo.
    
    """
    if id:
        print(id)
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        item = model(**data)

    if commit:
        item.save()

    return item
