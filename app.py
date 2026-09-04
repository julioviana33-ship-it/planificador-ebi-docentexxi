import streamlit as st
import random

# Configuration and Theme Styling matching DocenteXXI Brand Identity
st.set_page_config(
    page_title="Planificador EBI Inteligente - DocenteXXI",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for DocenteXXI Branding
st.markdown("""
<style>
    /* Brand Colors */
    :root {
        --navy: #0D2240;
        --teal: #1BA098;
        --gold: #F2B824;
        --light-bg: #F4F7F6;
    }
    
    /* Global styles */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Header & Branding */
    .brand-title {
        color: #0D2240;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 800;
        font-size: 2.5rem;
        margin-bottom: 0px;
    }
    .brand-tagline {
        color: #1BA098;
        font-family: 'Georgia', serif;
        font-style: italic;
        font-size: 1.1rem;
        margin-top: -5px;
        margin-bottom: 25px;
    }
    
    /* Sidebar styling */
    .sidebar-logo-text {
        color: #F2B824;
        font-weight: bold;
        font-size: 1.5rem;
        text-align: center;
        margin-bottom: 10px;
    }
    
    /* Box treatments */
    .ebi-card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        border-left: 6px solid #1BA098;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    .premium-box {
        background-color: #0D2240;
        color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 6px solid #F2B824;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #1BA098 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px 24px !important;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1) !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        background-color: #0D2240 !important;
        box-shadow: 0 5px 12px rgba(0,0,0,0.2) !important;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR BRANDING & CONFIGURATION -----------------
with st.sidebar:
    st.markdown("<div class='sidebar-logo-text'>📖 DocenteXXI 🌟</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; color: #E2E8F0; margin-top: -10px;'>\"Ideas que brillan, aulas que inspiran\"</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.header("⚙️ Configuración EBI")
    
    # Selection of EBI Tramos (Educación Básica Integrada)
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
    
    # Selection of Espacio de Aprendizaje
    espacio = st.selectbox(
        "Espacio del Conocimiento / Aprendizaje:",
        options=[
            "Espacio Científico-Matemático",
            "Espacio de Comunicación",
            "Espacio Creativo-Artístico",
            "Espacio de Ciencias Sociales y Humanidades",
            "Espacio de Desarrollo Personal y Social"
        ],
        index=0
    )
    
    # Dynamic Subjects based on Espacio
    subjects_map = {
        "Espacio Científico-Matemático": ["Matemática", "Ciencias de la Naturaleza (Biología/Física/Química)", "Pensamiento Computacional"],
        "Espacio de Comunicación": ["Lengua Española", "Segunda Lengua / Inglés", "Literatura"],
        "Espacio Creativo-Artístico": ["Artes Visuales y Plásticas", "Expresión Corporal y Teatro", "Música"],
        "Espacio de Ciencias Sociales y Humanidades": ["Ciencias Sociales (Geografía/Historia)", "Formación Ciudadana y Ética"],
        "Espacio de Desarrollo Personal y Social": ["Educación Física", "Educación Socioemocional", "Taller de Iniciativa Emprendedora"]
    }
    
    unidad_curricular = st.selectbox(
        "Unidad Curricular:",
        options=subjects_map[espacio]
    )
    
    # Selecting Metodologías Activas for the sequence
    metodologia = st.selectbox(
        "Enfoque Metodológico Principal:",
        options=[
            "Aprendizaje Basado en Proyectos (ABP)",
            "Indagación Científica y Experimentación",
            "Gamificación Educativa",
            "Aprendizaje Cooperativo"
        ]
    )
    
    st.markdown("---")
    st.markdown("### 🔒 Acceso Premium")
    st.info("Desbloquea exportaciones en Word editable (.docx) y accede a un catálogo de 22 temarios completos y simulacros oficiales 2026-2027.")

# ----------------- MAIN APP HEADER -----------------
st.markdown("<h1 class='brand-title'>Planificador EBI Inteligente</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-tagline'>Diseña secuencias didácticas completas por competencias a partir de una sola idea inicial.</p>", unsafe_allow_html=True)

# ----------------- MAIN INPUT PANEL -----------------
st.markdown("### 💡 ¿Qué quieres enseñar hoy?")
st.markdown("Escribe una idea simple, un tema cotidiano, un recurso o una inquietud de tus alumnos. La app lo transformará en una planificación completa alineada con todos los marcos de la Educación Básica Integrada (EBI).")

idea_docente = st.text_area(
    "Tu idea para la clase:",
    placeholder="Ej: Quiero enseñar cómo se alimentan las plantas usando hojas del patio, o aprender a usar las fracciones dividiendo una pizza, o las reglas de convivencia con un juego...",
    height=100
)

# ----------------- DETERMINISTIC PLANNING ENGINE -----------------
def generate_ebi_plan(idea, tramo, espacio, unidad, metodologia):
    if not idea.strip():
        return None
        
    # Standardize input for templates
    idea_clean = idea.strip()
    
    # Select default EBI Competences based on Espacio
    competencias_mcn = {
        "Espacio Científico-Matemático": [
            "Competencia en Pensamiento Científico: Formula preguntas, experimenta y analiza evidencias de su entorno.",
            "Competencia Metacognitiva: Reflexiona sobre sus propios procesos de resolución de problemas numéricos y de lógica."
        ],
        "Espacio de Comunicación": [
            "Competencia Comunicativa: Expresa ideas, sentimientos y saberes de forma oral, escrita y multimedia.",
            "Competencia en Pensamiento Crítico: Interpreta y cuestiona mensajes de diversos textos y contextos."
        ],
        "Espacio Creativo-Artístico": [
            "Competencia en Pensamiento Creativo: Diseña, reinventa y se expresa artísticamente combinando múltiples lenguajes.",
            "Competencia Comunicativa (Artística): Codifica y decodifica lenguajes estéticos."
        ],
        "Espacio de Ciencias Sociales y Humanidades": [
            "Competencia Ciudadana: Actúa de forma reflexiva y ética ante problemas sociales y comunitarios de su entorno.",
            "Competencia de Relación con los Otros: Practica la empatía y valora la diversidad sociocultural."
        ],
        "Espacio de Desarrollo Personal y Social": [
            "Competencia Intrapersonal: Reconoce y gestiona sus propias emociones, regulando su esfuerzo y resiliencia.",
            "Competencia de Iniciativa y Orientación a la Acción: Toma decisiones autónomas para el bienestar personal y colectivo."
        ]
    }
    
    comps = competencias_mcn.get(espacio, [
        "Competencia Pensamiento Crítico: Analiza y evalúa diferentes perspectivas.",
        "Competencia Metacognitiva: Reconoce su forma de aprender."
    ])
    
    # Generate pedagogical components dynamically
    meta_aprendizaje = f"Que el estudiante logre comprender, de manera vivencial y reflexiva, el concepto de '{idea_clean}' a través del análisis activo, relacionándolo con su vida diaria y aplicando competencias del {espacio}."
    
    criterios_logro = [
        f"Identifica y describe con claridad los elementos esenciales relacionados con '{idea_clean}' utilizando terminología adecuada para el {tramo}.",
        f"Aplica las estrategias planteadas por la metodología de {metodologia} para resolver situaciones y desafíos prácticos.",
        f"Reflexiona críticamente sobre su propio proceso de aprendizaje e interactúa respetuosamente con sus pares durante las actividades colectivas."
    ]
    
    # Generate Didactic Sequence based on Metodologia & Idea
    if metodologia == "Aprendizaje Basado en Proyectos (ABP)":
        inicio_desc = f"**Lanzamiento del Reto (15 min):** Se presenta a los estudiantes un problema motivador basado en '{idea_clean}'. El docente formula una *pregunta impulsora* para despertar la curiosidad y activar saberes previos. Se organiza el aula en pequeños equipos de trabajo."
        desarrollo_desc = f"**Investigación y Creación (45 min):** Los equipos recopilan información, experimentan y diseñan una solución o producto intermedio relacionado de forma directa con la idea propuesta. El docente actúa como mediador y facilitador de recursos pedagógicos."
        cierre_desc = f"**Difusión del Producto (20 min):** Los grupos exponen brevemente sus hallazgos o prototipo al resto de la clase. Se promueve la coevaluación y la valoración del esfuerzo grupal utilizando una rúbrica compartida."
    elif metodologia == "Indagación Científica y Experimentación":
        inicio_desc = f"**Focalización (15 min):** Se coloca a los estudiantes frente a un fenómeno intrigante derivado de '{idea_clean}'. Se promueve la observación directa y se les motiva a plantear hipótesis de manera colectiva anotándolas en la pizarra."
        desarrollo_desc = f"**Exploración y Contraste (45 min):** Los estudiantes manipulan materiales reales o analizan datos concretos para comprobar sus hipótesis. El docente guía el registro de datos e incentiva la argumentación con base en evidencias."
        cierre_desc = f"**Reflexión y Conclusión (20 min):** Se contrastan las hipótesis iniciales con los resultados experimentales obtenidos. Los alumnos elaboran una conclusión compartida y sintetizan qué aprendieron sobre el fenómeno."
    elif metodologia == "Gamificación Educativa":
        inicio_desc = f"**Inmersión en la Narrativa (15 min):** Se explica a los estudiantes la misión lúdica o desafío del día vinculado a '{idea_clean}'. Se presentan las reglas del juego, los roles de cada equipo y el tablero o sistema de puntaje/recompensas."
        desarrollo_desc = f"**Misión Activa (45 min):** Los equipos superan retos o 'misiones' de aprendizaje secuenciales diseñadas para practicar contenidos curriculares específicos. Se promueve la perseverancia al error y el trabajo colaborativo en tiempo real."
        cierre_desc = f"**Consolidación y Recuento (20 min):** Se realiza el recuento de los logros de la misión y se felicita el esfuerzo de todos los equipos. Los estudiantes identifican qué estrategias del juego les ayudaron a comprender mejor el tema pedagógico."
    else: # Aprendizaje Cooperativo
        inicio_desc = f"**Activación en Parejas (15 min):** Se introduce '{idea_clean}' a través de una breve lectura, imagen o pregunta. Se aplica la estructura de 'Pensar-Compartir-Discutir' para que cada pareja consolide una primera perspectiva del tema."
        desarrollo_desc = f"**Trabajo Interdependiente (45 min):** Se asignan roles específicos dentro de los equipos (coordinador, secretario, portavoz, gestor del tiempo). Cada miembro es responsable de una sección del reto de aprendizaje, asegurando la participación de todos."
        cierre_desc = f"**Evaluación Grupal (20 min):** Los equipos entregan una síntesis colectiva de su trabajo. Se dedica un espacio de metacognición donde evalúan cómo funcionó su equipo y qué compromiso asumen para la siguiente sesión."

    # Generate custom exit ticket recommendation based on the idea
    exit_ticket_idea = f"**Ticket 3-2-1 personalizado para '{idea_clean}':**\n" \
                       f"- **3** Conceptos clave que descubriste sobre '{idea_clean}' hoy.\n" \
                       f"- **2** Formas en que puedes observar o aplicar esto fuera del salón de clases.\n" \
                       f"- **1** Pregunta que aún te queda flotando en la cabeza."

    return {
        "tramo": tramo,
        "espacio": espacio,
        "unidad": unidad,
        "metodologia": metodologia,
        "meta": meta_aprendizaje,
        "competencias": comps,
        "criterios": criterios_logro,
        "secuencia": {
            "inicio": inicio_desc,
            "desarrollo": desarrollo_desc,
            "cierre": cierre_desc
        },
        "exit_ticket": exit_ticket_idea
    }

# ----------------- INTERACTIVE USER ACTION -----------------
if st.button("✨ Generar Planificación de Aula EBI"):
    if not idea_docente.strip():
        st.error("⚠️ Por favor, introduce una idea sobre lo que quieres enseñar hoy en el cuadro de texto superior.")
    else:
        with st.spinner("Generando planificación alineada a los marcos pedagógicos EBI..."):
            plan = generate_ebi_plan(idea_docente, tramo, espacio, unidad_curricular, metodologia)
            
            # Displays generated content beautifully
            st.success("🎉 ¡Planificación generada con éxito! Revisa todos los componentes pedagógicos a continuación:")
            
            # 1. General Metadata block
            st.markdown(f"""
            <div class='ebi-card'>
                <h3 style='color: #0D2240; margin-top:0px;'>📋 Datos Generales EBI</h3>
                <p><strong>Nivel / Tramo:</strong> {plan['tramo']}</p>
                <p><strong>Espacio del Conocimiento:</strong> {plan['espacio']}</p>
                <p><strong>Unidad Curricular:</strong> {plan['unidad']}</p>
                <p><strong>Metodología Activa:</strong> {plan['metodologia']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # 2. Curricular Alignment block
            st.markdown("### 🎯 Alineación Curricular por Competencias (MCN)")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### Competencias Generales EBI Priorizadas:")
                for comp in plan['competencias']:
                    st.markdown(f"- **{comp.split(':')[0]}**:{comp.split(':')[1]}")
            with col2:
                st.markdown("#### Meta de Aprendizaje:")
                st.info(plan['meta'])
                
            # 3. Assessment Criteria block
            st.markdown("### 🏆 Criterios de Logro / Evaluación")
            for crit in plan['criterios']:
                st.markdown(f"✅ *{crit}*")
                
            # 4. Three-Moment Didactic Sequence block
            st.markdown("### 📐 Secuencia Didáctica Progresiva")
            t_inicio, t_desarrollo, t_cierre = st.tabs(["🚀 Inicio", "⚙️ Desarrollo", "🏆 Cierre"])
            with t_inicio:
                st.markdown(plan['secuencia']['inicio'])
            with t_desarrollo:
                st.markdown(plan['secuencia']['desarrollo'])
            with t_cierre:
                st.markdown(plan['secuencia']['cierre'])
                
            # 5. Formative Assessment / Exit Ticket block
            st.markdown("### 🎫 Evaluación Formativa: Boleto de Salida (Exit Ticket)")
            st.markdown("Utiliza esta herramienta interactiva en los últimos 5 minutos de la clase para recoger evidencias de aprendizaje de manera lúdica:")
            st.code(plan['exit_ticket'], language="markdown")
            
            # 6. Call to Action / Export & Monetization Panel
            st.markdown("""
            <div class='premium-box'>
                <h3 style='color: #F2B824; margin-top:0px;'>💎 ¡Lleva esta planificación al siguiente nivel pedagógico!</h3>
                <p>¿Quieres descargar esta planificación en un documento de <strong>Word (.docx) 100% editable</strong> con formato institucional de DocenteXXI, o necesitas adaptarla para tu nivel específico?</p>
                <p>Los miembros <strong>Premium de DocenteXXI</strong> tienen acceso ilimitado a:</p>
                <ul>
                    <li>Descarga ilimitada de planificaciones editables por competencias.</li>
                    <li>Acceso al catálogo oficial de 22 temarios para el Concurso Docente 2026-2027.</li>
                    <li>Soporte y asesoría pedagógica directa por WhatsApp.</li>
                </ul>
                <a href='https://wa.me/message/DOCENTEXXI?text=Hola%20DocenteXXI%20🌟%20Quiero%20mi%20Planificación%20en%20formato%20Word%20editable%20y%20conocer%20la%20Suscripción%20Premium' target='_blank'>
                    <button style='background-color: #F2B824; color: #0D2240; font-weight: bold; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer;'>
                        📥 Exportar en Word Editable (.docx) por WhatsApp
                    </button>
                </a>
            </div>
            """, unsafe_allow_html=True)
            
            # Allow raw markdown download locally as free feature
            md_plan = f"""# Planificación de Aula EBI - DocenteXXI
            
## Datos Generales
* **Tramo EBI:** {plan['tramo']}
* **Espacio:** {plan['espacio']}
* **Unidad Curricular:** {plan['unidad']}
* **Metodología:** {plan['metodologia']}

## Competencias Priorizadas
{chr(10).join([f'* {c}' for c in plan['competencias']])}

## Meta de Aprendizaje
{plan['meta']}

## Criterios de Evaluación / Logro
{chr(10).join([f'* {c}' for c in plan['criterios']])}

## Secuencia Didáctica
### Inicio
{plan['secuencia']['inicio']}

### Desarrollo
{plan['secuencia']['desarrollo']}

### Cierre
{plan['secuencia']['cierre']}

## Evaluación Formativa (Exit Ticket)
{plan['exit_ticket']}

---
Generado por DocenteXXI - "Ideas que brillan, aulas que inspiran" © 2026-2027
"""
            st.download_button(
                label="📥 Descargar Planificación en Markdown (Gratuito)",
                data=md_plan,
                file_name="planificacion-ebi-docentexxi.md",
                mime="text/markdown"
            )

# ----------------- FOOTER -----------------
st.markdown("---")
st.markdown("<p style='text-align: center; color: #718096; font-size: 0.9rem;'>DocenteXXI © 2026-2027 | Creando ideas que brillan para aulas que inspiran. Todos los derechos reservados.</p>", unsafe_allow_html=True)
