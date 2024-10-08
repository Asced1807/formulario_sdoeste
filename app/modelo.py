from sqlalchemy import Column, Integer, String, Date, Text, ARRAY, DateTime, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session 
from sqlalchemy.sql import func
from clave import DATABASE # AQUI ESTA MI CONEXION A POSTGRESQL CON CLAVE Y TODO NO VISIBLE 


engine = create_engine(DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Formulario(Base):
    __tablename__ = 'formulario'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Información personal y del encuestado
    nombre = Column(String, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    sexo = Column(String, nullable=False)
    fecha_encuesta = Column(Date, nullable=False)
    ubicacion = Column(String, nullable=False)
    tipo_usuario = Column(String, nullable=False)
    tiempo_residencia = Column(String, nullable=False)
    consumo = Column(Integer, nullable=False)
    comentarios_adicionales = Column(Text, nullable=True)

    # Frecuencia y duración de los apagones
    frecuencia_apagones = Column(String, nullable=False)
    duracion_apagones = Column(String, nullable=False)
    horario_apagones = Column(String, nullable=False)
    comentarios_frecuencia = Column(Text, nullable=True)
    epoca_apagones = Column(String, nullable=False)
    condiciones_climaticas = Column(ARRAY(String), nullable=True)
    relacion_apagones = Column(ARRAY(String), nullable=True)

    # Facturación y consumo
    facturacion = Column(String, nullable=False)
    cobro_apagones = Column(String, nullable=False)
    diferencias_facturacion = Column(String, nullable=False)
    compensaciones_apagones = Column(String, nullable=False)
    metodo_pago = Column(String, nullable=False)
    registro_horas = Column(ARRAY(String), nullable=True)
    comentarios_facturacion = Column(Text, nullable=True)

    # Impacto y consecuencias
    impacto_economico = Column(String, nullable=False)
    perdidas_economicas = Column(String, nullable=False)
    sistema_respaldo = Column(String, nullable=False)
    comentarios_impacto = Column(Text, nullable=True)

    # Comunicación y respuesta
    notificaciones_apagones = Column(String, nullable=False)
    medio_notificaciones = Column(String, nullable=False)
    tiempo_respuesta = Column(String, nullable=False)
    comentarios_comunicacion = Column(Text, nullable=True)

    # Datos técnicos
    num_transformador = Column(Integer, nullable=False)
    estado_infraestructura = Column(String, nullable=False)
    observaciones_tecnicas = Column(Text, nullable=True)

    # Sistema predictivo de apagones
    utilidad_sistema = Column(String, nullable=False)
    tiempo_alerta = Column(String, nullable=False)
    acciones_alerta = Column(ARRAY(String), nullable=True)
    medio_alerta = Column(ARRAY(String), nullable=True)
    info_alerta = Column(ARRAY(String), nullable=True)
    funcionalidades = Column(ARRAY(String), nullable=True)
    compartir_datos = Column(String, nullable=False)
    mejora_planificacion = Column(String, nullable=False)
    beneficios = Column(ARRAY(String), nullable=True)
    confiabilidad_sistema = Column(String, nullable=False)
    participar_piloto = Column(String, nullable=False)
    interes_reportar = Column(String, nullable=False)

    
    
# Crear las tablas en la base de datos                                                                                       
Base.metadata.create_all(engine) # solo debe ser ejecuctado una sola vez nada mas porque si esta activo sobreescribira la base de datos   
