import streamlit as st
import plotly.graph_objs as go
import datetime
import yfinance as yf
from streamlit_extras.app_logo import add_logo
from PIL import Image

def calculer_prix_tshirt(prix_initial_bitcoin, prix_initial_tshirt, prix_actuel_bitcoin):
    taux_variation_bitcoin = (prix_actuel_bitcoin - prix_initial_bitcoin) / prix_initial_bitcoin
    prix_tshirt = prix_initial_tshirt * (1 + taux_variation_bitcoin)
    return max(prix_tshirt, prix_initial_tshirt)  

# Prix initial du Bitcoin (il y a 6 mois)
prix_initial_bitcoin = 24950.45

# Liste de noms de t-shirts
noms_tshirts = [f"T-shirt {i}" for i in range(1, 11)]

# Liste des prix initiaux pour chaque t-shirt
prix_initial_tshirts = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]  

# Liste des images pour chaque t-shirt
images_tshirts = ["https://static.wixstatic.com/media/8320c7_4901793bfb4d4e13a16d1669a4bc81f5~mv2.webp", "https://static.wixstatic.com/media/8320c7_e0710083e81345c38d9ba0fa408eed1b~mv2.jpg/v1/fill/w_68,h_68,al_c,q_85,usm_0.66_1.00_0.01/8320c7_e0710083e81345c38d9ba0fa408eed1b~mv2.webp", "https://static.wixstatic.com/media/8320c7_8556204384e648ba9d6edbf7ce03b52b~mv2.jpg/v1/fill/w_68,h_68,al_c,q_85,usm_0.66_1.00_0.01/8320c7_8556204384e648ba9d6edbf7ce03b52b~mv2.webp", "https://static.wixstatic.com/media/8320c7_1073916e1e99422baafabbdbced85eb0~mv2.jpg/v1/fill/w_68,h_68,al_c,q_85,usm_0.66_1.00_0.01/8320c7_1073916e1e99422baafabbdbced85eb0~mv2.webp", "https://static.wixstatic.com/media/8320c7_55af4dc6e1c748ceacb7498321fd1414~mv2.jpg/v1/fill/w_68,h_68,al_c,q_85,usm_0.66_1.00_0.01/8320c7_55af4dc6e1c748ceacb7498321fd1414~mv2.webp", "https://static.wixstatic.com/media/8320c7_f8fac75901104679bb749a0e5bbb2ca8~mv2.webp", "https://static.wixstatic.com/media/8320c7_0b2ce0113d2a4a99b11b0d240f657cb9~mv2.jpg/v1/fill/w_68,h_68,al_c,q_85,usm_0.66_1.00_0.01/8320c7_0b2ce0113d2a4a99b11b0d240f657cb9~mv2.webp", "https://static.wixstatic.com/media/8320c7_3bf6f77c5ba4440ea58efe1405751e01~mv2.jpg/v1/fill/w_68,h_68,al_c,q_85,usm_0.66_1.00_0.01/8320c7_3bf6f77c5ba4440ea58efe1405751e01~mv2.webp", "https://static.wixstatic.com/media/8320c7_4241c27042ba4b47b5e91a61e53b69ee~mv2.gif", "https://static.wixstatic.com/media/8320c7_3e4116e9416a4acea931d5e7df0c24c6~mv2.jpg/v1/fill/w_68,h_68,al_c,q_85,usm_0.66_1.00_0.01/8320c7_3e4116e9416a4acea931d5e7df0c24c6~mv2.webp"]

# Liste des descriptions pour chaque t-shirt
descriptions_tshirts = [
    "Description du T-shirt 1.",
    "Description du T-shirt 2.",
    "Description du T-shirt 3.",
    "Description du T-shirt 4.",
    "Description du T-shirt 5.",
    "Description du T-shirt 6.",
    "Description du T-shirt 7.",
    "Description du T-shirt 8.",
    "Description du T-shirt 9.",
    "Description du T-shirt 10."
]

# Liste des liens d'achat pour chaque t-shirt
liens_achat_tshirts = [
    "https://leonilagnado.wixsite.com/carla/product-page/tshirt-1",
    "https://leonilagnado.wixsite.com/carla/product-page/tshirt-2",
    "https://leonilagnado.wixsite.com/carla/product-page/tshirt-3",
    "https://leonilagnado.wixsite.com/carla/product-page/tshirt-4",
    "https://leonilagnado.wixsite.com/carla/product-page/tshirt-5",
    "https://leonilagnado.wixsite.com/carla/product-page/tshirt-6",
    "https://leonilagnado.wixsite.com/carla/product-page/tshirt-7",
    "https://leonilagnado.wixsite.com/carla/product-page/tshirt-8",
    "https://leonilagnado.wixsite.com/carla/product-page/tshirt-9",
    "https://leonilagnado.wixsite.com/carla/product-page/tshirt-10"
]

# Sélection du t-shirt à afficher
tshirt_selectionne = st.selectbox("Sélectionnez un t-shirt :", noms_tshirts)

expander = st.expander("Aperçu du produit")

# Trouver l'index du t-shirt sélectionné
index_tshirt = noms_tshirts.index(tshirt_selectionne)

# Afficher l'aperçu correspondant au t-shirt sélectionné
expander.markdown(f"""
<div style="display: flex; align-items: center;">
    <div style="flex: 1;">
        <img src="{images_tshirts[index_tshirt]}" alt="{tshirt_selectionne}" width="150" height="150">
    </div>
    <div style="flex: 3; padding-left: 20px;">
        <p>{descriptions_tshirts[index_tshirt]}</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Télécharger les données historiques du Bitcoin
data = yf.download("BTC-USD", start=datetime.datetime.now() - datetime.timedelta(days=180), end=datetime.datetime.now())

# Calculer l'évolution du prix du t-shirt
dates = data.index
prix_initial_tshirt = prix_initial_tshirts[noms_tshirts.index(tshirt_selectionne)]
prix_tshirt_history = [calculer_prix_tshirt(prix_initial_bitcoin, prix_initial_tshirt, prix_actuel_bitcoin) for prix_actuel_bitcoin in data['Close']]

# Dernier prix du t-shirt
dernier_prix_tshirt = round(prix_tshirt_history[-1], 2)

# Création du graphique avec Plotly (Chandeliers japonais)
fig = go.Figure(data=[go.Candlestick(x=dates,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])

fig.update_layout(title=f'Évolution du prix du {tshirt_selectionne} en fonction du prix du Bitcoin', xaxis_title='Date', yaxis_title='Prix du t-shirt (€)')

# Supprimer le volume en dessous du graphique
fig.update_layout(xaxis_rangeslider_visible=False, showlegend=False)

# Afficher le graphique
col1, col2 = st.columns([3, 1])
with col1:
    st.plotly_chart(fig)

# Ajouter l'image à droite du graphique
with col2:
    image = st.image("https://st3.depositphotos.com/1311476/17107/i/450/depositphotos_171075154-stock-photo-golden-bitcoin-souvenir-coin.jpg",width=100)

# Afficher le bouton "Acheter" avec un lien d'achat différent pour chaque t-shirt
st.markdown(f'<center><a href="{liens_achat_tshirts[index_tshirt]}">Acheter maintenant ({dernier_prix_tshirt} €)</a></center>', unsafe_allow_html=True)
