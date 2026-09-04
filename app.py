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
st.markdown("Diseña secuencias didácticas completas por competencias a partir de una idea inicial.")

st.subheader("💡 ¿Qué quieres enseñar hoy?")

idea_docente = st.text_area(
    "Tu idea para la clase:",
    placeholder="Ej: Enseñar cómo se alimentan las plantas, aprender fracciones dividiendo pizza...",
    height=100,
    label_visibility="collapsed"
)

def generate_ebi_plan(idea, tramo, espacio, unidad, metodologia):
    if not idea.strip():
        return None
        
    idea_clean = idea.strip()
    
    # Competencias alineadas a cada espacio
    competencias_mcn = {
        "Espacio Científico-Matemático": [
            "Pensamiento Científico: Formula preguntas, observa, experimenta y analiza evidencias.",
            "Resolución de Problemas: Aplica estrategias lógicas y matemáticas para resolver desafíos."
        ],
        "Espacio de Comunicación": [
            "Competencia Comunicativa: Expresa ideas de forma oral, escrita y multimedia con claridad.",
            "Pensamiento Crítico: Interpreta y cuestiona mensajes de textos diversos."
        ],
        "Espacio Creativo-Artístico": [
            "Pensamiento Creativo: Diseña, innova y se expresa artísticamente.",
            "Lenguajes Estéticos: Codifica y decodifica mensajes a través del arte."
        ],
        "Espacio de Ciencias Sociales y Humanidades": [
            "Competencia Ciudadana: Actúa reflexiva y éticamente ante problemas sociales.",
            "Empatía y Diversidad: Valora perspectivas diferentes y practica la inclusión."
        ],
        "Espacio de Desarrollo Personal y Social": [
            "Autorregulación: Gestiona emociones y regula su comportamiento.",
            "Iniciativa Personal: Toma decisiones autónomas para el bienestar propio y colectivo."
        ]
    }
    
    comps = competencias_mcn.get(espacio, ["Pensamiento Crítico", "Metacognición"])
    
    # META DE APRENDIZAJE: Específica, medible y alineada al contenido
    meta_aprendizaje = f"El estudiante comprenderá '{idea_clean}' de manera vivencial y reflexiva, identificando sus elementos clave, aplicando estrategias de {metodologia}, y demostrando comprensión a través de su participación activa en la secuencia didáctica."
    
    # CRITERIOS DE LOGRO: Derivados directamente de la meta
    criterios_logro = [
        f"Identifica y explica los elementos esenciales de '{idea_clean}' utilizando vocabulario apropiado.",
        f"Analiza '{idea_clean}' en contextos reales y establece conexiones con su vida cotidiana.",
        f"Participa activamente en las actividades de {metodologia}, colaborando y respetando a sus compañeros.",
        f"Demuestra reflexión sobre su propio aprendizaje de '{idea_clean}' a través de la evaluación formativa."
    ]
    
    # Secuencia didáctica según metodología
    if metodologia == "Aprendizaje Basado en Proyectos (ABP)":
        inicio = f"**Lanzamiento del Reto (15 min):** Presenta a los estudiantes un problema o desafío real relacionado con '{idea_clean}'. Activa saberes previos con preguntas impulsoras. Organiza el aula en pequeños equipos de trabajo heterogéneos."
        desarrollo = f"**Investigación y Prototipado (45 min):** Los equipos recopilan información sobre '{idea_clean}', experimentan con recursos disponibles y diseñan una solución o producto. El docente actúa como facilitador, orientando sin resolver el problema."
        cierre = f"**Presentación y Coevaluación (20 min):** Cada grupo expone brevemente su solución. Realizan coevaluación usando rúbrica compartida. Se reflexiona sobre procesos y aprendizajes."
    elif metodologia == "Indagación Científica y Experimentación":
        inicio = f"**Focalización (15 min):** Presenta un fenómeno intrigante sobre '{idea_clean}'. Promueve la observación directa y recopila hipótesis de los estudiantes. Registra predicciones colectivas."
        desarrollo = f"**Exploración (45 min):** Estudiantes manipulan materiales concretos o analizan datos para comprobar hipótesis sobre '{idea_clean}'. Registran observaciones y buscan patrones. Docente guía el pensamiento científico con preguntas."
        cierre = f"**Conclusión y Reflexión (20 min):** Contrastan hipótesis iniciales con resultados. Elaboran conclusiones científicas sobre '{idea_clean}'. Reflexionan sobre el proceso de investigación."
    elif metodologia == "Gamificación Educativa":
        inicio = f"**Inmersión Narrativa (15 min):** Explica la misión lúdica o desafío del día vinculado a '{idea_clean}'. Presenta reglas claras, roles de equipos y sistema de puntuación. Crea entusiasmo y motivación."
        desarrollo = f"**Misiones y Retos (45 min):** Equipos superan desafíos secuenciales de aprendizaje sobre '{idea_clean}'. Acumulan puntos y avanzan de niveles. Se promueve perseverancia ante errores y trabajo colaborativo."
        cierre = f"**Recuento y Metacognición (20 min):** Anuncia ganadores y celebra logros de todos. Reflexionan sobre estrategias que los ayudaron a aprender '{idea_clean}'. Conexión del aprendizaje lúdico con contenidos académicos."
    else:  # Aprendizaje Cooperativo
        inicio = f"**Activación en Parejas (15 min):** Introduce '{idea_clean}' mediante lectura, imagen o video breve. Aplica estructura 'Pensar-Compartir-Discutir' en parejas. Cada pareja comparte su perspectiva inicial."
        desarrollo = f"**Trabajo Interdependiente (45 min):** Asigna roles específicos en equipos (coordinador, secretario, portavoz, gestor de tiempo). Cada miembro es responsable de una sección del aprendizaje. Todos contribuyen para el éxito del equipo sobre '{idea_clean}'."
        cierre = f"**Síntesis Grupal (20 min):** Cada equipo presenta síntesis de su trabajo. Docente destaca contribuciones individuales. Metacognición: ¿Cómo funcionó el equipo? ¿Qué aprendimos de '{idea_clean}'?"

    return {
        "tramo": tramo,
        "espacio": espacio,
        "unidad": unidad,
        "metodologia": metodologia,
        "meta": meta_aprendizaje,
        "competencias": comps,
        "criterios": criterios_logro,
        "inicio": inicio,
        "desarrollo": desarrollo,
        "cierre": cierre
    }

if st.button("✨ Generar Planificación", use_container_width=True):
    if not idea_docente.strip():
        st.error("⚠️ Introduce una idea antes de generar.")
    else:
        with st.spinner("Generando planificación..."):
            plan = generate_ebi_plan(idea_docente, tramo, espacio, unidad_curricular, metodologia)
            
            st.success("🎉 ¡Planificación lista!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Tramo", plan['tramo'].split("(")[0].strip())
                st.metric("Unidad", plan['unidad'])
            with col2:
                st.metric("Espacio", plan['espacio'].split()[-1])
                st.metric("Metodología", plan['metodologia'].split("(")[0].strip())
            
            st.subheader("🎯 Competencias Priorizadas")
            for comp in plan['competencias']:
                st.write(f"✓ {comp}")
            
            st.subheader("🎓 Meta de Aprendizaje")
            st.info(plan['meta'])
            
            st.subheader("🏆 Criterios de Logro")
            st.markdown("*Alineados directamente con la meta de aprendizaje:*")
            for i, crit in enumerate(plan['criterios'], 1):
                st.write(f"{i}. {crit}")
            
            st.subheader("📐 Secuencia Didáctica")
            tab1, tab2, tab3 = st.tabs(["🚀 Inicio", "⚙️ Desarrollo", "🏆 Cierre"])
            with tab1:
                st.write(plan['inicio'])
            with tab2:
                st.write(plan['desarrollo'])
            with tab3:
                st.write(plan['cierre'])
            
            md_plan = f"""# Planificación EBI - DocenteXXI

## Datos Generales
- **Tramo:** {plan['tramo']}
- **Espacio:** {plan['espacio']}
- **Unidad Curricular:** {plan['unidad']}
- **Metodología:** {plan['metodologia']}

## Competencias Priorizadas
{chr(10).join([f'- {c}' for c in plan['competencias']])}

## Meta de Aprendizaje
{plan['meta']}

## Criterios de Logro (Alineados con la Meta)
{chr(10).join([f'{i+1}. {c}' for i, c in enumerate(plan['criterios'])])}

## Secuencia Didáctica

### Inicio
{plan['inicio']}

### Desarrollo
{plan['desarrollo']}

### Cierre
{plan['cierre']}

---
DocenteXXI © 2026-2027 | Ideas que brillan, aulas que inspiran
"""
            st.download_button(
                "📥 Descargar Planificación",
                md_plan,
                "planificacion-ebi.md",
                use_container_width=True
            )

st.divider()
st.caption("DocenteXXI © 2026-2027 | Ideas que brillan, aulas que inspiran")
