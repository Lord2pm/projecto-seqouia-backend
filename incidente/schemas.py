from datetime import datetime

from ninja import ModelSchema, Schema

from .models import Incidente, TipoIncidente


class IncidenteSchema(ModelSchema):
    class Meta:
        model = Incidente
        fields = (
            "id",
            "titulo",
            "descricao",
            "status",
            "tipo",
            "localizacao",
            "created_at",
            "updated_at",
        )


class IncidenteCreateSchema(Schema):
    titulo: str
    descricao: str
    localizacao: str
    id_tipo: int


class TipoIncidenteSchema(ModelSchema):
    class Meta:
        model = TipoIncidente
        fields = (
            "id",
            "nome",
            "descricao",
            "created_at",
            "updated_at",
        )
