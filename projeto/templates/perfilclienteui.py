import streamlit as st
from service import Service
import time

class PerfilClienteUI:
    def cliente_main():
        st.header('Meus Dados')
        op = Service.cliente_listar_id(st.session_state['usuario_id'])
        st.write('Foto de perfil')
        st.image(op.get_foto(), width=150)
        foto = st.file_uploader('Nova foto', type=['png', 'jpg', 'jpeg'])
        nome = st.text_input('Informe o novo nome', op.get_nome())
        email = st.text_input('Informe o novo e-mail', op.get_email())
        fone = st.text_input('Informe o novo fone', op.get_fone())
        senha = st.text_input('Informe a nova senha', op.get_senha(), type='password')
        imagem = foto.getvalue() if foto else op.get_foto()
        if st.button('Atualizar'):
            try:
                id = op.get_id()
                Service.cliente_atualizar(id, nome, email, fone, senha, imagem)
                st.success('Cliente atualizado com sucesso')
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()