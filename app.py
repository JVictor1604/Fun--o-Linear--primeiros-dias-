import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random
import time

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Matemática para Lili",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS CUSTOMIZADOS ---
st.markdown("""
<style>
    html, body, [class*="st-"] {
        font-family: 'Helvetica', sans-serif;
    }
    .stButton>button {
        border-radius: 20px;
        border: 2px solid #FF4B4B;
        color: #FF4B4B;
        background-color: transparent;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        border-color: #FFFFFF;
        color: #FFFFFF;
        background-color: #FF4B4B;
    }
    h1, h2 {
        color: #2c3e50;
    }
    /* Estilo para os cartões de jogo */
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] {
        border: 1px solid #e6e6e6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: box-shadow 0.3s ease-in-out;
    }
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"]:hover {
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("Matemática para Lili")

with st.sidebar.expander("Menu de Navegação", expanded=True):
    st.markdown("### Um guia interativo sobre Funções Lineares")
    st.markdown("---")
    pagina_selecionada = st.sidebar.radio(
        "Escolha uma etapa:",
        ("Explicação Interativa", "Pratique com Jogos", "Revisão e Simulado")
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Para Lili 💖")
    st.sidebar.warning(
        """
        **Para a garota mais inteligente que conheço. Que esses estudos te lembre sempre da sua capacidade. Sempre vou estar com você! Eu te amo muito! ❤️**
        """
    )


# --- PÁGINAS DA APLICAÇÃO ---

def pagina_explicacao():
    st.title("📘 Desvendando a Função Linear")
    st.markdown("Uma função linear descreve uma relação de crescimento ou decrescimento **constante**. Sua principal característica é que o gráfico resultante é sempre uma **linha reta**.")
    st.markdown("---")

    with st.expander("🤔 Conceito de Função (Clique para expandir)"):
        st.write("""
        Uma função é uma regra matemática que estabelece uma relação entre dois conjuntos de valores. 
        Para cada valor de **entrada (variável independente)**, a função associa um único valor de **saída (variável dependente)**.

        **Exemplo Prático (Salário):**
        Imagine que um salário `s` é calculado com base nos dias `d` trabalhados.
        - A variável **independente** é o número de dias (`d`), pois é um valor que pode ser alterado.
        - A variável **dependente** é o salário (`s`), pois seu valor final *depende* do número de dias.

        Se a regra de cálculo for `s = 10 * d + 200`, temos uma função.
        """)

    st.header("✨ A Fórmula da Função Linear: `f(x) = ax + b`")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("O Coeficiente `a` (Coeficiente Angular)")
        st.info("""
        O coeficiente `a` multiplica a variável `x` e determina a **inclinação** da reta.
        - **Se `a` for positivo (`a > 0`):** A reta tem inclinação para cima, representando uma função **crescente**.
        - **Se `a` for negativo (`a < 0`):** A reta tem inclinação para baixo, representando uma função **decrescente**.
        - Quanto maior o valor absoluto de `a`, mais íngreme (vertical) é a inclinação da reta.
        """)

    with col2:
        st.subheader("O Coeficiente `b` (Coeficiente Linear)")
        st.warning("""
        O coeficiente `b` é o termo independente. Ele determina o ponto em que a reta **intercepta o Eixo y**.
        - Pode ser visto como o **ponto de partida** do gráfico.
        - A coordenada exata onde a reta cruza o Eixo y é sempre **(0, b)**.
        - Alterar `b` **desloca** a reta verticalmente (para cima ou para baixo), sem alterar sua inclinação.
        """)

    st.markdown("---")
    
    # NOVA SEÇÃO INTERATIVA
    st.header("❓ O que define o 'Primeiro Grau'?")
    st.markdown("A função é chamada de 'primeiro grau' porque a variável `x` está elevada à potência **1**. O que você acha que acontece com o gráfico se o expoente for diferente de 1? Teste no controle abaixo e observe a transformação.")

    exp_col1, exp_col2 = st.columns([1,2])
    with exp_col1:
        expoente = st.slider("Altere o expoente de x", 1.0, 3.0, 1.0, 0.1, key="expoente_slider")
        st.latex(f"f(x) = 2x^{{{expoente:.1f}}} - 1")
        st.write("Observe que, quando o expoente é 1.0, o gráfico é uma reta. Ao mudar o valor, ele se torna uma curva.")


    with exp_col2:
        x_exp = np.linspace(-10, 10, 400)
        # Lógica ajustada para lidar com expoentes não inteiros e bases negativas
        y_exp = 2 * (np.power(np.abs(x_exp), expoente) * np.sign(x_exp)) - 1
        
        fig_exp = go.Figure()
        fig_exp.add_trace(go.Scatter(x=x_exp, y=y_exp, mode='lines', name='Gráfico', line=dict(color='orange', width=4)))
        fig_exp.update_layout(
            title="A Transformação do Gráfico",
            xaxis=dict(range=[-10, 10], zeroline=True, zerolinewidth=1, zerolinecolor='black'),
            yaxis=dict(range=[-10, 10], zeroline=True, zerolinewidth=1, zerolinecolor='black'),
            plot_bgcolor='white',
            height=400
        )
        st.plotly_chart(fig_exp, use_container_width=True)
    st.markdown("---")


    st.header("🎨 Explore o Gráfico Interativo")
    st.markdown("Utilize os controles para alterar os valores de 'a' e 'b'. O que acontece com a inclinação da reta quando 'a' se aproxima de zero? E para onde o ponto de interceptação se move quando você altera 'b'?")

    interactive_col1, interactive_col2 = st.columns([1, 2])

    with interactive_col1:
        st.subheader("Controles do Gráfico")
        a = st.slider("Altere o valor de 'a' (inclinação)", -5.0, 5.0, 1.0, 0.1, key="slider_a")
        b = st.slider("Altere o valor de 'b' (ponto de partida)", -10.0, 10.0, 2.0, 0.5, key="slider_b")
        
        st.subheader("Função atual:")
        st.latex(f"f(x) = {a:.1f}x {'+' if b >= 0 else ''} {b:.1f}")

    with interactive_col2:
        x = np.linspace(-10, 10, 400)
        y = a * x + b
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'Reta f(x)', line=dict(color='mediumvioletred', width=4)))
        fig.add_trace(go.Scatter(x=[0], y=[b], mode='markers', name=f'Ponto (0, {b:.1f})', marker=dict(color='black', size=12, symbol='circle')))
        fig.update_layout(
            title="Gráfico da Função Linear",
            xaxis_title="<b>Eixo x</b> (variável independente)",
            yaxis_title="<b>Eixo y</b> (variável dependente)",
            xaxis=dict(range=[-10, 10], zeroline=True, zerolinewidth=2, zerolinecolor='black', showgrid=True, gridwidth=1, gridcolor='lightgrey'),
            yaxis=dict(range=[-10, 10], zeroline=True, zerolinewidth=2, zerolinecolor='black', showgrid=True, gridwidth=1, gridcolor='lightgrey'),
            plot_bgcolor='white',
            height=500,
            legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
        )
        st.plotly_chart(fig, use_container_width=True)

def pagina_jogos():
    st.title("🧠 Pratique com Jogos")
    
    if 'jogo_selecionado' not in st.session_state:
        st.session_state.jogo_selecionado = None
    
    if st.session_state.jogo_selecionado is None:
        menu_de_jogos()
    else:
        if st.session_state.jogo_selecionado == "Qual é a Função?":
            jogo_qual_a_funcao()
        elif st.session_state.jogo_selecionado == "Calculadora de Funções":
            jogo_calculadora_funcoes()
        elif st.session_state.jogo_selecionado == "Desafio do Ponto Zero (Raiz)":
            jogo_desafio_raiz()

def menu_de_jogos():
    st.markdown("A prática leva à perfeição. Escolha um dos jogos abaixo para aplicar seus conhecimentos.")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container():
            st.subheader("Qual é a Função?")
            st.write("Observe o gráfico e selecione a equação correta entre as opções. Um teste de reconhecimento visual!")
            if st.button("Jogar 'Qual é a Função?'", key="btn_jogo1"):
                st.session_state.jogo_selecionado = "Qual é a Função?"
                st.rerun()

    with col2:
        with st.container():
            st.subheader("Calculadora de Funções")
            st.write("Use a calculadora para criar uma função. Seu objetivo é fazer a reta passar por um ponto-alvo no gráfico.")
            if st.button("Jogar 'Calculadora de Funções'", key="btn_jogo2"):
                st.session_state.jogo_selecionado = "Calculadora de Funções"
                st.rerun()

    with col3:
        with st.container():
            st.subheader("Desafio do Ponto Zero")
            st.write("Encontre a raiz da função! Calcule o valor de 'x' onde a reta cruza o eixo x e teste sua precisão.")
            if st.button("Jogar 'Desafio do Ponto Zero'", key="btn_jogo3"):
                st.session_state.jogo_selecionado = "Desafio do Ponto Zero (Raiz)"
                st.rerun()

def jogo_qual_a_funcao():
    if st.button("⬅️ Voltar ao Menu de Jogos"):
        st.session_state.jogo_selecionado = None
        st.rerun()
    st.subheader("Jogo: Qual é a Função?")
    questoes = [
        {"a": 2, "b": 1, "resposta": "y = 2.0x + 1.0", "opcoes": ["y = 2.0x + 1.0", "y = 1.0x + 2.0", "y = -2.0x + 1.0"]},
        {"a": -1, "b": 3, "resposta": "y = -1.0x + 3.0", "opcoes": ["y = 1.0x - 3.0", "y = -1.0x + 3.0", "y = 3.0x - 1.0"]},
        {"a": 1, "b": 0, "resposta": "y = 1.0x", "opcoes": ["y = 1.0x", "y = x + 1.0", "y = 0.0"]},
        {"a": 3, "b": -2, "resposta": "y = 3.0x - 2.0", "opcoes": ["y = 2.0x - 3.0", "y = -3.0x - 2.0", "y = 3.0x - 2.0"]},
        {"a": -0.5, "b": -1, "resposta": "y = -0.5x - 1.0", "opcoes": ["y = -0.5x - 1.0", "y = 0.5x + 1.0", "y = -1.0x - 0.5"]},
    ]

    if 'game_started' not in st.session_state or not st.session_state.game_started:
        st.session_state.game_started = True
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.questions = random.sample(questoes, len(questoes))
        st.session_state.shuffled_options = random.sample(st.session_state.questions[0]['opcoes'], len(st.session_state.questions[0]['opcoes']))
        st.session_state.answered = False

    idx = st.session_state.current_question
    if idx < len(st.session_state.questions):
        q = st.session_state.questions[idx]
        
        st.progress((idx) / len(questoes), text=f"Questão {idx+1} de {len(questoes)}")

        col1, col2 = st.columns(2)
        with col1:
            x = np.linspace(-5, 5, 100)
            y = q['a'] * x + q['b']
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='royalblue', width=3)))
            # Destacando a interceptação em Y
            fig.add_trace(go.Scatter(x=[0], y=[q['b']], mode='markers', name=f'Intercepta Y em {q["b"]}', marker=dict(color='red', size=10, symbol='x')))
            fig.update_layout(
                title="Observe o gráfico:",
                xaxis=dict(range=[-5, 5], zeroline=True, zerolinewidth=2, zerolinecolor='black', showgrid=True, gridwidth=1, gridcolor='lightgrey'),
                yaxis=dict(range=[-5, 5], zeroline=True, zerolinewidth=2, zerolinecolor='black', showgrid=True, gridwidth=1, gridcolor='lightgrey'),
                plot_bgcolor='white',
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write("Qual das equações abaixo representa o gráfico ao lado?")
            
            escolha = st.radio("Escolha uma opção:", st.session_state.shuffled_options, key=f"q_{idx}", disabled=st.session_state.answered)
            
            if st.button("Confirmar Resposta", key=f"btn_{idx}", disabled=st.session_state.answered):
                st.session_state.answered = True
                if escolha == q["resposta"]:
                    st.success("Correto! 🎉")
                    st.session_state.score += 1
                else:
                    st.error(f"Incorreto. A resposta certa é: **{q['resposta']}**")
                st.rerun()

            if st.session_state.answered:
                if st.button("Próxima Questão"):
                    st.session_state.current_question += 1
                    if st.session_state.current_question < len(st.session_state.questions):
                         st.session_state.shuffled_options = random.sample(st.session_state.questions[st.session_state.current_question]['opcoes'], len(st.session_state.questions[st.session_state.current_question]['opcoes']))
                    st.session_state.answered = False
                    st.rerun()
    else:
        st.header("🎉 Fim de Jogo! 🎉")
        st.subheader(f"Sua pontuação final: {st.session_state.score} de {len(questoes)}")
        if st.session_state.score == len(questoes):
            st.balloons()
        if st.button("Jogar Novamente"):
            st.session_state.game_started = False
            st.rerun()

def jogo_calculadora_funcoes():
    if st.button("⬅️ Voltar ao Menu de Jogos"):
        st.session_state.jogo_selecionado = None
        st.rerun()
    st.subheader("Jogo: Calculadora de Funções")
    st.markdown("Seu desafio é determinar os coeficientes 'a' e 'b' de uma função linear que passe exatamente sobre o **ponto-alvo (estrela)** no gráfico.")

    if 'calc_game_started' not in st.session_state or not st.session_state.calc_game_started:
        st.session_state.calc_game_started = True
        st.session_state.target_x = random.choice([i for i in range(-4, 5) if i != 0])
        st.session_state.target_y = random.randint(-4, 4)
        st.session_state.user_a = 1.0
        st.session_state.user_b = 0.0

    target_x = st.session_state.target_x
    target_y = st.session_state.target_y

    calc_col1, calc_col2 = st.columns([1, 2])
    with calc_col1:
        st.subheader("Sua Calculadora")
        st.session_state.user_a = st.number_input("Valor de a:", value=st.session_state.user_a, step=0.1, format="%.1f")
        st.session_state.user_b = st.number_input("Valor de b:", value=st.session_state.user_b, step=0.1, format="%.1f")
        
        st.latex(f"y = {st.session_state.user_a:.1f}x + {st.session_state.user_b:.1f}")

        y_calculado = st.session_state.user_a * target_x + st.session_state.user_b
        if np.isclose(y_calculado, target_y):
            st.success("VOCÊ CONSEGUIU! A reta passou pelo ponto! 🎯")
            st.balloons()
            if st.button("Novo Desafio!"):
                st.session_state.target_x = random.choice([i for i in range(-4, 5) if i != 0])
                st.session_state.target_y = random.randint(-4, 4)
                st.rerun()
        else:
            st.info(f"Para x={target_x}, sua função resulta em y={y_calculado:.2f}. Tente chegar em y={target_y}!")


    with calc_col2:
        x = np.linspace(-5, 5, 100)
        y = st.session_state.user_a * x + st.session_state.user_b

        fig = go.Figure()
        # Reta do usuário
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Sua Reta', line=dict(color='mediumpurple', width=4)))
        # Ponto alvo
        fig.add_trace(go.Scatter(x=[target_x], y=[target_y], mode='markers', name='Ponto Alvo', marker=dict(color='red', size=15, symbol='star')))

        fig.update_layout(
            title="Ajuste a reta para passar pela estrela!",
            xaxis=dict(range=[-5, 5], zeroline=True, zerolinewidth=2, zerolinecolor='black'),
            yaxis=dict(range=[-5, 5], zeroline=True, zerolinewidth=2, zerolinecolor='black'),
            plot_bgcolor='white',
        )
        st.plotly_chart(fig, use_container_width=True)

def jogo_desafio_raiz():
    if st.button("⬅️ Voltar ao Menu de Jogos"):
        st.session_state.jogo_selecionado = None
        st.rerun()
    st.subheader("Jogo: Desafio do Ponto Zero (Raiz)")
    st.markdown("Sua missão é encontrar a **raiz** da função. A raiz é o valor de `x` onde a reta cruza o eixo x (ou seja, onde `y = 0`).")

    if 'raiz_game_started' not in st.session_state or not st.session_state.raiz_game_started:
        st.session_state.raiz_game_started = True
        a = random.choice([i for i in range(-4, 5) if i != 0])
        b = random.randint(-10, 10)
        st.session_state.raiz_a = a
        st.session_state.raiz_b = b
        st.session_state.raiz_correta = -b / a
        st.session_state.raiz_answered = False

    a = st.session_state.raiz_a
    b = st.session_state.raiz_b
    raiz_correta = st.session_state.raiz_correta

    raiz_col1, raiz_col2 = st.columns([1, 2])
    with raiz_col1:
        st.subheader("Função do Desafio:")
        st.latex(f"f(x) = {a}x {'+' if b >= 0 else ''} {b}")

        user_answer = st.number_input("Qual o valor da raiz (x)?", key="raiz_input", format="%.2f")

        if st.button("Verificar Raiz", disabled=st.session_state.raiz_answered):
            st.session_state.raiz_answered = True
            if np.isclose(user_answer, raiz_correta):
                st.success(f"Exato! A raiz é {raiz_correta:.2f}. Parabéns! ✅")
                st.balloons()
            else:
                st.error(f"Quase! A resposta correta é {raiz_correta:.2f}.")
            st.rerun()
        
        if st.session_state.raiz_answered:
            with st.expander("Ver cálculo da raiz"):
                st.markdown(f"""
                Para encontrar a raiz, igualamos a função a zero:
                1. `f(x) = 0`
                2. `{a}x {'+' if b >= 0 else ''} {b} = 0`
                3. `{a}x = {-b}`
                4. `x = {-b} / {a}`
                5. `x = {raiz_correta:.2f}`
                """)
            if st.button("Próximo Desafio"):
                st.session_state.raiz_game_started = False
                st.rerun()

    with raiz_col2:
        x = np.linspace(raiz_correta - 5, raiz_correta + 5, 100)
        y = a * x + b
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Função', line=dict(color='teal', width=3)))
        fig.add_trace(go.Scatter(x=[raiz_correta], y=[0], mode='markers', name='Raiz (Ponto Zero)', marker=dict(color='crimson', size=12, symbol='diamond')))
        fig.update_layout(
            title="Gráfico da Função e sua Raiz",
            xaxis=dict(zeroline=True, zerolinewidth=2, zerolinecolor='black', showgrid=True),
            yaxis=dict(zeroline=True, zerolinewidth=2, zerolinecolor='black', showgrid=True),
            plot_bgcolor='white',
        )
        st.plotly_chart(fig, use_container_width=True)

def pagina_simulado():
    st.title("✨ Revisão e Simulado")
    st.markdown("Vamos revisar e testar seus conhecimentos. Responda às questões a seguir para avaliar seu aprendizado.")
    st.markdown("---")
    
    questoes_simulado = [
        {
            "pergunta": "Uma corrida de táxi custa uma taxa fixa de R$ 5,00 (bandeirada) mais R$ 2,50 por quilômetro rodado (k). Qual função representa o preço (P) de uma corrida?",
            "opcoes": ["P(k) = 5k + 2.50", "P(k) = 5 + 2.50k", "P(k) = 7.50k", "P(k) = 2.50 - 5k"],
            "resposta": "P(k) = 5 + 2.50k",
            "explicacao": "O preço tem uma parte fixa (R$ 5,00), que é o coeficiente linear 'b', e uma parte que varia com os quilômetros (R$ 2,50 * k), que é o termo com o coeficiente angular 'a'."
        },
        {
            "pergunta": "O gráfico de uma função f(x) = -2x + 8 é uma reta. Em qual ponto essa reta corta o eixo y?",
            "opcoes": ["(0, 8)", "(4, 0)", "(0, -2)", "(8, 0)"],
            "resposta": "(0, 8)",
            "explicacao": "A reta corta o eixo y quando x=0. O coeficiente linear 'b' é 8, o que indica diretamente que o ponto de cruzamento com o eixo y é (0, 8)."
        },
        {
            "pergunta": "Qual é a raiz da função f(x) = 3x - 12? (Ou seja, qual valor de 'x' faz f(x) ser igual a zero?)",
            "opcoes": ["x = -12", "x = 3", "x = 4", "x = -4"],
            "resposta": "x = 4",
            "explicacao": "Para encontrar a raiz, igualamos a função a zero: 3x - 12 = 0. Somando 12 dos dois lados, temos 3x = 12. Dividindo por 3, encontramos x = 4."
        }
    ]

    if 'simulado_idx' not in st.session_state:
        st.session_state.simulado_idx = 0
        st.session_state.simulado_score = 0
        st.session_state.show_explanation = False

    idx = st.session_state.simulado_idx
    if idx < len(questoes_simulado):
        q = questoes_simulado[idx]
        st.subheader(f"Questão {idx + 1}")
        st.progress((idx) / len(questoes_simulado))
        st.write(q["pergunta"])
        
        escolha = st.radio("Escolha uma opção:", q["opcoes"], key=f"sim_{idx}", disabled=st.session_state.show_explanation)
        
        if not st.session_state.show_explanation:
            if st.button("Responder", key=f"btn_sim_{idx}"):
                st.session_state.show_explanation = True
                if escolha == q["resposta"]:
                    st.session_state.simulado_score += 1
                st.rerun()

        if st.session_state.show_explanation:
            if escolha == q['resposta']:
                st.success(f"Resposta Correta! {escolha}")
            else:
                st.error(f"Sua resposta: {escolha}. Resposta correta: {q['resposta']}")

            st.info(f"**Explicação:** {q['explicacao']}")
            if st.button("Próxima Questão"):
                st.session_state.simulado_idx += 1
                st.session_state.show_explanation = False
                st.rerun()
    else:
        st.header("Simulado Finalizado!")
        st.subheader(f"Sua pontuação: {st.session_state.simulado_score} de {len(questoes_simulado)}")
        if st.button("Refazer Simulado"):
            st.session_state.simulado_idx = 0
            st.session_state.simulado_score = 0
            st.session_state.show_explanation = False
            st.rerun()

# --- ROTEADOR DE PÁGINAS ---
if pagina_selecionada == "Explicação Interativa":
    pagina_explicacao()
elif pagina_selecionada == "Pratique com Jogos":
    pagina_jogos()
elif pagina_selecionada == "Revisão e Simulado":
    pagina_simulado()

