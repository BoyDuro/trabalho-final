import streamlit as st
from service import Service
import time

class PerfilProfissionalUI:
    def profissional_main():
        st.header('Meus Dados')
        op = Service.profissional_listar_id(st.session_state['usuario_id'])
        st.write('Foto de perfil')
        st.image(op.get_foto())
        foto = st.file_uploader('Nova foto', type=['png', 'jpg', 'jpeg'])
        nome = st.text_input('Informe o novo nome', op.get_nome())
        email = st.text_input('Informe o novo e-mail', op.get_email())
        especialidade = st.text_input('Informe a nova especialidade', op.get_especialidade())
        senha = st.text_input('Informe a nova senha', op.get_senha(), type='password')
        imagem = foto.getvalue() if foto else op.get_foto()
        if st.button('Atualizar'): 
            try:
                id = op.get_id()
                Service.profissional_atualizar(id, nome, email, especialidade, senha, imagem)
                st.success('Profissional atualizado com sucesso')
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()