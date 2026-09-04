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
    
    competencias_mcn = {
        "Espacio Científico-Matemático": [
            "Pensamiento Científico: Formula preguntas, experimenta y analiza evidencias.",
            "Metacognición: Reflexiona sobre procesos de resolución de problemas."
        ],
        "Espacio de Comunicación": [
            "Competencia Comunicativa: Expresa ideas de forma oral, escrita y multimedia.",
            "Pensamiento Crítico: Interpreta y cuestiona mensajes de textos diversos."
        ],
        "Espacio Creativo-Artístico": [
            "Pensamiento Creativo: Diseña y se expresa artísticamente.",
            "Lenguajes Estéticos: Codifica y decodifica mensajes visuales."
        ],
        "Espacio de Ciencias Sociales y Humanidades": [
            "Competencia Ciudadana: Actúa reflexiva y éticamente ante problemas sociales.",
            "Relación con los Otros: Practica empatía y valora diversidad."
        ],
        "Espacio de Desarrollo Personal y Social": [
            "Intrapersonal: Gestiona emociones y regula esfuerzo.",
            "Iniciativa: Toma decisiones autónomas para el bienestar."
        ]
    }
    
    comps = competencias_mcn.get(espacio, ["Pensamiento Crítico", "Metacognición"])
    
    meta_aprendizaje = f"Que el estudiante comprenda '{idea_clean}' de forma vivencial, relacionándolo con su vida diaria aplicando competencias del {espacio}."
    
    criterios_logro = [
        f"Identifica y describe elementos clave de '{idea_clean}'.",
        f"Aplica estrategias de {metodologia} para resolver desafíos.",
        f"Reflexiona sobre su aprendizaje interactuando respetuosamente."
    ]
    
    if metodologia == "Aprendizaje Basado en Proyectos (ABP)":
        inicio = f"**Lanzamiento (15 min):** Presenta problema sobre '{idea_clean}'. Formula pregunta impulsora y organiza equipos."
        desarrollo = f"**Investigación (45 min):** Equipos recopilan info, experimentan y diseñan solución sobre '{idea_clean}'."
        cierre = f"**Difusión (20 min):** Grupos exponen hallazgos con coevaluación."
    elif metodologia == "Indagación Científica y Experimentación":
        inicio = f"**Focalización (15 min):** Presenta fenómeno sobre '{idea_clean}'. Registra hipótesis colectivas."
        desarrollo = f"**Exploración (45 min):** Estudiantes manipulan materiales y analizan datos de '{idea_clean}'."
        cierre = f"**Conclusión (20 min):** Contrastan hipótesis con resultados."
    elif metodologia == "Gamificación Educativa":
        inicio = f"**Inmersión (15 min):** Explica misión lúdica sobre '{idea_clean}'. Define reglas y roles."
        desarrollo = f"**Misión (45 min):** Equipos superan retos de aprendizaje secuenciales."
        cierre = f"**Recuento (20 min):** Celebra logros e identifica estrategias."
    else:
        inicio = f"**Activación (15 min):** Introduce '{idea_clean}' con Pensar-Compartir-Discutir en parejas."
        desarrollo = f"**Trabajo (45 min):** Asigna roles (coordinador, secretario, portavoz) en equipos."
        cierre = f"**Evaluación (20 min):** Síntesis grupal y metacognición."

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
                st.metric("Tramo", plan['tramo'].split("(")[0])
                st.metric("Espacio", plan['espacio'].split()[-1])
            with col2:
                st.metric("Unidad", plan['unidad'])
                st.metric("Metodología", plan['metodologia'].split("(")[0])
            
            st.subheader("🎯 Competencias Priorizadas")
            for comp in plan['competencias']:
                st.write(f"✓ {comp}")
            
            st.subheader("🎓 Meta de Aprendizaje")
            st.info(plan['meta'])
            
            st.subheader("🏆 Criterios de Logro")
            for crit in plan['criterios']:
                st.write(f"✅ {crit}")
            
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
- Tramo: {plan['tramo']}
- Espacio: {plan['espacio']}
- Unidad: {plan['unidad']}
- Metodología: {plan['metodologia']}

## Competencias
{chr(10).join([f'- {c}' for c in plan['competencias']])}

## Meta
{plan['meta']}

## Criterios
{chr(10).join([f'- {c}' for c in plan['criterios']])}

## Secuencia

### Inicio
{plan['inicio']}

### Desarrollo
{plan['desarrollo']}

### Cierre
{plan['cierre']}

---
DocenteXXI © 2026-2027
"""
            st.download_button(
                "📥 Descargar Planificación",
                md_plan,
                "planificacion.md",
                use_container_width=True
            )

st.divider()
st.caption("DocenteXXI © 2026-2027 | Ideas que brillan, aulas que inspiran")
