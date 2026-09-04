import streamlit as st

st.set_page_config(
    page_title="Planificador EBI Inteligente - DocenteXXI",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# SIDEBAR
with st.sidebar:
    st.title("📖 DocenteXXI")
    st.caption("Ideas que brillan, aulas que inspiran")
    
    st.divider()
    st.subheader("⚙️ Configuración EBI")
    
    tramo = st.selectbox(
        "Selecciona el Tramo EBI:",
        options=[
            "Tramo 1 (3 y 4 años - Ed. Inicial)",
            "Tramo 2 (5 años de Inicial, 1° y 2° de Primaria)",
            "Tramo 3 (3° y 4° de Primaria)",
            "Tramo 4 (5° y 6° de Primaria)",
            "Tramo 5 (7° y 8° de Ed. Secundaria / Básica)",
            "Tramo 6 (9° de Ed. Secundaria / Básica)"
        ],
        index=1
    )
    
    espacio = st.selectbox(
        "Espacio del Conocimiento:",
        options=[
            "Espacio Científico-Matemático",
            "Espacio de Comunicación",
            "Espacio Creativo-Artístico",
            "Espacio de Ciencias Sociales y Humanidades",
            "Espacio de Desarrollo Personal y Social"
        ],
        index=0
    )
    
    subjects_map = {
        "Espacio Científico-Matemático": ["Matemática", "Ciencias de la Naturaleza", "Pensamiento Computacional"],
        "Espacio de Comunicación": ["Lengua Española", "Segunda Lengua / Inglés", "Literatura"],
        "Espacio Creativo-Artístico": ["Artes Visuales", "Expresión Corporal", "Música"],
        "Espacio de Ciencias Sociales y Humanidades": ["Ciencias Sociales", "Formación Ciudadana"],
        "Espacio de Desarrollo Personal y Social": ["Educación Física", "Educación Socioemocional", "Iniciativa Emprendedora"]
    }
    
    unidad_curricular = st.selectbox(
        "Unidad Curricular:",
        options=subjects_map[espacio]
    )
    
    metodologia = st.selectbox(
        "Enfoque Metodológico:",
        options=[
            "Aprendizaje Basado en Proyectos (ABP)",
            "Indagación Científica y Experimentación",
            "Gamificación Educativa",
            "Aprendizaje Cooperativo"
        ]
    )
    
    st.divider()
    st.info("💎 Premium: Descarga Word editable + 22 temarios oficiales 2026-2027")

# MAIN CONTENT
st.title("✨ Planificador EBI Inteligente")
st.markdown("Diseña secuencias didácticas completas con **coherencia total** entre contenidos, metas y criterios de logro.")

st.subheader("💡 ¿Qué quieres enseñar hoy?")

idea_docente = st.text_area(
    "Tu idea para la clase:",
    placeholder="Ej: Cómo se alimentan las plantas, fracciones dividiendo pizza, ciclo del agua...",
    height=100,
    label_visibility="collapsed"
)

def extract_learning_elements(idea, unidad, espacio):
    """
    Extrae los elementos de aprendizaje coherentes de la idea.
    Retorna: contenidos, concepto central, verbos de acción.
    """
    idea_clean = idea.strip().lower()
    
    # Mapeo de conceptos clave según la unidad curricular
    conceptos_por_unidad = {
        "Matemática": {
            "fracciones": ["dividir", "partes", "proporciones", "equivalencia"],
            "operaciones": ["suma", "resta", "multiplicación", "división"],
            "geometría": ["formas", "ángulos", "simetría", "perímetro", "área"],
            "medida": ["longitud", "masa", "capacidad", "tiempo"],
            "patrones": ["secuencias", "regularidades", "símbolos"]
        },
        "Ciencias de la Naturaleza": {
            "plantas": ["fotosíntesis", "raíces", "tallos", "hojas", "reproducción"],
            "animales": ["hábitat", "alimentación", "reproducción", "ciclo de vida"],
            "agua": ["ciclo", "estados", "evaporación", "condensación", "precipitación"],
            "energía": ["fuentes", "transformación", "luz", "calor"],
            "ecosistema": ["cadena alimenticia", "relaciones", "biodiversidad"]
        },
        "Lengua Española": {
            "lectura": ["comprensión", "inferencia", "vocabulario", "tipos de texto"],
            "escritura": ["ortografía", "coherencia", "estructura", "géneros"],
            "oralidad": ["expresión", "entonación", "escucha activa", "dicción"],
            "gramática": ["partes del discurso", "sintaxis", "análisis"]
        },
        "Ciencias Sociales": {
            "historia": ["cronología", "causas", "consecuencias", "períodos"],
            "geografía": ["ubicación", "paisaje", "recursos", "territorio"],
            "cultura": ["costumbres", "tradiciones", "identidad", "diversidad"],
            "sociedad": ["instituciones", "roles", "comunidad", "ciudadanía"]
        },
        "Educación Física": {
            "movimiento": ["coordinación", "equilibrio", "lateralidad", "motricidad"],
            "deporte": ["técnica", "estrategia", "reglamento", "juego limpio"],
            "salud": ["bienestar", "higiene", "nutrición", "actividad"]
        }
    }
    
    # Detectar conceptos en la idea
    conceptos_detectados = []
    verbos_accion = []
    
    # Búsqueda genérica de conceptos
    if "fracci" in idea_clean or "dividir" in idea_clean or "partes" in idea_clean:
        conceptos_detectados = ["Fracciones", "Proporciones", "Divisibilidad"]
        verbos_accion = ["identifica", "representa", "compara", "opera"]
    elif "plant" in idea_clean or "fotosíntes" in idea_clean or "alimenta" in idea_clean:
        conceptos_detectados = ["Plantas", "Nutrición vegetal", "Fotosíntesis", "Ciclo de vida"]
        verbos_accion = ["observa", "clasifica", "explica", "experimenta"]
    elif "agua" in idea_clean or "ciclo" in idea_clean or "evaporación" in idea_clean:
        conceptos_detectados = ["Ciclo del agua", "Estados del agua", "Evaporación", "Condensación"]
        verbos_accion = ["describe", "demuestra", "relaciona", "predice"]
    elif "lect" in idea_clean or "lectura" in idea_clean or "texto" in idea_clean:
        conceptos_detectados = ["Comprensión lectora", "Tipos de texto", "Inferencia"]
        verbos_accion = ["analiza", "interpreta", "sintetiza", "critica"]
    elif "escri" in idea_clean or "escritura" in idea_clean:
        conceptos_detectados = ["Producción textual", "Ortografía", "Coherencia"]
        verbos_accion = ["redacta", "organiza", "revisa", "mejora"]
    else:
        # Extracción genérica
        palabras = idea_clean.split()
        conceptos_detectados = [idea[:20].title() + "..."] if len(idea) > 20 else [idea.title()]
        verbos_accion = ["comprende", "aplica", "analiza", "evalúa"]
    
    return {
        "conceptos": conceptos_detectados,
        "verbos": verbos_accion,
        "idea_limpia": idea.strip()
    }

def generate_coherent_plan(idea, tramo, espacio, unidad, metodologia):
    """
    Genera un plan completamente coherente:
    Contenidos → Meta → Criterios de Logro (todo del mismo árbol conceptual)
    """
    if not idea.strip():
        return None
    
    # Extraer elementos de aprendizaje
    elementos = extract_learning_elements(idea, unidad, espacio)
    conceptos = elementos["conceptos"]
    verbos = elementos["verbos"]
    idea_clean = elementos["idea_limpia"]
    
    # CONTENIDOS (Qué enseñar)
    contenidos = [
        f"Conceptos clave: {', '.join(conceptos)}",
        f"Procedimientos: Observación, experimentación y análisis de {idea_clean}",
        f"Actitudes: Curiosidad, pensamiento crítico y disposición al aprendizaje colaborativo"
    ]
    
    # META DE APRENDIZAJE (Coherente con contenidos)
    # Estructura: [verbo + qué + para qué]
    verbo_principal = verbos[0] if verbos else "comprende"
    meta_aprendizaje = f"El estudiante {verbo_principal} los conceptos clave de '{idea_clean}' ({', '.join(conceptos[:2])}), aplicándolos en contextos significativos y demostrando pensamiento crítico mediante la participación activa en actividades de {metodologia}."
    
    # CRITERIOS DE LOGRO (Derivados coherentemente de la meta)
    # Cada criterio corresponde a un verbo de la Taxonomía de Bloom
    criterios_logro = [
        f"**Conocimiento:** Identifica y define correctamente los conceptos de {idea_clean} ({', '.join(conceptos[:1])}).",
        f"**Comprensión:** Explica cómo funcionan los elementos de {idea_clean} utilizando ejemplos del mundo real.",
        f"**Aplicación:** Aplica los conceptos aprendidos de {idea_clean} para resolver problemas nuevos o situaciones concretas.",
        f"**Análisis y Reflexión:** Analiza críticamente sus propios aprendizajes sobre {idea_clean} y propone mejoras en su proceso de aprendizaje."
    ]
    
    # Competencias alineadas
    competencias_mcn = {
        "Espacio Científico-Matemático": [
            "Pensamiento Científico: Formula preguntas, observa, experimenta y analiza evidencias.",
            "Resolución de Problemas: Aplica estrategias lógicas para resolver desafíos."
        ],
        "Espacio de Comunicación": [
            "Competencia Comunicativa: Expresa ideas con claridad y coherencia.",
            "Pensamiento Crítico: Interpreta y cuestiona mensajes diversos."
        ],
        "Espacio Creativo-Artístico": [
            "Pensamiento Creativo: Diseña e innova expresándose artísticamente.",
            "Lenguajes Estéticos: Codifica y decodifica mensajes a través del arte."
        ],
        "Espacio de Ciencias Sociales y Humanidades": [
            "Competencia Ciudadana: Actúa reflexiva y éticamente.",
            "Empatía y Diversidad: Valora perspectivas diferentes."
        ],
        "Espacio de Desarrollo Personal y Social": [
            "Autorregulación: Gestiona emociones y regula su comportamiento.",
            "Iniciativa Personal: Toma decisiones autónomas."
        ]
    }
    
    comps = competencias_mcn.get(espacio, ["Pensamiento Crítico", "Metacognición"])
    
    # Secuencia didáctica específica
    if metodologia == "Aprendizaje Basado en Proyectos (ABP)":
        inicio = f"**Lanzamiento del Reto (15 min):** Presenta un desafío real sobre '{idea_clean}'. Activa saberes previos sobre {', '.join(conceptos[:2])}. Organiza equipos heterogéneos de trabajo."
        desarrollo = f"**Investigación y Diseño (45 min):** Los equipos recopilan información sobre {idea_clean}, experimentan y diseñan soluciones. Registran hallazgos aplicando los conceptos de {conceptos[0] if conceptos else 'aprendizaje'}."
        cierre = f"**Presentación y Coevaluación (20 min):** Cada grupo expone sus resultados. Reflexionan sobre cómo aplicaron {', '.join(conceptos[:1])} en su proyecto."
    elif metodologia == "Indagación Científica y Experimentación":
        inicio = f"**Focalización (15 min):** Presenta un fenómeno intrigante sobre '{idea_clean}'. Recopila hipótesis de estudiantes sobre {conceptos[0] if conceptos else 'el tema'}."
        desarrollo = f"**Exploración y Experimentación (45 min):** Estudiantes prueban hipótesis mediante experimentos sobre '{idea_clean}'. Registran observaciones y descubren los conceptos de {', '.join(conceptos[:2])}."
        cierre = f"**Conclusiones Científicas (20 min):** Contrastan hipótesis con resultados. Elaboran conclusiones sobre '{idea_clean}' utilizando vocabulario científico."
    elif metodologia == "Gamificación Educativa":
        inicio = f"**Inmersión Narrativa (15 min):** Explica la misión lúdica sobre '{idea_clean}'. Presenta desafíos vinculados a {conceptos[0] if conceptos else 'aprendizaje'}. Establece sistema de puntuación."
        desarrollo = f"**Misiones Secuenciales (45 min):** Equipos superan retos que requieren aprender sobre '{idea_clean}'. Acumulan puntos al dominar conceptos de {', '.join(conceptos[:2])}."
        cierre = f"**Reflexión y Síntesis (20 min):** Celebran logros. Reflexionan sobre qué aprendieron de '{idea_clean}' y cómo lo aplicarían."
    else:  # Aprendizaje Cooperativo
        inicio = f"**Activación en Parejas (15 min):** Introduce '{idea_clean}' mediante lectura o video. Estructura 'Pensar-Compartir-Discutir' sobre {conceptos[0] if conceptos else 'el tema'}."
        desarrollo = f"**Trabajo Interdependiente (45 min):** Asigna roles en equipos. Cada miembro es responsable de una sección de '{idea_clean}'. Todos contribuyen al dominio de {', '.join(conceptos[:2])}."
        cierre = f"**Síntesis Grupal (20 min):** Cada equipo presenta síntesis. Destacan cómo cada miembro contribuyó a comprender '{idea_clean}'."

    return {
        "tramo": tramo,
        "espacio": espacio,
        "unidad": unidad,
        "metodologia": metodologia,
        "contenidos": contenidos,
        "meta": meta_aprendizaje,
        "competencias": comps,
        "criterios": criterios_logro,
        "inicio": inicio,
        "desarrollo": desarrollo,
        "cierre": cierre
    }

if st.button("✨ Generar Planificación Coherente", use_container_width=True):
    if not idea_docente.strip():
        st.error("⚠️ Introduce una idea antes de generar.")
    else:
        with st.spinner("Generando planificación coherente..."):
            plan = generate_coherent_plan(idea_docente, tramo, espacio, unidad_curricular, metodologia)
            
            st.success("🎉 ¡Planificación generada con coherencia total!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Tramo", plan['tramo'].split("(")[0].strip())
                st.metric("Unidad", plan['unidad'])
            with col2:
                st.metric("Espacio", plan['espacio'].split()[-1])
                st.metric("Metodología", plan['metodologia'].split("(")[0].strip())
            
            st.subheader("📚 Contenidos a Enseñar")
            for contenido in plan['contenidos']:
                st.write(f"• {contenido}")
            
            st.subheader("🎯 Competencias Priorizadas")
            for comp in plan['competencias']:
                st.write(f"✓ {comp}")
            
            st.subheader("🎓 Meta de Aprendizaje")
            st.info(f"📍 {plan['meta']}")
            
            st.subheader("🏆 Criterios de Logro (Coherentes con la Meta)")
            st.markdown("*Cada criterio evalúa un nivel diferente de aprendizaje (Taxonomía de Bloom):*")
            for i, crit in enumerate(plan['criterios'], 1):
                st.write(f"{i}. {crit}")
            
            st.info("✅ **Coherencia garantizada:** Contenidos → Meta → Criterios están alineados al mismo objetivo educativo")
            
            st.subheader("📐 Secuencia Didáctica")
            tab1, tab2, tab3 = st.tabs(["🚀 Inicio", "⚙️ Desarrollo", "🏆 Cierre"])
            with tab1:
                st.write(plan['inicio'])
            with tab2:
                st.write(plan['desarrollo'])
            with tab3:
                st.write(plan['cierre'])
            
            md_plan = f"""# Planificación EBI Coherente - DocenteXXI

## Datos Generales
- **Tramo:** {plan['tramo']}
- **Espacio:** {plan['espacio']}
- **Unidad Curricular:** {plan['unidad']}
- **Metodología:** {plan['metodologia']}

## Contenidos a Enseñar
{chr(10).join([f'- {c}' for c in plan['contenidos']])}

## Competencias Priorizadas
{chr(10).join([f'- {c}' for c in plan['competencias']])}

## Meta de Aprendizaje
{plan['meta']}

## Criterios de Logro (Alineados Coherentemente con la Meta)
{chr(10).join([f'{i+1}. {c}' for i, c in enumerate(plan['criterios'])])}

**Nota:** Cada criterio corresponde a un nivel de la Taxonomía de Bloom (Conocimiento → Comprensión → Aplicación → Análisis)

## Secuencia Didáctica

### Inicio
{plan['inicio']}

### Desarrollo
{plan['desarrollo']}

### Cierre
{plan['cierre']}

---
✅ Coherencia garantizada: Contenidos → Meta → Criterios alineados al mismo objetivo educativo

DocenteXXI © 2026-2027 | Ideas que brillan, aulas que inspiran
"""
            st.download_button(
                "📥 Descargar Planificación",
                md_plan,
                "planificacion-ebi-coherente.md",
                use_container_width=True
            )

st.divider()
st.caption("DocenteXXI © 2026-2027 | Ideas que brillan, aulas que inspiran")
