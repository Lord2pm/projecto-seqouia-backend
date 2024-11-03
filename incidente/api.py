from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Incidente, TipoIncidente
from .schemas import IncidenteSchema, IncidenteCreateSchema, TipoIncidenteSchema

incidente_router = Router()


@incidente_router.get("", response={200: list[IncidenteSchema]})
def get_all_incidentes(request):
    return 200, Incidente.objects.all()


@incidente_router.get("{incidente_id}/", response={200: IncidenteSchema, 404: dict})
def get_incidente_by_id(request, incidente_id: int):
    incidente = get_object_or_404(Incidente, id=incidente_id)
    return 200, incidente


@incidente_router.post("", response={201: IncidenteSchema, 400: dict})
def create_incidente(request, data: IncidenteCreateSchema):
    try:
        tipo = get_object_or_404(TipoIncidente, id=data.id_tipo)
        incidente = Incidente.objects.create(
            titulo=data.titulo,
            descricao=data.descricao,
            localizacao=data.localizacao,
            tipo=tipo,
        )
        return 201, incidente
    except Exception as e:
        return 400, {"error": str(e)}


@incidente_router.put(
    "{incidente_id}/", response={200: IncidenteSchema, 404: dict, 400: dict}
)
def update_incidente(request, incidente_id: int, data: IncidenteCreateSchema):
    incidente = get_object_or_404(Incidente, id=incidente_id)

    for attr, value in data.model_dump().items():
        setattr(incidente, attr, value)

    try:
        incidente.save()
        return 200, incidente
    except Exception as e:
        return 400, {"error": str(e)}


@incidente_router.delete("{incidente_id}/", response={204: None, 404: dict})
def delete_incidente(request, incidente_id: int):
    incidente = get_object_or_404(Incidente, id=incidente_id)
    incidente.delete()
    return 204, None
