# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:26:35 2025

@author: HP
"""
import streamlit as st
import random
import time
import pandas as pd

# Initialisation des listes dans l'état de session
if "clients" not in st.session_state:
    st.session_state.clients = [
        {"Nom": "Mahdi Salah Doubeh", "Numéro": "77631405"},
        {"Nom": "Amin Hassan Doualeh", "Numéro": "77049495"},
        {"Nom": "Amal Abdourahman Abib", "Numéro": "77653929"},
        {"Nom": "Djibril Djama Obsieh", "Numéro": "77132436"},
        {"Nom": "Ayan Abdi Ali", "Numéro": "77037454"},
        {"Nom": "Abdillahi Omar Dirieh", "Numéro": "77825892"},
        {"Nom": "Ayan Douksieh Abdi", "Numéro": "77287792"},
        {"Nom": "Abdourahman Abdoulhakim Med", "Numéro": "77657470"},
        {"Nom": "Abdourahman Omar Assoweh", "Numéro": "77855034"},
        {"Nom": "Moussa Farah Iyeh", "Numéro": "77876903"},
        {"Nom": "Fathia Ismael Hassan", "Numéro": "77884664"},
        {"Nom": "Elmi Ahmed Abdi", "Numéro": "77826904"},
        {"Nom": "Hibo Mahamoud Abdillahi ", "Numéro": "77812815"},
        {"Nom": "Fozzi Ali Batoun", "Numéro": "77825921"},
        {"Nom": "Abdoulfatah Moussa Doualeh", "Numéro": "77219582"},
        {"Nom": "Hodan Abdi Osman", "Numéro": "77115632"},
        {"Nom": "Sami", "Numéro": "77206755"},
    ]

if "gagnants" not in st.session_state:
    st.session_state.gagnants = []

if "dernier_gagnant" not in st.session_state:
    st.session_state.dernier_gagnant = None

st.title("🎲 Tirage au sort des clients")

# 🔹 Organisation en deux colonnes
col1, col2 = st.columns(2)

# 🟢 Clients restants
with col1:
    st.subheader("📜 Clients dans l'urne")
    if st.session_state.clients:
        df_clients = pd.DataFrame(st.session_state.clients)
        st.dataframe(df_clients, use_container_width=True)
    else:
        st.write("✅ Tous les clients ont été tirés !")

# 🏆 Gagnants
with col2:
    st.subheader("🏅 Gagnants")
    if st.session_state.gagnants:
        df_gagnants = pd.DataFrame(st.session_state.gagnants)
        st.dataframe(df_gagnants, use_container_width=True)
    else:
        st.write("Aucun gagnant pour l'instant.")

# Bouton pour tirer un numéro
if st.button("🎯 Tirer un client"):
    if st.session_state.clients:
        with st.spinner("Tirage en cours... 🎰 (Attends 2s)"):
            time.sleep(2)  # Attente de 30 secondes
            
        # Sélection aléatoire du client
        client_choisi = random.choice(st.session_state.clients)
        st.session_state.clients.remove(client_choisi)

        # Stocker le gagnant temporairement
        st.session_state.dernier_gagnant = client_choisi
        
        # Rafraîchir l'interface pour afficher le pop-up
        st.experimental_rerun()
    else:
        st.warning("Il n'y a plus de clients à tirer.")

# 🎉 Simulation d'un pop-up
if st.session_state.dernier_gagnant:
    pop_up = st.empty()  # Création d'un espace temporaire pour afficher le message

    with pop_up.container():
        st.markdown("### 🎉 Félicitations au gagnant !")
        st.success(f"🎊 **{st.session_state.dernier_gagnant['Nom']} -- {st.session_state.dernier_gagnant['Numéro']}**")
        #st.write(f"📞 **Numéro : {st.session_state.dernier_gagnant['Numéro']}**")
        if st.button("🏅 Ajouter aux gagnants"):
            st.session_state.gagnants.append(st.session_state.dernier_gagnant)
            st.session_state.dernier_gagnant = None
            pop_up.empty()  # Effacer le pop-up
            st.experimental_rerun()

# Bouton pour réinitialiser la liste
if st.button("🔄 Réinitialiser l'urne"):
    st.session_state.clients = [
        {"Nom": "Mahdi Salah Doubeh", "Numéro": "77631405"},
        {"Nom": "Amin Hassan Doualeh", "Numéro": "77049495"},
        {"Nom": "Amal Abdourahman Abib", "Numéro": "77653929"},
        {"Nom": "Djibril Djama Obsieh", "Numéro": "77132436"},
        {"Nom": "Ayan Abdi Ali", "Numéro": "77037454"},
        {"Nom": "Abdillahi Omar Dirieh", "Numéro": "77825892"},
        {"Nom": "Ayan Douksieh Abdi", "Numéro": "77287792"},
        {"Nom": "Abdourahman Abdoulhakim Med", "Numéro": "77657470"},
        {"Nom": "Abdourahman Omar Assoweh", "Numéro": "77855034"},
        {"Nom": "Moussa Farah Iyeh", "Numéro": "77876903"},
        {"Nom": "Fathia Ismael Hassan", "Numéro": "77884664"},
        {"Nom": "Elmi Ahmed Abdi", "Numéro": "77826904"},
        {"Nom": "Hibo Mahamoud Abdillahi ", "Numéro": "77812815"},
        {"Nom": "Fozzi Ali Batoun", "Numéro": "77825921"},
        {"Nom": "Abdoulfatah Moussa Doualeh", "Numéro": "77219582"},
        {"Nom": "Hodan Abdi Osman", "Numéro": "77115632"},
        {"Nom": "Sami", "Numéro": "77206755"},
    ]
    st.session_state.gagnants = []  # Réinitialiser les gagnants
    st.session_state.dernier_gagnant = None  # Effacer le dernier gagnant
    st.experimental_rerun()












