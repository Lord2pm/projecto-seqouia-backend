from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from incidente.api import incidente_router

api = NinjaAPI(
    title="API para Registro e Gestão de Incidentes",
    description="Sistema de gestão de ocorrências de incidentes do Projeto SEQUOIA. O objetivo é permitir que o sistema funcione de forma modular, com back-end e front-end independentes, facilitando futuras integrações e escalabilidade.",
)

api.add_router("incidentes/", incidente_router)

urlpatterns = [path("admin/", admin.site.urls), path("api/v1/", api.urls)]
