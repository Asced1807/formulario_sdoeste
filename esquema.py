from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class FormularioBase(BaseModel):
    nombre: str
    fecha_nacimiento: date
    sexo: str
    fecha_encuesta: date
    ubicacion: str
    tipo_usuario: str
    tiempo_residencia: str
    consumo: int
    comentarios_adicionales: Optional[str] = None
    frecuencia_apagones: str
    duracion_apagones: str
    horario_apagones: str
    comentarios_frecuencia: Optional[str] = None
    epoca_apagones: str
    condiciones_climaticas: List[str]
    relacion_apagones: List[str]
    facturacion: str
    cobro_apagones: str
    diferencias_facturacion: str
    compensaciones_apagones: str
    metodo_pago: str
    registro_horas: List[str]
    comentarios_facturacion: Optional[str] = None
    impacto_economico: str
    perdidas_economicas: str
    sistema_respaldo: str
    comentarios_impacto: Optional[str] = None
    notificaciones_apagones: str
    medio_notificaciones: str
    tiempo_respuesta: str
    comentarios_comunicacion: Optional[str] = None
    num_transformador: int
    estado_infraestructura: str
    observaciones_tecnicas: Optional[str] = None
    utilidad_sistema: str
    tiempo_alerta: str
    acciones_alerta: List[str]
    medio_alerta: List[str]
    info_alerta: List[str]
    funcionalidades: List[str]
    compartir_datos: str
    mejora_planificacion: str
    beneficios: List[str]
    confiabilidad_sistema: str
    participar_piloto: str
    interes_reportar: str


