
#url campaing

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_campaing/', views.create_campaing, name="create_campaing"),
    url(r'^creado/', views.creado, name="creado"),
    url(r'^ver_colaboradores/', views.ver_colaboradores, name="ver_colaboradores"),



    #home campaing
	url(r'^home/', views.home, name="home"),

	#
	url(r'^buscar_paciente/', views.buscar_paciente, name="buscar_paciente"),


	
	
	url(r'^formulario_inscripcion/', views.formulario_inscripcion, name="formulario_inscripcion"),


	
	url(r'^pre_inscribirse/', views.pre_inscribirse, name="pre_inscribirse"),
	

	#aca esta para buscar preinscriptos??? y despues ir a la ventana formulario inscripcion??
	url(r'^inscribir_paciente_pre/', views.inscribir_paciente_pre, name="inscribir_paciente_pre"),
	
	url(r'^alta_paciente/([0-9]+)$', views.alta_paciente, name="alta_paciente"),



	url(r'^formulario_inscripcion/', views.formulario_inscripcion, name="formulario_inscripcion"),




    url(r'^ver_campanas/', views.ver_campanas, name="ver_campanas"),


	url(r'^home_admin/', views.home_admin, name="home_admin"),    

]
