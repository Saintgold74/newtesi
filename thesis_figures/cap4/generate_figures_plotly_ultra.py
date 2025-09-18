#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figure Ultra-Moderne per Capitolo 4 usando Plotly
Design di livello pubblicazione premium
"""

import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd

# Tema colori professionale
COLORS = {
    'primary': '#2C3E50',      # Blu scuro elegante
    'secondary': '#E74C3C',     # Rosso sofisticato
    'accent': '#3498DB',        # Blu brillante
    'success': '#27AE60',       # Verde successo
    'warning': '#F39C12',       # Arancione warning
    'info': '#8E44AD',          # Viola info
    'light': '#ECF0F1',         # Grigio chiaro
    'dark': '#34495E',          # Grigio scuro
}

# Template Plotly personalizzato
template_custom = dict(
    layout=go.Layout(
        font=dict(family="Helvetica, Arial", size=12, color=COLORS['dark']),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(l=60, r=60, t=80, b=60),
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Arial"),
        hovermode='closest'
    )
)

# =============================================================================
# FIGURA 1: DIAGRAMMA DI VENN INTERATTIVO
# =============================================================================

def create_venn_diagram_plotly():
    """
    Diagramma di Venn interattivo con Plotly
    """
    fig = go.Figure()
    
    # Definizione dei cerchi
    circles = [
        dict(name='PCI-DSS 4.0', x=0, y=0, r=2.5, color=COLORS['primary'], 
             controls=264, opacity=0.5),
        dict(name='GDPR', x=2.2, y=0, r=2.5, color=COLORS['secondary'], 
             controls=99, opacity=0.5),
        dict(name='NIS2', x=1.1, y=-1.9, r=2.5, color=COLORS['success'], 
             controls=31, opacity=0.5),
    ]
    
    # Aggiungi i cerchi
    for circle in circles:
        # Crea punti per il cerchio
        theta = np.linspace(0, 2*np.pi, 100)
        x_circle = circle['x'] + circle['r'] * np.cos(theta)
        y_circle = circle['y'] + circle['r'] * np.sin(theta)
        
        fig.add_trace(go.Scatter(
            x=x_circle, y=y_circle,
            fill='toself',
            fillcolor=circle['color'],
            opacity=circle['opacity'],
            line=dict(color=circle['color'], width=3),
            name=circle['name'],
            hovertemplate=f"<b>{circle['name']}</b><br>{circle['controls']} controlli<extra></extra>",
            mode='lines'
        ))
    
    # Aggiungi annotazioni per le intersezioni
    annotations = [
        dict(x=1.1, y=0, text='<b>47</b>', showarrow=False, 
             font=dict(size=20, color=COLORS['info'])),
        dict(x=-0.3, y=-0.8, text='<b>23</b>', showarrow=False,
             font=dict(size=16, color=COLORS['info'])),
        dict(x=2.5, y=-0.8, text='<b>31</b>', showarrow=False,
             font=dict(size=16, color=COLORS['info'])),
        dict(x=1.1, y=-0.7, text='<b>55</b>', showarrow=False,
             font=dict(size=24, color=COLORS['warning'])),
        
        # Labels principali
        dict(x=-1.2, y=2.2, text='<b>PCI-DSS 4.0</b><br>264 controlli', 
             showarrow=False, font=dict(size=14, color=COLORS['primary'])),
        dict(x=3.4, y=2.2, text='<b>GDPR</b><br>99 articoli', 
             showarrow=False, font=dict(size=14, color=COLORS['secondary'])),
        dict(x=1.1, y=-4.5, text='<b>NIS2</b><br>31 misure', 
             showarrow=False, font=dict(size=14, color=COLORS['success'])),
    ]
    
    # Box informativo
    fig.add_trace(go.Scatter(
        x=[4.5, 6.5, 6.5, 4.5, 4.5],
        y=[-0.5, -0.5, -2.5, -2.5, -0.5],
        mode='lines',
        line=dict(color=COLORS['dark'], width=2),
        fill='toself',
        fillcolor=COLORS['light'],
        showlegend=False,
        hoverinfo='skip'
    ))
    
    annotations.append(dict(
        x=5.5, y=-1.5,
        text='<b>Controlli Comuni</b><br>156 totali (39.6%)<br>55 core<br>101 parziali',
        showarrow=False,
        font=dict(size=11, color=COLORS['dark']),
        bgcolor='white',
        bordercolor=COLORS['primary'],
        borderwidth=2
    ))
    
    fig.update_layout(
        title=dict(
            text='<b>Sovrapposizioni Standard Normativi nel Retail</b><br><sub>Analisi integrazione multi-framework</sub>',
            font=dict(size=20, color=COLORS['dark']),
            x=0.5,
            xanchor='center'
        ),
        xaxis=dict(visible=False, range=[-4, 7]),
        yaxis=dict(visible=False, range=[-6, 4], scaleanchor="x"),
        annotations=annotations,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor=COLORS['dark'],
            borderwidth=1
        ),
        height=600,
        template=template_custom
    )
    
    return fig

# =============================================================================
# FIGURA 2: ARCHITETTURA SANKEY DIAGRAM
# =============================================================================

def create_architecture_sankey():
    """
    Diagramma Sankey per l'architettura del sistema
    """
    # Definizione nodi
    labels = [
        # Livello 1 (0-4)
        "Config Mgmt", "SIEM Logs", "Metriche KPI", "Threat Intel", "Audit Trail",
        # Livello 2 (5-7)
        "Correlazione", "Analisi Rischio", "Valutazione Conformità",
        # Livello 3 (8-11)
        "Dashboard", "Console Op.", "Reporting", "API REST"
    ]
    
    # Definizione collegamenti
    source = [0,1,2,3,4, 0,1,2,3,4, 5,5,6,6,7,7, 5,6,7]
    target = [5,5,6,6,7, 5,5,6,6,7, 8,9,9,10,10,11, 8,10,11]
    value =  [20,25,15,10,20, 15,20,25,15,15, 30,20,25,30,35,25, 10,15,20]
    
    # Colori per livelli
    node_colors = (
        [COLORS['success']] * 5 +  # Livello 1
        [COLORS['info']] * 3 +     # Livello 2
        [COLORS['warning']] * 4    # Livello 3
    )
    
    link_colors = ['rgba(52, 152, 219, 0.2)'] * len(source)
    
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=30,
            line=dict(color="white", width=2),
            label=[f"<b>{label}</b>" for label in labels],
            color=node_colors,
            hovertemplate='<b>%{label}</b><br>Flusso: %{value}<extra></extra>',
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color=link_colors,
            hovertemplate='Da %{source.label}<br>A %{target.label}<br>Valore: %{value}<extra></extra>',
        )
    )])
    
    fig.update_layout(
        title=dict(
            text='<b>Architettura del Sistema - Flusso Dati</b><br><sub>Integrazione multi-livello per conformità</sub>',
            font=dict(size=20, color=COLORS['dark']),
            x=0.5,
            xanchor='center'
        ),
        font=dict(size=11, color=COLORS['dark']),
        height=500,
        template=template_custom,
        annotations=[
            dict(x=0, y=1.1, text='<b>Livello 1: Raccolta</b>', 
                 showarrow=False, font=dict(size=12, color=COLORS['success'])),
            dict(x=0.5, y=1.1, text='<b>Livello 2: Elaborazione</b>', 
                 showarrow=False, font=dict(size=12, color=COLORS['info'])),
            dict(x=1, y=1.1, text='<b>Livello 3: Presentazione</b>', 
                 showarrow=False, font=dict(size=12, color=COLORS['warning'])),
        ]
    )
    
    return fig

# =============================================================================
# FIGURA 3: PROCESSO GDPR - FLOWCHART INTERATTIVO
# =============================================================================

def create_gdpr_process_flow():
    """
    Flowchart interattivo del processo GDPR
    """
    # Creazione del grafico di rete
    fig = go.Figure()
    
    # Definizione posizioni dei nodi
    nodes = {
        'start': (0, 2, '🚀 START'),
        'receive': (2, 2, '📥 Ricezione'),
        'verify': (4, 2, '🔍 Verifica'),
        'reject': (4, 4, '❌ Respinta'),
        'identify': (6, 2, '🔎 Identificazione'),
        'execute': (8, 1, '⚡ Esecuzione'),
        'notify': (8, 3, '📧 Notifica'),
        'document': (10, 2, '📝 Audit'),
        'end': (12, 2, '🏁 END')
    }
    
    # Aggiungi nodi come scatter plot
    for node_id, (x, y, label) in nodes.items():
        color = COLORS['danger'] if node_id == 'reject' else COLORS['primary']
        if node_id in ['start', 'end']:
            color = COLORS['success']
        
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            marker=dict(size=60, color=color, 
                       line=dict(width=3, color='white')),
            text=[label],
            textposition='middle center',
            textfont=dict(size=10, color='white', family='Arial Black'),
            hovertemplate=f'<b>{label}</b><extra></extra>',
            showlegend=False
        ))
    
    # Definizione delle connessioni
    connections = [
        ('start', 'receive', 'Inizio'),
        ('receive', 'verify', 'Submit'),
        ('verify', 'reject', 'NO'),
        ('verify', 'identify', 'SI'),
        ('identify', 'execute', ''),
        ('identify', 'notify', ''),
        ('execute', 'document', ''),
        ('notify', 'document', ''),
        ('document', 'end', 'Fine')
    ]
    
    # Aggiungi le frecce
    for start, end, label in connections:
        x0, y0, _ = nodes[start]
        x1, y1, _ = nodes[end]
        
        # Freccia
        fig.add_annotation(
            x=x1, y=y1,
            ax=x0, ay=y0,
            xref='x', yref='y',
            axref='x', ayref='y',
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor=COLORS['dark'],
            opacity=0.6
        )
        
        # Label sulla freccia
        if label:
            fig.add_annotation(
                x=(x0+x1)/2, y=(y0+y1)/2,
                text=label,
                showarrow=False,
                font=dict(size=9, color=COLORS['dark']),
                bgcolor='white',
                bordercolor=COLORS['dark'],
                borderwidth=1,
                borderpad=2
            )
    
    # Timer annotations
    fig.add_shape(
        type="rect",
        x0=1, y0=1.5, x1=5, y1=2.5,
        line=dict(color=COLORS['warning'], width=2, dash="dash"),
        fillcolor=COLORS['warning'],
        opacity=0.1
    )
    fig.add_annotation(
        x=3, y=1.3,
        text='⏱️ Max 72h',
        showarrow=False,
        font=dict(size=10, color=COLORS['warning'], family='Arial Black')
    )
    
    fig.add_shape(
        type="rect",
        x0=5.5, y0=0.5, x1=10.5, y1=3.5,
        line=dict(color=COLORS['info'], width=2, dash="dash"),
        fillcolor=COLORS['info'],
        opacity=0.1
    )
    fig.add_annotation(
        x=8, y=0.3,
        text='📅 Max 30 giorni',
        showarrow=False,
        font=dict(size=10, color=COLORS['info'], family='Arial Black')
    )
    
    fig.update_layout(
        title=dict(
            text='<b>Processo Automatizzato GDPR</b><br><sub>Gestione diritti degli interessati</sub>',
            font=dict(size=20, color=COLORS['dark']),
            x=0.5,
            xanchor='center'
        ),
        xaxis=dict(visible=False, range=[-1, 13]),
        yaxis=dict(visible=False, range=[0, 5]),
        height=400,
        template=template_custom,
        showlegend=False
    )
    
    return fig

# =============================================================================
# FIGURA 4: CONFRONTO 3D BAR CHART
# =============================================================================

def create_3d_comparison():
    """
    Grafico 3D per il confronto degli scenari
    """
    metrics = ['Detection<br>(ore)', 'Sistemi<br>(unità)', 
               'Downtime<br>(ore)', 'Impatto<br>(k€)']
    
    # Dati
    real = [360, 2847, 120, 8700]
    compliant = [6, 12, 4, 300]
    
    # Crea subplot 3D
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('<b>Scenario Reale</b>', '<b>Con Conformità Integrata</b>'),
        specs=[[{'type': 'bar'}, {'type': 'bar'}]],
        horizontal_spacing=0.15
    )
    
    # Scenario reale
    fig.add_trace(
        go.Bar(
            x=metrics,
            y=real,
            name='Scenario Reale',
            marker=dict(
                color=real,
                colorscale='Reds',
                showscale=True,
                colorbar=dict(x=0.45, len=0.5, title='Valore'),
                line=dict(color='darkred', width=2)
            ),
            text=[f'{v:,}' for v in real],
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Valore: %{y:,}<extra></extra>'
        ),
        row=1, col=1
    )
    
    # Scenario conforme
    fig.add_trace(
        go.Bar(
            x=metrics,
            y=compliant,
            name='Conformità',
            marker=dict(
                color=compliant,
                colorscale='Greens',
                showscale=True,
                colorbar=dict(x=1.02, len=0.5, title='Valore'),
                line=dict(color='darkgreen', width=2)
            ),
            text=[f'{v:,}' for v in compliant],
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Valore: %{y:,}<extra></extra>'
        ),
        row=1, col=2
    )
    
    # Aggiungi indicatori di miglioramento
    improvements = [
        (0, 98.3), (1, 99.6), (2, 96.7), (3, 96.5)
    ]
    
    for col in [1, 2]:
        for i, imp in improvements:
            y_pos = real[i] if col == 1 else compliant[i]
            fig.add_annotation(
                x=i, y=y_pos * 1.15,
                text=f'<b>-{imp}%</b>' if col == 2 else '',
                showarrow=False,
                font=dict(size=10, color=COLORS['success']),
                xref=f'x{col}', yref=f'y{col}'
            )
    
    fig.update_layout(
        title=dict(
            text='<b>Analisi Controfattuale - Confronto Scenari</b><br><sub>Impatto della conformità integrata sui KPI critici</sub>',
            font=dict(size=20, color=COLORS['dark']),
            x=0.5,
            xanchor='center'
        ),
        showlegend=False,
        height=500,
        template=template_custom,
    )
    
    # Update y-axes to log scale
    fig.update_yaxes(type="log", row=1, col=1, title_text="Scala Log")
    fig.update_yaxes(type="log", row=1, col=2, title_text="Scala Log")
    
    return fig

# =============================================================================
# FIGURA 5: MATURITY MODEL RADAR CHART
# =============================================================================

def create_maturity_radar():
    """
    Radar chart per il modello di maturità
    """
    categories = ['Governance', 'Processi', 'Tecnologia', 
                  'Persone', 'Metriche', 'Automazione']
    
    # Dati per i diversi livelli di maturità
    levels = {
        'Frammentato': [1, 1, 2, 1, 1, 0],
        'Coordinato': [2, 3, 3, 2, 2, 1],
        'Integrato': [4, 4, 4, 3, 3, 3],
        'Ottimizzato': [4, 5, 5, 4, 4, 4],
        'Adattivo': [5, 5, 5, 5, 5, 5]
    }
    
    fig = go.Figure()
    
    colors_radar = {
        'Frammentato': COLORS['danger'],
        'Coordinato': COLORS['warning'],
        'Integrato': COLORS['info'],
        'Ottimizzato': COLORS['success'],
        'Adattivo': COLORS['primary']
    }
    
    for level, values in levels.items():
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            fillcolor=colors_radar[level],
            opacity=0.2,
            line=dict(color=colors_radar[level], width=2),
            name=level,
            hovertemplate='<b>%{theta}</b><br>Livello: %{r}<extra></extra>'
        ))
    
    # Aggiungi posizione attuale (esempio RetailCo)
    fig.add_trace(go.Scatterpolar(
        r=[3, 4, 4, 3, 3, 3],
        theta=categories,
        fill='toself',
        fillcolor=COLORS['accent'],
        opacity=0.5,
        line=dict(color=COLORS['accent'], width=3, dash='dash'),
        name='RetailCo (Attuale)',
        marker=dict(size=8, color=COLORS['accent'])
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5],
                tickmode='array',
                tickvals=[1, 2, 3, 4, 5],
                ticktext=['1', '2', '3', '4', '5']
            ),
            angularaxis=dict(
                tickfont=dict(size=11)
            )
        ),
        title=dict(
            text='<b>Modello di Maturità - Conformità Integrata</b><br><sub>Valutazione multidimensionale delle capacità</sub>',
            font=dict(size=20, color=COLORS['dark']),
            x=0.5,
            xanchor='center'
        ),
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.1,
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor=COLORS['dark'],
            borderwidth=1
        ),
        height=500,
        template=template_custom
    )
    
    return fig

# =============================================================================
# FIGURA 6: TIMELINE GANTT INTERATTIVO
# =============================================================================

def create_interactive_gantt():
    """
    Gantt chart interattivo per la timeline di implementazione
    """
    df = pd.DataFrame([
        dict(Task="Assessment", Start='2024-01-01', Finish='2024-03-31', 
             Resource="Fase 1", Completion=100),
        dict(Task="Progettazione", Start='2024-04-01', Finish='2024-06-30', 
             Resource="Fase 2", Completion=100),
        dict(Task="Pilota", Start='2024-07-01', Finish='2024-12-31', 
             Resource="Fase 3", Completion=75),
        dict(Task="Rollout", Start='2025-01-01', Finish='2025-12-31', 
             Resource="Fase 4", Completion=25),
    ])
    
    # Colori per fase
    colors_gantt = {
        'Fase 1': COLORS['info'],
        'Fase 2': COLORS['success'], 
        'Fase 3': COLORS['warning'],
        'Fase 4': COLORS['primary']
    }
    
    fig = ff.create_gantt(
        df,
        colors=colors_gantt,
        index_col='Resource',
        show_colorbar=True,
        showgrid_x=True,
        showgrid_y=True,
        group_tasks=True
    )
    
    # Aggiungi milestone
    milestones = [
        ('2024-03-31', 'M1: Business Case'),
        ('2024-06-30', 'M2: Framework'),
        ('2024-12-31', 'M3: Pilota'),
        ('2025-12-31', 'M4: Completo')
    ]
    
    for date, label in milestones:
        fig.add_vline(
            x=date, 
            line_width=2,
            line_dash="dash", 
            line_color=COLORS['danger'],
            annotation_text=label,
            annotation_position="top"
        )
    
    # Aggiungi percentuali di completamento
    for i, row in df.iterrows():
        fig.add_annotation(
            x=pd.to_datetime(row['Start']) + (pd.to_datetime(row['Finish']) - pd.to_datetime(row['Start']))/2,
            y=i,
            text=f"{row['Completion']}%",
            showarrow=False,
            font=dict(color='white', size=12, family='Arial Black'),
            bgcolor=colors_gantt[row['Resource']],
            borderpad=4
        )
    
    fig.update_layout(
        title=dict(
            text='<b>Roadmap Implementazione Conformità</b><br><sub>Timeline e milestone del progetto</sub>',
            font=dict(size=20, color=COLORS['dark']),
            x=0.5,
            xanchor='center'
        ),
        xaxis=dict(title='Timeline', tickformat='%b %Y'),
        yaxis=dict(title='Fasi', autorange='reversed'),
        height=400,
        template=template_custom,
        hovermode='x unified'
    )
    
    return fig

# =============================================================================
# SALVATAGGIO FIGURE
# =============================================================================

def save_all_plotly_figures():
    """
    Genera e salva tutte le figure Plotly
    """
    figures = [
        (create_venn_diagram_plotly(), 'figura_4_1_venn_ultra'),
        (create_architecture_sankey(), 'figura_4_2_sankey_ultra'),
        (create_gdpr_process_flow(), 'figura_4_3_process_ultra'),
        (create_3d_comparison(), 'figura_4_4_comparison_ultra'),
        (create_maturity_radar(), 'figura_4_5_maturity_ultra'),
        (create_interactive_gantt(), 'figura_4_6_gantt_ultra')
    ]
    
    print("\n" + "="*70)
    print("🎨 GENERAZIONE FIGURE ULTRA-MODERNE CON PLOTLY")
    print("="*70 + "\n")
    
    for fig, filename in figures:
        try:
            # Salva come HTML interattivo
            fig.write_html(f"{filename}.html")
            
            # Salva come immagine statica PNG
            fig.write_image(f"{filename}.png", width=1600, height=900, scale=2)
            
            # Salva come PDF
            fig.write_image(f"{filename}.pdf", width=1600, height=900)
            
            # Salva come SVG
            fig.write_image(f"{filename}.svg", width=1600, height=900)
            
            print(f"✅ {filename}")
            print(f"   ├─ HTML: {filename}.html (interattivo)")
            print(f"   ├─ PNG:  {filename}.png (alta risoluzione)")
            print(f"   ├─ PDF:  {filename}.pdf (vettoriale)")
            print(f"   └─ SVG:  {filename}.svg (editabile)")
            
        except Exception as e:
            print(f"❌ Errore in {filename}: {str(e)}")
            print("   Suggerimento: installa kaleido con 'pip install kaleido' per export")
    
    print("\n" + "="*70)
    print("✨ FIGURE ULTRA-MODERNE GENERATE CON SUCCESSO!")
    print("="*70)

if __name__ == '__main__':
    import sys
    
    # Verifica dipendenze
    try:
        import plotly
        import kaleido
    except ImportError:
        print("\n⚠️  ATTENZIONE: Dipendenze mancanti!")
        print("-"*50)
        print("Installa le dipendenze necessarie con:")
        print("\npip install plotly kaleido pandas")
        print("\nPer l'export in PDF potrebbe essere necessario anche:")
        print("pip install -U kaleido")
        print("-"*50)
        sys.exit(1)
    
    # Genera tutte le figure
    save_all_plotly_figures()
    
    print("\n" + "📊 CARATTERISTICHE DELLE FIGURE ULTRA-MODERNE:")
    print("-"*50)
    print("✓ Design interattivo (HTML)")
    print("✓ Grafica vettoriale scalabile")
    print("✓ Palette colori professionale")
    print("✓ Effetti visivi avanzati")
    print("✓ Export multi-formato")
    print("✓ Responsive e adattabile")
    print("✓ Pronte per pubblicazione")
    print("\n" + "="*70)
