# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:26:35 2025

@author: HP
"""
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="🎯 Tirage Par MSISDN", layout="centered")
st.title("🎲 Tirage au sort pour la promo du Jeudi")

# Initialiser la session
if "valeurs" not in st.session_state:
    st.session_state.valeurs = []
if "tirages" not in st.session_state:
    st.session_state.tirages = []
if "df_sans_doublons" not in st.session_state:
    st.session_state.df_sans_doublons = pd.DataFrame()

# Upload fichier
uploaded_file = st.file_uploader("📥 Téléversez un fichier Excel contenant une seule colonne", type=["xlsx", "xls"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.subheader("🧾 Contenu du fichier (avec doublons possibles)")
        st.dataframe(df)

        # Sélection automatique de la colonne s’il y en a une seule
        colonnes = df.columns.tolist()
        if len(colonnes) == 1:
            col = colonnes[0]
            if st.button("📤 Charger les données"):
                # Supprimer les doublons et valeurs manquantes
                valeurs_uniques = df[col].dropna().drop_duplicates().tolist()
               
                nb_total = df[col].dropna().shape[0]
                nb_uniques = len(valeurs_uniques)
                nb_doublons = nb_total - nb_uniques

                st.session_state.valeurs = valeurs_uniques
                st.session_state.tirages = []
                st.session_state.df_sans_doublons = pd.DataFrame(valeurs_uniques, columns=["Valeurs uniques"])
               
               
                st.success(f"✅ Données chargées avec succès : {nb_doublons} numéro(s) doublon(s) supprimé(s).")
               
               

        else:
            st.warning("❌ Le fichier doit contenir **exactement une seule colonne**.")

    except Exception as e:
        st.error(f"Erreur lors du chargement : {e}")

# Affichage du tableau sans doublons
if not st.session_state.df_sans_doublons.empty:
    st.subheader("✅ Données sans doublons")
    st.dataframe(st.session_state.df_sans_doublons)

# Tirage
if st.session_state.valeurs:
    st.subheader("🎯 Tirage")
    if st.button("🎁 Tirer un client"):
        valeur = random.choice(st.session_state.valeurs)
        st.session_state.valeurs.remove(valeur)
        st.session_state.tirages.append(valeur)
        st.success(f"🎉 Client tiré : **{valeur}**")

# Afficher les résultats
if st.session_state.tirages:
    st.subheader("📋 Résultats des tirages")
    st.dataframe(pd.DataFrame(st.session_state.tirages, columns=["Clients Tirés"]))












