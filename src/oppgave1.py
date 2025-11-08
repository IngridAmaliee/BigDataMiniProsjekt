import os
from pathlib import Path
import pandas as pd
import plotly.express as px

def visualiser_churn_mot_avgift():
    """
    Funksjon for å visualisere kundefrafall (churn) mot månedlige avgifter.
    Returnerer en plotly figur som viser forholdet mellom churn og månedlige avgifter.
    """
    # Les inn datasettet (finn fil relativt til denne filen eller som fallback fra gjeldende arbeidskatalog)
    csv_filename = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
    # Primærvei: repo/data/... basert på denne filens plassering
    data_file = Path(__file__).resolve().parent.parent / 'data' / csv_filename
    # Fallback: arbeidskatalog/data/...
    alt_file = Path.cwd() / 'data' / csv_filename
    if data_file.exists():
        csv_path = data_file
    elif alt_file.exists():
        csv_path = alt_file
    else:
        raise FileNotFoundError(
            f"Fant ikke datafilen '{csv_filename}'. Sjekket: {data_file} og {alt_file}")

    df = pd.read_csv(csv_path)
    
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