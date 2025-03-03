import random
intentos_restantes=0
def obtener_palabra_aleatoria(dificultad):
    palabras = {
        "facil": (
            "Sam", "James", "Ellie_Williams", "Bill", "Isaac_Dixon", "Sarah_Miller",
            "Abby_Anderson", "Manny_Alvarez", "Robert", "Dina", "Lev", "Tommy_Miller",
            "Jesse", "Marlene", "David", "Owen_Moore", "Henry", "Tess_Servopoulos",
            "Emily", "Frank", "Nora_Harris", "Yara", "Joel_Miller", "Maria"
        ),
        "medio": (
            "Austin", "Texas", "Zona_de_Cuarentena", "Boston", "Lincoln",
            "Massachusetts", "Pittsburgh", "Pennsylvania", "Wyoming",
            "Universidad_de_Eastern_Colorado", "Colorado", "Lakeside_Resort",
            "Salt_Lake_City", "Jackson_Wyoming", "Seattle", "Seraphites_Island",
            "Estadio_de_los_WLF", "Acuarios_de_Seattle", "Santa_Barbara",
            "California", "Museo_de_ciencias_de_Jackson", "Hospital_de_Salt_Lake_City"
        ),
        "dificil": (
            "Supervivencia", "Amor", "Conexión_humana", "Pérdida", "Duelo", "Venganza",
            "Consecuencias","Redención", "Perdón", "Moralidad_ambigua", "Identidad", 
            "Propósito", "Aislamiento", "Comunidad" "Inocencia", "Pérdida", "Esperanza", 
            "Desesperación", "Prólogo", "Las_afueras", "El_pueblo_dde_Bill", "Los_suburbios",
            "La_presa_de_Tommy", "La_universidad", "La_estación_de_autobuses",
            "El_laboratorio_de_las_luciérnagas", "Alegría", "Apostar", "Alargar", "Ajusticiar", 
            "Acechar", "Atardecer", "Anochecer", "Ametralladora", "Árbol", "Ambigua", "Anarquía", 
            "Arboles", "Animal", "Arrogancia", "Anticuado", "Antiguo", "Antigua", "Amargado", 
            "Apocalíptico", "Atrocidad", "Arrinconado", "Agonía", "Asedio", "Azote", "Abismo",
            "Abyecto", "Abandonado", "Abandonar", "Auge", "Amenaza", "Arco", "Armagedón", 
            "Ambición", "Atormentar", "Asombro", "Asolación", "Afanoso", "Alineación", "Acribillado",
            "Aterrorizar", "Aterrorizado", "Acribillar", "Armas", "Aislamiento", "Aniquilación", 
            "Atestiguar", "Averiguar", "Aceptación", "Asimilar", "Arrebato", "Analizando", "Analizar", 
            "Angustia", "Auto", "Astucia", "Becerros", "Bosque", "Balas", "Bueno", "Bate", 
            "Clavos", "Base", "Bases", "Bala", "Balacera", "Bobo", "Blanco", "Barco", 
            "Biodiversidad", "Botella", "Batería", "Baterías", "Bigote", "Batalla", "Baldío", 
            "Blasfemia", "Berserker", "Bilis", "Bomba", "Barba", "Caos", "Camisa", "Cataclismo", 
            "Cementerio", "Cementerios", "Cenizas", "Calamidad", "Cuerda", "Clanes", "Campo", 
            "Concentración", "Calidad", "Chasqueador", "Condena", "Caníbal", "Cuchilla", "Colmena", 
            "Cubierto", "Combate", "Colapsado", "Control", "Cerebral", "Cerebrales", "Conexión", 
            "Conectado", "Colapsados", "Colapsadas", "Castigo", "Ciencia", "Carencia", "Costumbre", 
            "Comercio", "Cuestión", "Cuervo", "Cepillo", "Cocodrilo", "Cuestionamiento", "Canciones", 
            "Cristal", "Cuchillo", "Crecer", "Cero", "Conocimiento", "Carajo", "Certero", "Cazar", 
            "Cazador", "Cerrado", "Cerrar", "Cartera", "Cerdo", "Contagio", "Debilidad", "Dualidad", 
            "Desestimar", "Derrota", "Decepción", "Desilusión", "Desolación", "Deshecho", "Derruido", 
            "Delirio", "Dueño", "Dueños", "Desesperado", "Dosificado", "Densificado", "Dócil", "Dañino", 
            "Drama", "Deuda", "Dificultad", "Descubrimiento", "Destructivo", "Destrucción", 
            "Desintegración", "Determinación", "Demolición", "Destreza", "Delicado", "Dedo", 
            "Derrumbado", "Dedos", "Derrumbe", "Dolor", "Despojos", "Destinado", "Expectativa", 
            "Esperanza", "Estudio", "Espora", "Esporas", "Extinción", "Enfermedad", "Esencia", 
            "Efectividad", "Esclavitud", "Expectativas", "Elocuencia", "Engendro", "Ejecutor", 
            "Estructura", "Engaño", "Epidemia", "Enigmático", "Esclavo", "Estricto", "Empatía", "Épico", 
            "Equidad", "Errores", "Estruendo", "Ética", "Evitar", "Evocar", "Estupefacto", 
            "Escopeta", "Escombros", "Experiencia", "Ecos", "Enojo", "Enlazado", "Entendimiento", 
            "Evaluar", "Envió", "Eventual", "Eternidad", "Evitable", "Estima", "Extremo", "Exterminio", 
            "Exilio", "Enojado", "Enojada", "Espanto", "Estadio", "Estadios", "Fuerza", "Fatalidad", 
            "Fatalismo", "Fase", "Fases", "Ferocidad", "Fe", "Fuego", "Familiar", "Familia", "Futuro", 
            "Flagelo", "Fascinación", "Fluidos", "Fundar", "Fundación", "Franqueza", "Fraternidad", 
            "Fractura", "Fracaso", "Felicidad", "Francotirador", "Fragmentación", "Forajido", "Falange", 
            "Falanges", "Funesto", "Flecha", "Frutífero", "Fascinación", "Fallo", "Fétido", "Férreo", 
            "Fabricante", "Fuego", "Falta", "Fatalismo", "Filo", "Fin", "Fuga", "Fortalecer", "Fosa", 
            "Fango", "Feral", "Féretro", "Funesto", "Formar", "Ganar", "Granja", "Guerra", "Genocidio", 
            "Grieta", "Gas", "Gris", "Grito", "Golpe", "Gusano", "Gusanos", "Guerreo", "Guerreros", 
            "Genio", "Gozo", "Genética", "Gen", "Granada", "Ganancia", "Gestionar", "Gusto", "Golpear", 
            "Gorra", "Gozar", "Género", "Gentileza", "Guardia", "Guarida", "Guitarra", "Hipocresía", 
            "Hilarante", "Historia", "Histórico", "Hibrido", "Holocausto", "Hoyo", "Hambre", 
            "Herencia", "Huésped", "Honor", "Humanidad", "Humildad", "Hijo", "Hija", "Hijos", "Horror", 
            "Horda", "Humor", "Humo", "Hierro", "Horroroso", "Hostigamiento", "Húmedo", "Humedales", 
            "Hábitat", "Habitar", "Habitable", "Habitación", "Habilidad", "Habilidoso", "Hermandad", 
            "Hermoso", "Humano", "Hueso", "Huesos", "Hongo", "Hongos", "Hostilidad", "Hacha", 
            "Identidad", "Ingenuidad", "Idea", "Infantil", "Infantiles", "Inútil", "Inutilidad", 
            "Inmundo", "Idiota", "Iluso", "Inmutable", "Incrédulo", "Incredibilidad", "Inocencia", 
            "Inocente", "Imbécil", "Invencible", "Intratable", "Iracundo", "Ira", "Irrompible", 
            "Increíble", "Intocable", "Intratable", "Irreverente", "Inmoral", "Ilegal", "Imparcial", 
            "Irracional", "Inteligente", "Inusual", "Ignífugo", "Inicial", "Insípido", "Imaginativo", 
            "Inmortal", "Infierno", "Infestados", "Infestado", "Infortunio", "Inquieto", "Irreal", 
            "Ilusión", "Ilusionado", "Improvisado", "Ilusión", "Infectados", "Infección", 
            "Inevitabilidad", "Insania", "Intemperie", "Impotencia", "Isla", "Ídolo", "Iglesia", 
            "Imitador", "Intenso", "Infiltración", "Intensidad", "Inmundicia", "Inframundo", 
            "Imitadora", "Incendio", "Imaginación", "Juego", "Juegos", "Jactarse", "Joya", "Joyas", 
            "Jirafa", "Juicio", "Jinete", "Jauría", "Jerarquía", "Jornada", "Jaula", "Jadeo", "Jubileo", 
            "Jeringa", "Jugo", "Jirón", "Jabalí", "Justicia", "Juguete", "Karma", "Kamikaze", "Kevlar", 
            "Levantar", "Levantarse", "Latente", "Linterna", "Lupa", "Lore", "Luto", "Lamento", "Lobo", 
            "Lobos", "Manada", "Legión", "Límite", "Letargo", "Lanza", "Localizar", "Latas", "Lata", 
            "Lamentar", "Lamentable", "Limitado", "Lento", "Luz", "Lazo", "Luciérnaga", "Llenos", 
            "Lucero", "Lamer", "Lápida", "Lápidas", "Libertad", "Libertinaje", "Lluvia", "Laberinto", 
            "Lucirse", "Llamas", "Literal", "Mano", "Madre", "Mentira", "Museo", "Mentiras", 
            "Metralleta", "Mentiroso", "Melodía", "Madrugada", "Manual", "Martirio", "Maldita", 
            "Mutación", "Mentirosa", "Metal", "Misiles", "Militares", "Miseria", "Madrugada", 
            "Místico", "Misterioso", "Machete", "Malvado", "Mal", "Malo", "Malagradecido", "Mapa", 
            "Movimiento", "Montón", "Miramiento", "Malicioso", "Maliciosa", "Malicia", "Mayor", 
            "Menor", "Muerto", "Muerte", "Muertos", "Motor", "Mundo", "Mochila", "Mártir", "Marasmo", 
            "Miasma", "Megalópolis", "Maquinaria", "Moribundo", "Moribundos", "Mecer", "Monstruo", 
            "Miedo", "Memoria", "Muela", "Maligno", "Matar", "Maleta", "Mortalidad", "Masacre", 
            "Malgenio", "Munición", "Minucioso", "Niño", "Nosotros", "Navaja", "Niña", "Negro", 
            "Nocivo", "Normal", "Normalidad", "Negación", "Necesidad", "Necesidades", "Notificar", 
            "Necesitar", "Nadar", "Natación", "Nada", "Notar", "Natalidad", "Nacimiento", "Noticia", 
            "Necesario", "Nulidad", "Nepotismo", "Nuevo", "Nombre", "Novedad", "Noche", "Nocturno", 
            "Niebla", "Necrosis", "Náufrago", "Nómada", "Nómadas", "Némesis", "Necrópolis", 
            "Nutriente", "Nido", "Nostalgia", "Nexo", "Opacidad", "Opacado", "Orientado", "Orientación", 
            "Obligación", "Onírico", "Oscuridad", "Odio", "Olvido", "Ocaso", "Oficio", "Orden", "Ojo", 
            "Ojos", "Oasis", "Organizado", "Oso", "Osos", "Organización", "Organizar", "Orgánico", 
            "Orgullo", "Operar", "Obligar", "Obstrucción", "Operación", "Oportunidad", "Opresión", 
            "Orfandad", "Oleada", "Oleadas", "Orgulloso", "Orgullosa", "Oxidados", "Oxidado", "Oxidación", 
            "Oscilar", "Otros", "Pasado", "Penitencia", "Penumbra", "Pena", "Plantear", "Presente", "Posible", 
            "Pagar", "Puesto", "Puente", "Puentes", "Pandemia", "Puerto", "País", "Países", "Parque", 
            "Palabra", "Penumbra", "Palabras", "Parásitos", "Páramo", "Padecimiento", "Paranoia", "Plantas", 
            "Población", "Perro", "Perros", "Presentimiento", "Penitencia", "Puerta", "Paquete", "Portar", 
            "Pereza", "Pánico", "Puño", "Plomo", "Pesar", "Pesado", "Posando", "Pensando", "Pararse", "Padres", 
            "Patear", "Pala", "Posición", "Purga", "Punto", "Pulsar", "Pulsación", "Preservación", "Pulso", 
            "Planear", "Planificar", "Podrido", "Paciencia", "Pesadilla", "Purgatorio", "Peste", "Pasar", 
            "Pistola", "Puntería", "Qué", "Querer", "Quién", "Quienes", "Quebranto", "Quiebra", "Quemadura", 
            "Quemaduras", "Quejido", "Quisquilloso", "Quirúrgico", "Querella", "Quebradizo", "Rata", "Ratas", 
            "Rastrero", "Rapiña", "Reutilizar", "Repugnante", "Resiliente", "Resistente", "Remanente", "Rayo", 
            "Risa", "Reír", "Río", "Raciocinio", "Reservado", "Rudo", "Razón", "Ruego", "Rencor", "Resentido", 
            "Régimen", "Renegado", "Refugio", "Resentida", "Rebelde", "Racionado", "Rebeldía", "Renacimiento", 
            "Renacer", "Resentimiento", "Ritual", "Roca", "Rocas", "Rescate", "Reliquia", "Rifle", "Rabia", 
            "Radiactivo", "Radioactividad", "Rato", "Radio", "Reto", "Robar", "Rozar", "Ruina", "Ruinas", 
            "Resistencia", "Romper", "Rompedor", "Rugido", "Remarcar", "Retener", "Reorganizar", "Riesgo", 
            "Rastrear", "Rastro", "Redención", "Recolectar", "Recolector", "Reparar", "Replantear", "Rincón", 
            "Restos", "Responsabilidad", "Reciente", "Rápido", "Remasterizado", "Respuesta", "Ruptura", "Suerte", 
            "Solución", "Sencillez", "Satisfacción", "Supermercado", "Saqueado", "Sabiduría", "Serenidad", 
            "Santuario", "Silencio", "Sinceridad", "Sincero", "Sincera", "Sofisticado", "Saturado", "Seco", 
            "Secos", "Sentado", "Sentada", "Siempre", "Salir", "Soñar", "Sanarse", "Sanar", "Sangre", 
            "Sangriento", "Sanguinario", "Sediento", "Sudar", "Sudor", "Secreto", "Secretismo", "Sometimiento", 
            "Salvar", "Salvación", "Salvaje", "Salvajes", "Siniestro", "Síndrome", "Siniestra", "Suplicio", "Senda", 
            "Situado", "Situación", "Superación", "Salvador", "Sombra", "Sombras", "Sonreír", "Sonrisa", "Sonriente", 
            "Suave", "Seguro", "Solo", "Solitario", "Sublime", "Sutil", "Suficiente", "Satisfactorio", "Solucionable", 
            "Suerte", "Sutileza", "Sensibilidad", "Sufrimiento", "Sigilo", "Traer", "Tamaño", "Tristeza", "Travesía", 
            "Trampa", "Tumba", "Tortura", "Tonto", "Trasmisión", "Tarado", "Talón", "Trasformar", "Trastorno", 
            "Tragedias", "Trasmitir", "Tener", "Tragar", "Tesoro", "Terrible", "Tensión", "Terror", "Temor", "Tolerancia", 
            "Tanque", "Trueno", "Tos", "Talar", "Talado", "Traición", "Teléfono", "Televisor", "Trasformación", 
            "Tratamiento", "Traidor", "Traidora", "Traicionera", "Tormentosa", "Tormenta", "Trémulo", "Tregua", "Trinchera", 
            "Transitar", "Trasportar", "Temerario", "Temeraria", "Testamento", "Tiranía", "Tiránicos", "Torniquete", 
            "Tormento", "Tóxico", "Tóxicos", "Trueque", "Trasportador", "Tienda", "Tiniebla", "Tinieblas", "Ubicación", 
            "Último", "Urgencia", "Ultratumba", "Utilizar", "Umbral", "Umbroso", "Unánime", "Ulular", "Urbano", "Utensilio", 
            "Utopía", "Unción", "Unificación", "Ultraje", "Vanidad", "Vida", "Velocidad", "Viento", "Varilla", "Virus", 
            "Virulento", "Vegetación", "Vacío", "Vicio", "Vencedor", "Venganza", "Vorágine", "Veneno", "Violencia", 
            "Vestigios", "Vértigo", "Vástagos", "Valle", "Vendaval", "Víspera", "Vísperas", "Vil", "Voz", "Vaticinio", 
            "Xenofobia", "Xilófono", "Xenón", "Xerosis", "Xilófago", "Xenogénesis", "Xenocidio", "Yermo", "Yacimiento", 
            "Yacimientos", "Yugular", "Yugo", "Yelmo", "Yacer", "Zombi", "Zombis", "Zona", "Zafarrancho", "Zozobra", "Zanja", 
            "Zigurats", "Zarpa", "Zarpas", "Zambullida", "Zarcillo", "Zarcillos", "Zumbido", "Zapadores"

        )
    }
    return random.choice(palabras[dificultad]).upper()
def imagen_juego(intentos_restantes:int):
 if intentos_restantes==6:
  imagen_1="""
+*@%@@@@@@##@@@@@@@@@@@@@@@@ @@@@@@@@@*@@@@@@@@@@@@@@@@                          
 ++@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@*@@@@@@@@@@@@@@@@                          
 +#%%@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@*@@@@@@@@@@@@@@@@                          
 *#%@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@*@@@@@@@@@@@@@@@@                          
     %@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@                                 
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@                                 
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@                                 
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@                                 
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@                                 
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@                                 
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@                                 
     @@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@@@                           
     @@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@@@                           
     @@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@@@                           
     @@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@*@@@@@@@@@@@@@@@                           
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@                                 
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@                                 
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@                                 
     %@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@                                 
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@                                 
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@                                 
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@#@@@@@@@@@                                 
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@#@@@@@@@@@@@@@@@@                          
     @@@@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@@@@@@@@                          
     @@%@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@@@@@@@@                          
     @@%@@@@@@@    @@@@@@@@@@ @@@@@@@@@*@@@@@@@@@@@@@@@@                          
      @%@@@@@@     @@@@@@@@@  @@@@@@@@@ @@@@@@@@@@@@@@@                           
                                                                                  
*@@@@@@@@@          @@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@##%      
+%@@@@@@@@         @@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%@      
*@@@@@@@@@         @@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
#@@@@@@@@%         @@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
%@@@@@@@@@         @@@@@@@@@@@@@@@@  @@@@@@@@@@ @@@@@@@@@    @@@@@@@@@@           
%@@@@@@@@%         @@@@@@@@@@@@@@@@  @@@@@@@@@@ @@@@@@@@@    @@@@@@@@@@           
%@@@@@@@@@         @@@@@@@@@@@@@@@@  @@@@@@@@@@ @@@@@@@@@    @@@@@@@@@@           
#@@@@@@@@@        @@@@@@@@@@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@    @@@@@@@@@@           
%@@@@@@@@%        @@@@@@@@@@@@@@@@@@ @@@@@@@@@@ %@@@@@@@@    @@@@@@@@@@           
%@@@@@@@@%        @@@@@@@@@@@@@@@@@@ @@@@@@@@@@@             @@@@@@@@@@           
#@@@@@@@@@        @@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@           @@@@@@@@@@           
%@@@@@@@@%        @@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@         @@@@@@@@@@           
%@@@@@@@@@       @@@@@@@@@@@%%%@@@@%    @@@@@@@@@@@@@@       @@@@@@@@@@           
%@@@@@@@@@       @@@@@%%@@@@@%%@@@@@      %@@@@@@@@@@@@      @@@@@@@@@@           
%@@@@@@@@@       @@@@@@@@@ %@@@@@@@@@      @@@@@@@@@@@@@@    @@@@@@@@@@           
%@@@@@@@@@       @@@@@@@@@ @@@@@@@@@@        @@@@@@@@@@@@    @@@@@@@@@@           
%@@@@@@@@@       @@@@@@@@@@@@@@@@@@@@ %#%%%%%% @@@@@@@@@@%   @@@@@@@@@@           
%@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@ @@@@@@@@@@   @@@@@@@@@@           
%@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@ @@@@@@@@@@   @@@@@@@@@@           
#@@@@@@@@%      @@@%@@@@@@@@@@@@@@@@@#@@@@@@@@@ @@@@@@@@@@   @@@@@@@@@@           
%@@@@@@@@%      @@@@@@@@@@  @@@@@@@@@%@@@@@@@@@ @@@@@@@@@@   @@@@@@@@@@           
%@@@@@@@@%      @@@@@@@@@%  @@@@@@@@@%@@@@@@@@@ @@@@@@@@@@   @@@@@@@@@@           
#@@@@@@@%*%%%%%%@@@@@@@@@   @@@@@@@@@%@@@@@@@@@ @@@@@@@@@@   @@@@@@@@@@           
#@@@@@@@%@@@@@@%@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@           
%@@@@@@@%@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@           
#@@@@%@@@%@@@@@@@@@@@@@@@    @@@@@@@@@ @@@@@@@@@@@@@@@@@     @@@@@@@@@@           
 *%@@%%#%%%@@%@%@%#%@@@@     @@@@@@@@@   @@@@@@@@@@@@@        @@@@@@@@@           
                                                                                  
   @@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@     @@@@@@@@@ @@@@@@@@@@   @@@@@@@@%##%%%   
  @@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@     @@@@@@@@@ @@@@@@@@@@ @@@@@@@@@%###%%%@@ 
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@%**#%##%#*
 @@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@%#%%#%%#*
 @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@%%%%%      @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@ %#%%##%#%
 @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@ %%%%##%%%
 @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@ %%%%%#%%%
 @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@ @@@@@@@@@
 @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@ @@@@@@@@@
 @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@ @@@@@@% 
 @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@%        
 @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@%      @@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@@@%      
 %@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@%#*     @@@@@@@@@ @@@@@@@@@@  @@@@@@@@@@@@@@    
 -%@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@##     @@@@@@@@@ @@@@@@@@@@    @@@@@@@@@@@@@@  
 @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@@@@@@ @@@@@@@@@@      @@@@@@@@@@@@@ 
 #%@@@@@@@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ %%@@@@@@@@        @@@@%@@@@@@@
 *#@@@@@@@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ @@@@@@@@@@          @@@%@@@@@@
 **@@@@@@@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@ @@@@@@@@@
 **%%%@@@@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@ @@@@@@@@%
 +=+#%%@@@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@ @@@@@@@@@
 +=+@@%@@@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@ @@@@@@@@@
 +=*%%@%%@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@ @@@%@@%@@
 =-#%@@@@@ @@@@@@@@@@@@@@@@@@@@           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@ @@%@@@%%#
 %##@@@@@@@@@@@@@@@@@@@@@@@@@@@           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@%%%
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           @@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@%%%%%#*
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@            @@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@%%%@#**
   @@@@@@@@@@@@@@@@  @@@@@@@@@@             @@@@@@@@@@@@@@@@     @@@@@@@@@@##%%*                                                                                                                                                                                              
"""
 elif intentos_restantes==5:
    imagen_1="""                                 :#%%%@%*                                                                                                   
                               =##%%@@@@@@%:                                                                                                
                              =##%%@@%%%%%%#-                                                                                               
                              *#%%%%###****--                                                                                               
                              ####*#####***-                                                                                                
                              ##+=*#%@%%%#%*                                                                                                
                              :*:-*#**###+%:                                                                                                
                               -.-*%###%%**.                                                                                                
                               :-+#%##%%#=-                                                                                                 
                             .+*###%#####.                                                                                                  
                        -+****####%@%%%#                                                                                                    
                     :+*##**+*#####%%*                                                                                                      
                   -*######*+=-===-+*                                                                                                       
                  +#%%%####**+==--::-.                                                                                                      
                 +#%%%%%%###***+=-:--..                                                                                                     
                +%%%@@%@%%%##%##*=-:-=....                                                                                                  
               .#@@@@@@@@%%%@@%%#+=-:-=....                                                                                                 
               *@@@@@@%@@%@@@@%%#*+=-:==-:..                                                                                                
              -%@@@@@@@@%@@@@@@%%#*=-:----:.                                                                                                
              #@@@@@@@@@@@@@@@@%%%#+=--=:-:.                                                                                                
             -@@@@@@@@%@@@@@@@@@@@%%*++*+--.                                                                                                
             #@@@@@@@@@@@@@@@@@@@@@@####*+=:                                                                                                
            +@@@@@@@@#%@@@@@@@@@%%%%*#+++*#:                                                                                                
            *@@@@@@%=#%@@@@@@@@@%%%%*+===-.                                                                                                 
           +%@@@%%  :*%@@@@@@@@@@%%%#*+---                                                                                                  
          -#@@@@%   -*@@@@%@@@@@@@@%%#*==-                                                                                                  
          *@@@@@#   *###%@@@@@@@@%@%%#+==-                                                                                                  
          #@@@@@-   =*@%@@@@@@@@@%%%#*+=-=                                                                                                  
         .@@@@@@    +#@@@@@@@@@@@@%%%#+=-=.                                                                                                 
          @@@@@%   =%%%@@@@@@@@@@@@@%%*=-++                                                                                                 
          @@@@@@   +%@@@@@@@@@@@@@@%%#*=-*#:                                                                                                
          #@@@@@  :*#%%@@@@@@@@@@@@@%#*+-*#+                                                                                                
          :@@@@@  +#%@@@@@@@@@@@@@%%%##++@%#                                                                                                
 .%       :@@@@@  %@@@@@@@@@@@@%%%#%%##=+@@%=                                                                                               
          *%###+ +%@@@@@@@@@@@@@@@@%%#*=#@@%#                                                                                               
         +####*=+@@@@@@@@@@@@@@@@@@@@@%*%@@@%*                                                                                              
        +@%%%%+*#%@@@@@@@@@@@@@@%%%%%@#*=*%@@%.                                                                                             
         *@@@@%@%%%@@@@@@@@@@@@@%%%%%@*#= #@@%*                                                                                             
            .#  :@@%@@@@@@@@@@@@@%##%%%%* -*++-                                                                                             
                 -@@@%@@@@@@@@@@@%%@@@@@#  :.-:                                                                                             
                  %@@@@@@%@@@@@@@%@@@@@@@: -+-*=                                                                                            
                  %@@@@@@@@@#@@@@%@@@@@@@= --***+                                                                                           
                  %@@@@@@@@@@@@#%%@@@@@@@*   :.                                                                                             
                  #%@@@@@@@@@@@@@@*#@@@@@+                                                                                                  
                 =@@@@@@@@@@@@@@@@@@@#%@@=                                                                                                  
                 .@@@@@@@@@@@@@@@@@@@@@@+.                                                                                                  
                  @@@@@@@@@@@@@@@@@@@@@@@#.=                                                                                                
                  @@@@@@@@@@@@@@@@@@@@@@@.    =            @@@.                                                                             
                  @@@@@@@@@@@@@@@@@@@@@@%        ++      -@@@@%                                                                             
                  %@@@@@@@@@@@@@@@@@@@@@-           .-..@@@@@:                                                                              
                  @@@@@@@@@@@@@@@@@@@@@@                @%                                                                                  
                  @@@@@@@@@@@@@@@@@@@@@+                                                                                                    
                 @@@@@@@@@@@@@@@@@@@@@@                                                                                                     
                =%@@@@@@@@@@%@@@@@@@@@%                                                                                                     
                %@@@@@@@@@@@@@@@@@@@@@                                                                                                      
               #@@@@@@@@@@@%%@@@@@@@@@                                                                                                      
              *@@@@@@@@@@@@@@@@@@@@@@@                                                                                                      
             .@@@@@@@@@@@@%@@@@@@@@@@#                                                                                                      
             *@@@@@@@@@@@@@@@@@@@@@@@                                                                                                       
             @@@@@@@@@@@@#@@@@@@@@@@#                                                                                                       
             @@@@@@@@@@@* @@@@@@@@@@:                                                                                                       
            .@@@@@@@@@@@. @@@@@@@@@@                                                                                                        
            .@@@@@@@@@@@ -@@@@@@@@@@                                                                                                        
            @@@@@@@@@@@# -@@@@@@@@@@                                                                                                        
            @@@@@@@@@@@  -@@@@@@@@@@                                                                                                        
            :@@@@@@@@@    @@@@@@@@@                                                                                                         
             +@@@@@@@.    @@@@@@@@=                                                                                                         
             +@@@@@@@:    @@@@@@@@-                                                                                                         
             #@@@@@@@@   #@@@@@@@@#                                                                                                         
            #@@@@@@@@@@%@@@@@@@@@@@@+                                                                                                       
           +@@@@@@@@@@@@@@@@@@@@@@@@@@%    """
 elif intentos_restantes==4:
  imagen_1="""                                                                                                     ...
                                                                                          .......::=++**
                                                                              .......::--==++++*********
                                                                     .:-=+++++++++++++++*++++++++++****+
                                                                .:-=++**++++++++++++++++++++++++********
                    :.                                       .:=+**********++++++++++++++++++***********
                   .*.                 ..                 .:=***************+++++++*+++++*************##
                    :+........=::.::....               .:+****#****************++++++***###+++*###%%%%#*
                  .:.-%%#%#%%%####*%%*+.. ..          :*##########*****##*##********###%%##***#%@@%%%#*+
                  .-*###%%%%#%######*#%%##*+*+=-:...-+###***##############%##*###***##%%%%%%%@%##%##*+*#
             .:=+*#%%%%%%%%%##%#####+###%%#**####%#%%######**#######%#########****##%#*#%@@@%%##%#*##*##
           .-+###%%%%%%%%%%%%%%####%**##%%%#+*+*%%%%%%%########%%##%%#########*###%%%%%@@@%%%%%######%##
          .+###%%%%%%@@@@%%%%%%%%#%%%%###%##****#####%%%%#%#%#%%%%#%%%##########%%%%@@@@%%%%%#####%%%%%%
        ..+%##%%%%%%@@%%%%%##%*##*##%##%%%%%%%%%*#%#*##%%%%%%%#%%%%%%%#######%%%%%@@@@%%%%%%###%#%%%%%%#
        :#%##%%%%%%%%#**#***#***######++**##%%%%%%######%%%%%%@%%%%%%%###%%%%%%%%%@@@%%%%####%#%%###****
      .=#%%%%%%%%%%##**+++*###*++*#*****++#%%%%%%%%%%##*##%%%%%@@%%%%%%%#%%%%%%%%@@%%%%%########****####
      =#%%%%%%%%%#####**+*###*+*#+##**+***++#%%%%%%%%######%@%%%%%%%%%%%%%%%%%%%%@@%%%########**######%%
     :#%%%%%%%%%#******++#%***##*******###*+*##%%%%%%%%%%%##%%%%%%%%%@%%%%%%%%%%@@%#%##########%%#######
     =%%%%%%%%%%#********#%#%%#%*****#####**##%%%%%%%%%%%%%##%%%%%%%%%@@%%%%%%%%%%%%%###################
    .+%%%%%%%%@%###******%%%@%%%%%#%####*+++**##%%%%%%%%%%%@%%%%%%%%%@@@@%%%%%%%%%%%####################
    .#%%%%%%%@@%%%##**#*#%%@%%%@%%%%%#**++*##%%%%%%@%%%%%%@@%%%%@%%%%%%@@@%%%%%##########**##**######%%#
    .#%%%%@%@@%##%%#####%%%%@@@@%%###**##%%%@@@@%%%%%%%%%%%@@%%%%%%@@%%@@@%##*#########################%
     =%%%%@%@@%%%#%######%%%%%%##*####%%%%%%@%%###%%@%%%%%%@@@@@%%%%@@@@%######%%######%%%%%############
     .*%%%%%@%%%%%%%%#####%###*+++*#**#%%@@%%%%#%%%%@%%%%%%%@@@@@@%@%%%%##%%%%%####%%%%%%%####%%%%%#####
      :%%%%%@@%%%%%%%##%%%%%%%%#*#*++#%%@@@%%@%%%@%%@%%%%%%@@@@@%%@@%%%%%%%%%%%%%%%%%%%%##%%%%%%%%%%%%%%
       :#%%@@@%@%%%%%%%%%@@@@@@@%%%###%@@@@%%@%@@@%%%%%%%%@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%
        .#@%@@@@@@@@@%%%%@@@@@@%@%%%%@@%@@@@@@%@@%@%%%%%%%@@@@%%@@@%%%%%%%%%%%%%%@%%%%%%%%%@%%%%%%%%%%@@
         .*@@@@@@@@@@@%%%@@@@%%%%%%@%%@@%@@@@@@@@@%%%%%%%%@@@@@@@@%%%%%%%%%%%%%%@%%%%%%@%@%%%%%@@@@@@@@@
          .-*%%@@@@@@@@@@@@@@@@@%%%%%%%%%%@@@@@@@@%%%%%%%@@@@@@@@@%%%@%@%%@@%@%@@%%%%@@@@%%%@@@@@@@@@@@@
            ...:=***####################%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@
                                           ............................::...=##%%%%%%%%%@@%%%%#****###%%
                                                                                  ...........          .
                                                                                                           
"""
 elif intentos_restantes==3:
  imagen_1="""        .::.                                                                          
                                                            =***+++=:                                                                       
                                                           ******++++=.                                                                     
                                                          =*******+++==                                                                     
                                                          *****++++++=                                                                      
                                                         -****+++++==    .:                                                                 
                                                         -***+++++=::    =+.                                                                
                                                     .==+****+++++.      .+.                                                                
                                                  -*#*+===+**+=:==.                                                                         
                                                 -###**+--=++=-..-==                                                                        
                                                 *###**++===++=-:---.                                                                       
                                                 *##***+++==+*=---:-.                                                                       
                                                 *##**=***+=+*+==-:=:                                                                       
                                                 *###**+**+==+++=:==-                                                                       
                                                 *###*++#*+===++=-++=                                                                       
                                                 *###*++##*+++++++**+                                                                       
                                                 *###*-*##***++++***+=                                                                      
                                                 *%%###*++****+=+***+-                                                                      
                                                 *%%%%#########*++++*.                                                                      
                                                 #%%%%%%%######*++=+#                                                                       
                                                 #%%%%%%%%##*++***+++.                                                                      
                                                 %%%%%%%%%###*=.:***+                                                                       
                                                .%%%%%%%%####*=-==+=                                                                        
                                                -@@%%%%%####**+*++                                                                          
                                                :@@@@%%%%#####**#*+                                                                         
                                                 @@@@@@%%%####%%%%#*                                                                        
                                                 %@@@@@%%%#*#%%%%%%#*                                                                       
                                                 =@@@@@@%%%*#@@@%%%%#+                                                                      
                                                  @@@@@@%%%##@@@@%%%%#+                                                                     
                                                  #@@@@@@%%##@@@@@%%%%#-                                                                    
                                                  :@@@@@@@%#= %@@@@@@%#+                                                                    
                                                   @@@@@@@@%:  *@@@@@@%#.                                                                   
                                                   @@@@@@@@%.   %@@@@@%%=                                                                   
                                                   %@@@@@@@%    %%@@@@%%*                                                                   
                                                   @@@@@@@@%    %@@@@@@%*                                                                   
                                                   %@@@@@@@#    @@@@@@@%*                                                                   
                                                   %@@@@@@@.   -@@@@@@@%=                                                                   
                                                   #@@@@@@%    +@@@@@@@@:                                                                   
                                                   @@@@@@@:    *@@@@@@@@                                                                    
                                                  .@@@@@@.     +@@@@@@@*                                                                    
                                                  #@@@@*        @@@@@@@=                                                                    
                                                  @@@@*           =@@@@@                                                                    
                                                 :@@@@            .@@@@@                                                                    
                                                 #@@@@            +@@@@@#                                                                   
                                                 @@@@+            @@@@@@@%                                                                  
                                                -@@@@=             *@%@@@@@%*:                                                              
                                                %@@@@*                  :@@@@@@                                                             
                                                @@@@@%                                                                                      
                                                =@@@@@@%                       """
 elif intentos_restantes==2:
  imagen_1="""      .-....::.                                                           
                                                                       .:++=--::::::-                                                        
                                                                      .:.-*---------=:                                                       
                                                                     ::.   :-------==.                                                       
                                                                    *-.       :---=+.                                                        
                                                                   =+            .                                                           
                                                                  #=                                                                         
                                                                 #-                                                                          
                                                               .%.                                                                           
                                                              :*                                                                             
                                                             =*                                                                              
                                                            **                                                                               
                                                           #=                                                                                
                                                          %:                                                                                 
                                                        .#.                                                                                  
                                                       :#                                                                                    
                                                      =+                                                                                     
                                                     *+                                                                                      
                                                    %=                                                                                       
                                                   @-                                                                                        
                                                 .%:                                                                                         
                                                -#                                                                                           
                                               ++                                                                                            
                                              #+                                                                                             
                                             %+                                                                                              
                                            @-                                                                                               
                                          .%.                                                                                                
                                         =#                                                                                                  
                                        **                                                                                                   
                                       %+                                                                                                    
                                      @*                                                                                                     
                                     @=                                                                                                      
                                   :@:                                                                                                       
                                  +%                                                                                                         
                                 ##                                                                                                          
                                %+                                                                                                           
                               @+                                                                                                            
                             .@+                                                                                                             
                            -@-                                                                                                              
                           +%:                                                                                                               
                          .#                                                                                                                 
                          .                                                                                                                  
                        ..                                                                                                                   
                       ..                                                                                                                    
                      ..                                                                                                                     
                     .                                                                                                                       
                    .                                                                                                                        
                  ..                                                                                                                         
                 ..                                                                                                                          
                ..                                                                                                                           
               ..                                                                                                                            
            :%-                                                                                                                              
           =##=                                                                                                                              
          +%%=                                                                                                                               
         #%%:                                                                                                                                
        #%%.                                                                                                                                 
      :%%#                                                                                                                                   
     =%%*                                                                                                                                    
    +%%+                                                                                                                                     
   #%%=                                                                                                                                      
  #%%:                                                                                                                                       
:###. """
 elif intentos_restantes==1:
  imagen_1="""                                       --------========              
                                                   .******#####%%%%%              
                                                   .*******###%%%%%%              
                                                   .+****####%%%%###              
                                                   .***##########**#              
                                                   .*#####%##******#              
                                            .+*+****#######********#              
                                      ......-**#########*=                        
                                     .%%%##***#########**=                        
                                     .%%%############****=                        
                                     .%####%%%%###:                               
                                 .#@%#####%%%%#***                                
                               -=+#%%%%%%%%%%%:                                   
                             :=#%%%%%%%%%%%%%%:                                   
                            .%%%##%%%%%%@@@@@@-                                   
                            *%#####%%%%%%%%@%%=                                   
                          :##*==*##%%%%%%%%%%%=                                   
                         :##+-::-#%%%%%%%%%%%%=                                   
                        .*#*=-::=#%%%%%%%%%%%%=                                   
                        +##+=--=*#%%%%##*#%%%%=                                   
                       -###*+==+*##%%%##*#@%@@=                                   
                      .####*****#%%%%%%###@@@@+                                   
                      *%#****##%%%%%%%%%%%@@@@%##=                                
                     =%%****##%%%%%%%%@@@@@@@@@%%=                                
              @%%%%%%%%%#**#%%%@@@@@@@@@@@@@@@@@@%-                               
              %%%###%%@%%%%%@@@@@@@@@@@@@@@@@@@@@@=                               
              %%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*--------:::::::::              
              ####%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@%%#####**              
              ################%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@%%%%####              
              #################%%%%%%%%%%%%%%%%@@@@@@@@@@@@%%%%%%%##              
              ###################%%%%%%%%%%%%%%%%%%%%@@@@@@@@@%%%%%#              
              ###%%%%%%%%##%%%%#######%%%%%%%%%%%%%%%%%@@@@@@@@%%%##              
              ######%%%%%%%%%%%%%%#####%%%##%%%%###%%%%%%@@@@@@@%%##              
              %#######%%%%%%%%%%%%%%####%##%%%%%#####%%%%%%%%@@@@%%#              
              %%%#######%%%%%%%%%%%%%########%%%%%#########%%%%@@@%%              
              %%%%########%%%%%%%%%%%%%%%#######%%#%%%%#####%%%%%%%%              
              %%%%%%%%#####%%%%%%%%%%%%%%%%%%#######%%%%%%%%%%%%%%%%              
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###%%%%%%%%%%%%%%%              
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%              
              #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%              
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%              
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%              
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%              
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%              
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@%%%%%%              
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@%%%              
              =============+++++++++++++++++++++++++++++++++++++++++  """
 print(imagen_1)
def mostrar_tablero(palabra_oculta, letras_encontradas):
    tablero = ""
    for letra in palabra_oculta:
        if letra.upper() in letras_encontradas:
            tablero += letra
        elif letra == "_":  
            tablero += "_"
        else:
            tablero += "_ "
    print("\nPalabra:", tablero)

def seleccionar_dificultad():
    while True:
        dificultad = input("Elige dificultad (facil, medio, dificil): ").lower()
        if dificultad in ["facil", "medio", "dificil"]:
            return dificultad
        else:
            print("Opción inválida. Elige entre: facil, medio o dificil.")

def jugar_ahorcado():
    dificultad = seleccionar_dificultad()
    palabra_oculta = obtener_palabra_aleatoria(dificultad)
    letras_encontradas = []
    intentos_restantes = 6
    print()
    print("\n¡Bienvenido al juego del Ahorcado! 🎮")
    print(f"Dificultad seleccionada: {dificultad.capitalize()}")
    
    while intentos_restantes > 0:
        imagen_juego(intentos_restantes)
        mostrar_tablero(palabra_oculta, letras_encontradas)
        letra = input("Introduce una letra: ").upper()

        if not letra.isalpha() or len(letra) != 1:
            print("Ingresa solo UNA letra válida.")
            continue

        if letra in letras_encontradas:
            print("Ya usaste esta letra. Elige otra.")
            continue

        if letra in palabra_oculta:
            letras_encontradas.append(letra)
            if all(l.upper() in letras_encontradas or l == "_" for l in palabra_oculta):
                print(f"\n¡Has ganado! La palabra era: {palabra_oculta}")
                print("""                    .-*%@@@@@@@@%#+:                                                                
                                               .=%@@@@@@@@@@@@@@@@@%+:                                                            
                                             -*%@@@@@@@@@@@@@@@%%%%%@@#:                                                          
                                           -#%%@@@@@@@@@@@@@@@@@@@%@%%%%+                                                         
                                         .*@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%+                                                        
                                        .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%+                                                       
                                       -%@@@@@@@@@@@@@@@@@@@@%%%%@@%%%%%@%%+                                                      
                                      =@@%%@@@@@@@@%########*#*##%##**+*#%%%-                                                     
                                     =@@@@@#%@@@%@%#**+*********##****++++%%*                                                     
                                    .%@@@@%%@@@@%%#*****+*******###***+++=*%#-                                                    
                                    :@@@@@%%%%%%#**+****************++++===#*+.                                                   
                                    -@@@@%%%%%%%#***+++++++++*********##%#+**+:                                                   
                                    :@@@%@%%%%%%#****#%%%%%##*****##%@@%#**+*+-                                                   
                                    :@@@@@%%%%%%#*#%%@@@@@@@@%%#*+*%%%%%##*++*-                                                   
                                    :%@@@@%%%%%##*#%###@@%%%%##++=+#%%%#*==+=#-                                                   
                                     *@@%%%%%%%###%##**####%#***++==+*###*=====                                                   
                                     :%@@%@%%%%#****####*##*****++===+++++==--:                                                   
                                      *@@@@@%%#*++=+++++++++*#*++++==**+++===-:                                                   
                                      =%**%@%@%#*+==+++++++*#*++*++===**+==-==-                                                   
                                      -#*+*%%@@%##****++++*#%%%%%%###%###*=-=--.                                                  
                                       **+*%%%@@%##**#*+*####%%%%@@@%%%%%%#+===.                                                  
                                        +####%@@%#######%@%%@@@@%%%%###%%@@#+**:                                                  
                                         =**#%@@%%%%@%%%@@@@%%%#***++++**%%%#%%:                                                  
                                          =%%#%@@@@@@@@@@@%*+++****#*==+**%%%%*.                                                  
                                           :#%#%%@@@@@@@@@%**#%@@@@%@@%*+#%%%*-                                                   
                                            :#%%%%%%@@@@@@%###%@@%%@@%#**#%@%-                                                    
                                             .#%#%%@@@@@@@@@%#%#%%%%##***#%%+                                                     
                                              -#*#%@@@@@@@@%%%*#*##%#*****##-.                                                    
                                               =++*#%@@@@@@@%%%%##%@@%####**=.                                                    
                                               :++**##%@@@@@@@@@@%@@@@@%%#++-:                                                    
                                               :**++**#%%@@@@@@@@@@@@@%*++++=-.                                                   
                                               +#*++++*###%@@@@@@@@@@%#++*+==-::.:.                                               
                                            .=#%#*+++++**##%%%%%%%%%#*+=+++==---=*@@@@@@@@@@@%*+-                                 
                                      .::=*%%#***#*++++++**####%%%%#*+=+++===---=+%@@@@@@@@@@@@@@@%=.                             
                                .-*#@@%#@@@@#++++**+++++++***######*+=+*+====---=+#@@@@@@@@@@@@@@@@@%*-                           
                             -#@@@@@@%#@@@@@#+++++++++++++++++***#**++*++========+%@@@@@@@@@@@@@@@@@@%##+:                        
                          =#@@@@@@@@@@%@@@@@%*++++++++++++++++**##*****++=++====+*%@@@@@@@@@@@@@@@@@@%%%%##=.                     
                       :*@@@@@@@@@@@@%%@@@@%%%*++++==+++++++**********++=+*++==++#@@@@@@@@@@@@@@@@@@@@@@@@%%%+.                   
                     -#%@@@@@@@@@@@@@%%@@@@@@%%#*+++++***++++********+*+*#*++++*%@@@@@@@@@@@@@@@@@@@@@@@@@@%%@%#:                 
                   -#%@@@@@@@@@@@@@@@%@@@@@@@@@@%%##**###**+++***##*+**#*****#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@%+                
                 -#@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%##*++==+*********##%@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@%%@@@%*:              
               .*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##**#####%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%@@@%@@@@%#-             
              =%@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@%#=            
             +@@@@@@@@@@@@@@@@@@@@@@%@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@%@%@@@@@@@@@%%#=           
           .*@@@@@@@@@@@@@@@@@@@@@@%%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%@@@@@@@@%%#*=          
          .#@@@@@@@@@@@@@@@@@@@@@@@%%@%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@%@@@@@@@@@@%%##*:         
          *@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%@%@@@@@@@@@@@@@@%@@@@@@@@@@%###+.        
         =%@@@@@@@@@@@@@@@@@@@@@@@@#%%%%%%@@%%@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%@@%@@@@@@@@@@@@@@@@@@@@@@@@@%##*-        
        .#@@@@@@@@@@@@@@@@@@@@%@@@@%%%%%%%%%%@@@@%%%@@@@@@@@%@@@@@%%%%%%%%%%%%%%%%%%%@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@%%%#+        
        -%@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%@@@@@@@%@%%%%%%%%%%%%%%%%%%%%%%%@@@%%%%%%@@@@@@@@@@@@@@@@@@@@@@@%%%#*:       
        =@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%@@@%%%%%%%%%%%%%%%%%@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@%%##=       
        +@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%@@@%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##*.      
        *@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%@@@%%%%%%%%%%%%%@@@@@@@@@#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%##:      
        *@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%%%%%%%%%%@@@@@@@@%@@%%%%%########@@@@@@@@@@@@@@@@@@@@@@%##-      
       .#@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@%%+      
       :%@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@%%#.     
       -%@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-     
       =@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%#%%%%%%%%%%%%%%%%%%@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@@@@@@@@@@@@@@@@*     
       +@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@%-    
       *@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@+    
      .#@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@#.   
      .#@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@%*:   
      .%@@@@@@@@@@@@@@@@@@@@@@@@@@%@%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@%#**=   
      :%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@%%%%%##*+:  
      -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@%%%%%%%%%###*-  
      =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@%@@@@@%%%%%%%%%%%%###*+. 
      +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%@@@@@%%%%%%%%%%%%%###*- 
      *%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@%%%%%%%%%%%%%###+ 
     .#%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@%%%%%%%%%%%%###*:
     -%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@**%@%%%%%%%%%%@%%%###-
     =@%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@+:%@@%%%%@@%%@@@%%%%#+""")
                return
        else:
            intentos_restantes -= 1
            print(f"Letra incorrecta. Intentos restantes: {intentos_restantes}")
        print("""                     .:-=*#%@@@@@@@@@#+:                                                  
                                                      .=*@@@@@@@@@@@@@@@@@@@@@@@@@.                                               
                                                .*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+                                              
                                            -%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%                                             
                                         =%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##%@@+                                           
                                      .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+++***#@-                                         
                                    .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@#+++==+++++++%:                                       
                                  .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@%*=============++@-                                     
                                 %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@%*+===========++==++*@-                                   
                               *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@%*++++***##%%##*++++===+@@-                                 
                             :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@#*+*#%@%#%@@@@@@@@%#*+====#@%.                               
                            *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%***#%%%#####%%@@@@@@@%*+===+*@@=                              
                           %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**###########%%%@@@@@%#**+++*##@@#                             
                         .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+****######@@@@@@@@%%%##*+++*#@@@@@#                            
                         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+++++**##%%@@%####%@@%%##*++=++%@@@@@@=                           
                       :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#+======+++++**########%##*++==--=*%%@@@@%                           
                      :#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#+====--==---======++++***+++=====-===+*#@@@*                          
                     .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#+===============++====++++++===-====--=======-=                         
                     %+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#+==+==========+++++++*****++++++====+=++===+*****.                       
                    -@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#++++++=====++****************++++==+*++=-=+*######-                       
                    +%=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#+++++++++++****#**###****++*+++===++**++=+*%@%%#%%#                        
                    *@+@@@@@@@@@@@@@@@%%%@@@@@@@@@@@%#*++++++++++**+********+++++++++++===+++*###%%**#%@#                         
                    -@@@@@@@@@@@@@@#%%%%####%%%@@@@@%*****++++***++++++****+++++++++===+++==--==+**++*##-                         
                     *@@@@@@@@@@@%%%###%%%###%%@@@%%#*************++++++++++*+++++++++=++++==--------=+*-                         
                     -@@@@@@@@@@@%%%*++==+*###%@@@%%#***************+++++*+++++++++++++++++==-----=*###*+.                        
                     :@@@@@@@@@@@%%%#+=+*#%%##%%@%@#*+++++++++++*****++*#*++++++++++++++++======+##%%%%%%#                        
                      #@@@@@@@@@@####++*%%##%@%%@%%#*++++++++++++++++++++++++++++++++=+++++++*#%%@@@@@@@@%.                       
                      -@@@@@@@@@@#*#*++*#***%@@%@%%*++++++++++++++++++++++++++++++++++*#####%%@@@@@@%%@@@@.                       
                       *@@@@@@@@@@#*##++***##%%%%%%##*+++++++++++++++++++++++++***##%%%%%%%%@@@@@@@@%@@@@@                        
                       :@@@@@@@@@@@#*##+++*+++*%###*##*+++++++++++++++++++++**###%@@@@@@%%%%#%%%@@@@@%@@@%.                       
                       .*@@@@@@@@@@@@*+*######*##**+****++++**++++++++++++**##%@@@@@%%##***++++++***##**#*-                       
                        *=@@@@@@@@@@@@%#*++==++*######**************++***#%%@@@@@%%#*++++=+====++**########                       
                        -+@@@@@@@@@@@@@@@@@%%%%%@@%%%#************+++**#%@@@@@%%**++++++++++++++++*##%%%%%#                       
                        =*-@@@@@@@@@@@@@@@@@@%#%####%##************###%@@@@@%%#*++++++**++++=+=++++***##%%*                       
                        :-:%@@@@@@@@@@@@@@@@@@#*****####*********##%%@@@@%%#*****++++++++++++==+=========+=                       
                         .:@@@@@@@@@@@@@@@@@@@%%**++**###*****#*##%@@@@%#*******+++*****+++++++=====-----==:                      
                          =@@@@@@@@@@@@@@@@@@@@%#*+++*##########%%%@@%##********************++++=====++++++++-.                   
                          %@@@@@@@@@@@@@@@@@@@@%%#*++**########%%%%%###*##***********************+++*****#*#*==                   
                          @@@@@@@@@@@@@@@@@@@@@@%%**+***#######%@@%###################*******###****########*==                   
                         .@@@@@@@@@@@@@%@@@@@@@@@%#******#####%%@%%##################################%%%%%%%*++                   
                         :@@@@@@@@@@@@@@@@@@@@@@@%%##****####%%%%%%####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@%#*++                   
                         =@@@@@@@@@@@@@@@@@@@@@@@@%%#*****####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@#*****                   
                         +@@@@@@@@@@@@@@@%@@@@@@@@@@%##****###%%%%%%%%%%%%%%%%%%%%%%%%%#*##**#%%%@@@%%%%#######.                  
                         -======================-=====--------------------=============--------==========-===== """)
    print(f"Has perdido. La palabra oculta era: {palabra_oculta}")


#def imagen_juego_segun_puntos(imagen_1:str):
  


jugar_ahorcado()


