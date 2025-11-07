import pandas as pd
import plotly.express as px

def visualiser_churn_mot_avgift():
    """
    Funksjon for å visualisere kundefrafall (churn) mot månedlige avgifter.
    Returnerer en plotly figur som viser forholdet mellom churn og månedlige avgifter.
    """
    # Les inn datasettet
    df = pd.read_csv('../WA_Fn-UseC_-Telco-Customer-Churn.csv')
    
    # Opprett en box plot som viser distribusjonen av månedlige avgifter for hver churn-kategori
    fig = px.box(df, 
                 x='Churn',  # Kundefrafall på x-aksen
                 y='MonthlyCharges',  # Månedlige avgifter på y-aksen
                 title='Distribusjon av månedlige avgifter per churn-status',
                 labels={
                     'Churn': 'Kundefrafall',
                     'MonthlyCharges': 'Månedlige avgifter (USD)'
                 })
    
    # Legg til litt styling
    fig.update_layout(
        title_x=0.5,  # Sentrer tittelen
        boxmode='group'  # Gruppér box plots
    )
    
    return fig

if __name__ == "__main__":
    # Test funksjonen
    fig = visualiser_churn_mot_avgift()
    fig.show()