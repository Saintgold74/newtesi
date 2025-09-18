#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figure Ultra-Moderne per Capitolo 4 usando Plotly - VERSIONE CORRETTA
Design di livello pubblicazione premium con gestione errori
"""

import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Tema colori professionale completo
COLORS = {
    'primary': '#2C3E50',      # Blu scuro elegante
    'secondary': '#E74C3C',     # Rosso sofisticato
    'accent': '#3498DB',        # Blu brillante
    'success': '#27AE60',       # Verde successo
    'danger': '#C0392B',        # Rosso danger
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
# FIGURA 1: DIAGRAMMA DI VENN INTERATTIVO (SEMPLIFICATO)
# =============================================================================

def create_venn_diagram_simple():
    """
    Diagramma di Venn semplificato ma elegante
    """
    fig = go.Figure()
    
    # Definizione dei cerchi
    circles = [
        dict(name='PCI-DSS 4.0', x=0, y=0, r=2.5, color=COLORS['primary'], 
             controls=264, opacity=0.4),
        dict(name='GDPR', x=2.2, y=0, r=2.5, color=COLORS['secondary'], 
             controls=99, opacity=0.4),
        dict(name='NIS2', x=1.1, y=-1.9, r=2.5, color=COLORS['success'], 
             controls=31, opacity=0.4),
    ]
    
    # Aggiungi i cerchi
    for circle in circles:
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
    
    # Annotazioni principali
    annotations = [
        # Valori intersezioni
        dict(x=1.1, y=0, text='<b>47</b>', font=dict(size=20, color='white'),
             bgcolor=COLORS['info'], borderpad=4),
        dict(x=-0.3, y=-0.8, text='<b>23</b>', font=dict(size=16, color='white'),
             bgcolor=COLORS['info'], borderpad=4),
        dict(x=2.5, y=-0.8, text='<b>31</b>', font=dict(size=16, color='white'),
             bgcolor=COLORS['info'], borderpad=4),
        dict(x=1.1, y=-0.7, text='<b>55</b>', font=dict(size=24, color='white'),
             bgcolor=COLORS['warning'], borderpad=4),
        
        # Labels standard
        dict(x=-1.2, y=2.5, text='<b>PCI-DSS 4.0</b><br>264 controlli', 
             font=dict(size=13, color=COLORS['primary'])),
        dict(x=3.4, y=2.5, text='<b>GDPR</b><br>99 articoli', 
             font=dict(size=13, color=COLORS['secondary'])),
        dict(x=1.1, y=-4.5, text='<b>NIS2</b><br>31 misure', 
             font=dict(size=13, color=COLORS['success'])),
        
        # Info box
        dict(x=5, y=-1.5,
             text='<b>Controlli Comuni</b><br>156 totali (39.6%)<br>55 core - 101 parziali',
             font=dict(size=10, color=COLORS['dark']),
             bgcolor='rgba(255,255,255,0.9)',
             bordercolor=COLORS['primary'],
             borderwidth=2,
             borderpad=8)
    ]
    
    for ann in annotations:
        ann['showarrow'] = False
    
    fig.update_layout(
        title=dict(
            text='<b>Sovrapposizioni Standard Normativi nel Retail</b>',
            font=dict(size=18, color=COLORS['dark']),
            x=0.5
        ),
        xaxis=dict(visible=False, range=[-4, 7]),
        yaxis=dict(visible=False, range=[-6, 4], scaleanchor="x"),
        annotations=annotations,
        showlegend=True,
        height=600,
        template=template_custom
    )
    
    return fig

# =============================================================================
# FIGURA 2: ARCHITETTURA - DIAGRAMMA GERARCHICO
# =============================================================================

def create_architecture_hierarchy():
    """
    Diagramma gerarchico dell'architettura
    """
    fig = go.Figure()
    
    # Livello 1 - Raccolta Dati
    level1 = ['Config Mgmt', 'SIEM Logs', 'Metriche KPI', 'Threat Intel', 'Audit Trail']
    x1 = np.linspace(-2, 2, len(level1))
    y1 = [0] * len(level1)
    
    # Livello 2 - Elaborazione
    level2 = ['Correlazione', 'Analisi Rischio', 'Valutazione Conformità']
    x2 = np.linspace(-1.5, 1.5, len(level2))
    y2 = [1] * len(level2)
    
    # Livello 3 - Presentazione
    level3 = ['Dashboard', 'Console Op.', 'Reporting', 'API REST']
    x3 = np.linspace(-1.8, 1.8, len(level3))
    y3 = [2] * len(level3)
    
    # Aggiungi nodi Livello 1
    fig.add_trace(go.Scatter(
        x=x1, y=y1,
        mode='markers+text',
        name='Livello 1: Raccolta',
        marker=dict(size=50, color=COLORS['success'], line=dict(width=2, color='white')),
        text=level1,
        textposition='bottom center',
        textfont=dict(size=10, color=COLORS['dark']),
        hovertemplate='<b>%{text}</b><br>Livello 1<extra></extra>'
    ))
    
    # Aggiungi nodi Livello 2
    fig.add_trace(go.Scatter(
        x=x2, y=y2,
        mode='markers+text',
        name='Livello 2: Elaborazione',
        marker=dict(size=50, color=COLORS['info'], line=dict(width=2, color='white')),
        text=level2,
        textposition='bottom center',
        textfont=dict(size=10, color=COLORS['dark']),
        hovertemplate='<b>%{text}</b><br>Livello 2<extra></extra>'
    ))
    
    # Aggiungi nodi Livello 3
    fig.add_trace(go.Scatter(
        x=x3, y=y3,
        mode='markers+text',
        name='Livello 3: Presentazione',
        marker=dict(size=50, color=COLORS['warning'], line=dict(width=2, color='white')),
        text=level3,
        textposition='bottom center',
        textfont=dict(size=10, color=COLORS['dark']),
        hovertemplate='<b>%{text}</b><br>Livello 3<extra></extra>'
    ))
    
    # Aggiungi connessioni
    for i in range(len(x1)):
        for j in range(len(x2)):
            fig.add_shape(type="line",
                x0=x1[i], y0=y1[i]+0.05, x1=x2[j], y1=y2[j]-0.05,
                line=dict(color="lightgray", width=1))
    
    for i in range(len(x2)):
        for j in range(len(x3)):
            fig.add_shape(type="line",
                x0=x2[i], y0=y2[i]+0.05, x1=x3[j], y1=y3[j]-0.05,
                line=dict(color="lightgray", width=1))
    
    # Aggiungi box per framework integrazione
    fig.add_shape(type="rect",
        x0=-2, y0=0.7, x1=2, y1=1.3,
        line=dict(color=COLORS['accent'], width=2, dash="dash"),
        fillcolor=COLORS['accent'], opacity=0.1
    )
    
    fig.add_annotation(
        x=0, y=1,
        text='<b>Framework di Integrazione Multi-Standard</b>',
        showarrow=False,
        font=dict(size=11, color=COLORS['accent']),
        bgcolor='white'
    )
    
    fig.update_layout(
        title=dict(
            text='<b>Architettura del Sistema di Conformità</b>',
            font=dict(size=18, color=COLORS['dark']),
            x=0.5
        ),
        xaxis=dict(visible=False, range=[-3, 3]),
        yaxis=dict(visible=False, range=[-0.5, 2.8]),
        height=500,
        showlegend=True,
        template=template_custom
    )
    
    return fig

# =============================================================================
# FIGURA 3: PROCESSO GDPR - FLOWCHART SEMPLIFICATO
# =============================================================================

def create_gdpr_flowchart_simple():
    """
    Flowchart GDPR semplificato
    """
    fig = go.Figure()
    
    # Nodi del processo
    nodes = [
        (1, 2, 'Ricezione', COLORS['info']),
        (3, 2, 'Verifica', COLORS['warning']),
        (3, 3.5, 'Respinta', COLORS['danger']),
        (5, 2, 'Identificazione', COLORS['info']),
        (7, 2, 'Esecuzione', COLORS['success']),
        (9, 2, 'Notifica', COLORS['primary']),
        (11, 2, 'Audit', COLORS['secondary'])
    ]
    
    # Aggiungi nodi
    for x, y, label, color in nodes:
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            marker=dict(size=60, color=color, line=dict(width=2, color='white')),
            text=[label],
            textposition='middle center',
            textfont=dict(size=10, color='white', family='Arial'),
            hovertemplate=f'<b>{label}</b><extra></extra>',
            showlegend=False
        ))
    
    # Frecce di flusso
    arrows = [
        (1, 2, 3, 2, 'Submit'),
        (3, 2, 3, 3.5, 'NO'),
        (3, 2, 5, 2, 'SI'),
        (5, 2, 7, 2, ''),
        (7, 2, 9, 2, ''),
        (9, 2, 11, 2, '')
    ]
    
    for x0, y0, x1, y1, label in arrows:
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
        
        if label:
            fig.add_annotation(
                x=(x0+x1)/2, y=(y0+y1)/2,
                text=label,
                showarrow=False,
                font=dict(size=9, color=COLORS['dark']),
                bgcolor='white'
            )
    
    # Timer zones
    fig.add_shape(type="rect",
        x0=0.5, y0=1.5, x1=3.5, y1=2.5,
        line=dict(color=COLORS['warning'], width=1, dash="dash"),
        fillcolor=COLORS['warning'], opacity=0.1
    )
    fig.add_annotation(
        x=2, y=1.3, text='Max 72h',
        showarrow=False,
        font=dict(size=10, color=COLORS['warning'])
    )
    
    fig.add_shape(type="rect",
        x0=4.5, y0=1.5, x1=11.5, y1=2.5,
        line=dict(color=COLORS['info'], width=1, dash="dash"),
        fillcolor=COLORS['info'], opacity=0.1
    )
    fig.add_annotation(
        x=8, y=1.3, text='Max 30 giorni',
        showarrow=False,
        font=dict(size=10, color=COLORS['info'])
    )
    
    fig.update_layout(
        title=dict(
            text='<b>Processo Automatizzato GDPR</b>',
            font=dict(size=18, color=COLORS['dark']),
            x=0.5
        ),
        xaxis=dict(visible=False, range=[0, 12]),
        yaxis=dict(visible=False, range=[0.5, 4]),
        height=400,
        template=template_custom
    )
    
    return fig

# =============================================================================
# FIGURA 4: CONFRONTO BAR CHART GROUPED
# =============================================================================

def create_comparison_bars():
    """
    Grafico a barre gruppate per confronto scenari
    """
    metrics = ['Detection<br>(ore)', 'Sistemi<br>(unità)', 
               'Downtime<br>(ore)', 'Impatto<br>(k€)']
    
    real = [360, 2847, 120, 8700]
    compliant = [6, 12, 4, 300]
    improvements = [98.3, 99.6, 96.7, 96.5]
    
    fig = go.Figure()
    
    # Barre scenario reale
    fig.add_trace(go.Bar(
        name='Scenario Reale',
        x=metrics,
        y=real,
        marker_color=COLORS['danger'],
        marker_line_color='darkred',
        marker_line_width=2,
        text=[f'{v:,}' for v in real],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Valore: %{y:,}<extra></extra>'
    ))
    
    # Barre scenario conforme
    fig.add_trace(go.Bar(
        name='Con Conformità',
        x=metrics,
        y=compliant,
        marker_color=COLORS['success'],
        marker_line_color='darkgreen',
        marker_line_width=2,
        text=[f'{v:,}' for v in compliant],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Valore: %{y:,}<extra></extra>'
    ))
    
    # Annotazioni miglioramenti
    for i, (metric, imp) in enumerate(zip(metrics, improvements)):
        fig.add_annotation(
            x=i, y=max(real[i], compliant[i]) * 1.1,
            text=f'<b>-{imp}%</b>',
            showarrow=False,
            font=dict(size=12, color=COLORS['info']),
            bgcolor='white',
            bordercolor=COLORS['info'],
            borderwidth=1,
            borderpad=2
        )
    
    fig.update_layout(
        title=dict(
            text='<b>Analisi Controfattuale - Confronto Scenari</b>',
            font=dict(size=18, color=COLORS['dark']),
            x=0.5
        ),
        barmode='group',
        yaxis=dict(
            title='Valori (scala logaritmica)',
            type='log',
            gridcolor='lightgray'
        ),
        xaxis=dict(
            title='Metriche',
            tickfont=dict(size=11)
        ),
        legend=dict(
            orientation="h",
            y=1.15,
            x=0.5,
            xanchor='center',
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor=COLORS['dark'],
            borderwidth=1
        ),
        height=500,
        template=template_custom
    )
    
    return fig

# =============================================================================
# FIGURA 5: MATURITY MODEL - SEMPLIFICATO
# =============================================================================

def create_maturity_levels():
    """
    Modello di maturità semplificato come barre orizzontali
    """
    levels = ['Frammentato', 'Coordinato', 'Integrato', 'Ottimizzato', 'Adattivo']
    current_level = 2.5  # RetailCo attualmente tra Coordinato e Integrato
    
    colors = [COLORS['danger'], COLORS['warning'], COLORS['info'], 
              COLORS['success'], COLORS['primary']]
    
    fig = go.Figure()
    
    # Barre dei livelli
    for i, (level, color) in enumerate(zip(levels, colors)):
        fig.add_trace(go.Bar(
            x=[i+1],
            y=[level],
            orientation='h',
            marker_color=color,
            marker_line_color='white',
            marker_line_width=2,
            name=level,
            hovertemplate=f'<b>{level}</b><br>Livello {i+1}<extra></extra>',
            showlegend=False
        ))
    
    # Indicatore posizione attuale
    fig.add_shape(
        type="line",
        x0=current_level, y0=-0.5, 
        x1=current_level, y1=len(levels)-0.5,
        line=dict(color=COLORS['accent'], width=3, dash="dash")
    )
    
    fig.add_annotation(
        x=current_level, y=len(levels),
        text='<b>RetailCo<br>Posizione Attuale</b>',
        showarrow=True,
        arrowhead=2,
        ax=0, ay=-40,
        font=dict(size=11, color=COLORS['accent']),
        bgcolor='white',
        bordercolor=COLORS['accent'],
        borderwidth=2
    )
    
    # Descrizioni livelli
    descriptions = [
        'Gestione separata, processi manuali',
        'Comunicazione tra team, alcune sinergie',
        'Framework unificato, processi standard',
        'Automazione estensiva, metriche predittive',
        'ML-driven, self-healing, adaptive'
    ]
    
    for i, desc in enumerate(descriptions):
        fig.add_annotation(
            x=0.1, y=i,
            text=desc,
            showarrow=False,
            font=dict(size=9, color=COLORS['dark']),
            xanchor='left'
        )
    
    fig.update_layout(
        title=dict(
            text='<b>Modello di Maturità - Conformità Integrata</b>',
            font=dict(size=18, color=COLORS['dark']),
            x=0.5
        ),
        xaxis=dict(
            title='Livello di Maturità',
            range=[0, 6],
            tickmode='array',
            tickvals=[1, 2, 3, 4, 5],
            ticktext=['1', '2', '3', '4', '5']
        ),
        yaxis=dict(
            tickmode='array',
            tickvals=list(range(len(levels))),
            ticktext=levels
        ),
        barmode='overlay',
        height=400,
        template=template_custom
    )
    
    return fig

# =============================================================================
# FIGURA 6: TIMELINE GANTT SEMPLIFICATO
# =============================================================================

def create_timeline_simple():
    """
    Timeline semplificato del progetto
    """
    # Dati delle fasi
    tasks = ['Assessment', 'Progettazione', 'Pilota', 'Rollout']
    start_dates = ['2024-01-01', '2024-04-01', '2024-07-01', '2025-01-01']
    end_dates = ['2024-03-31', '2024-06-30', '2024-12-31', '2025-12-31']
    completions = [100, 100, 75, 25]
    colors_timeline = [COLORS['info'], COLORS['success'], COLORS['warning'], COLORS['primary']]
    
    fig = go.Figure()
    
    # Aggiungi barre del Gantt
    for i, (task, start, end, completion, color) in enumerate(zip(
            tasks, start_dates, end_dates, completions, colors_timeline)):
        
        # Barra principale
        fig.add_trace(go.Scatter(
            x=[start, end, end, start, start],
            y=[i-0.4, i-0.4, i+0.4, i+0.4, i-0.4],
            fill='toself',
            fillcolor=color,
            opacity=0.6,
            line=dict(color=color, width=2),
            name=task,
            hovertemplate=f'<b>{task}</b><br>Completamento: {completion}%<extra></extra>',
            showlegend=False
        ))
        
        # Barra completamento
        if completion < 100:
            import pandas as pd
            start_dt = pd.to_datetime(start)
            end_dt = pd.to_datetime(end)
            completed_dt = start_dt + (end_dt - start_dt) * completion / 100
            
            fig.add_trace(go.Scatter(
                x=[start, str(completed_dt)[:10], str(completed_dt)[:10], start, start],
                y=[i-0.3, i-0.3, i+0.3, i+0.3, i-0.3],
                fill='toself',
                fillcolor=color,
                opacity=1,
                line=dict(color=color, width=0),
                showlegend=False,
                hoverinfo='skip'
            ))
        
        # Label task
        fig.add_annotation(
            x=start, y=i,
            text=f'<b>{task}</b> ({completion}%)',
            showarrow=False,
            font=dict(size=11, color='white'),
            xanchor='left',
            xshift=10
        )
    
    # Milestone
    milestones = [
        ('2024-03-31', 'M1: Business Case'),
        ('2024-06-30', 'M2: Framework'),
        ('2024-12-31', 'M3: Pilota'),
        ('2025-12-31', 'M4: Completo')
    ]
    
    for date, label in milestones:
        fig.add_shape(
            type="line",
            x0=date, y0=-0.5, x1=date, y1=len(tasks)-0.5,
            line=dict(color=COLORS['danger'], width=2, dash="dash")
        )
        fig.add_annotation(
            x=date, y=len(tasks),
            text=label,
            showarrow=False,
            font=dict(size=9, color=COLORS['danger']),
            textangle=-45
        )
    
    fig.update_layout(
        title=dict(
            text='<b>Roadmap Implementazione Conformità</b>',
            font=dict(size=18, color=COLORS['dark']),
            x=0.5
        ),
        xaxis=dict(
            title='Timeline 2024-2025',
            tickformat='%b %Y',
            gridcolor='lightgray'
        ),
        yaxis=dict(
            tickmode='array',
            tickvals=list(range(len(tasks))),
            ticktext=tasks,
            autorange='reversed'
        ),
        height=400,
        template=template_custom
    )
    
    return fig

# =============================================================================
# SALVATAGGIO FIGURE CON GESTIONE ERRORI
# =============================================================================

def save_all_plotly_figures():
    """
    Genera e salva tutte le figure Plotly con gestione errori robusta
    """
    figures = [
        (create_venn_diagram_simple, 'figura_4_1_venn_plotly'),
        (create_architecture_hierarchy, 'figura_4_2_architettura_plotly'),
        (create_gdpr_flowchart_simple, 'figura_4_3_processo_plotly'),
        (create_comparison_bars, 'figura_4_4_confronto_plotly'),
        (create_maturity_levels, 'figura_4_5_maturity_plotly'),
        (create_timeline_simple, 'figura_4_6_timeline_plotly')
    ]
    
    print("\n" + "="*70)
    print("🎨 GENERAZIONE FIGURE MODERNE CON PLOTLY")
    print("="*70 + "\n")
    
    successful_exports = []
    failed_exports = []
    
    for func, filename in figures:
        try:
            print(f"Generazione {filename}...")
            fig = func()
            
            # Sempre salva HTML (funziona sempre)
            html_file = f"{filename}.html"
            fig.write_html(html_file)
            print(f"  ✅ HTML: {html_file}")
            successful_exports.append(('HTML', html_file))
            
            # Prova export immagini se kaleido è disponibile
            try:
                # PNG
                png_file = f"{filename}.png"
                fig.write_image(png_file, width=1200, height=700, scale=2)
                print(f"  ✅ PNG:  {png_file}")
                successful_exports.append(('PNG', png_file))
                
                # PDF
                pdf_file = f"{filename}.pdf"
                fig.write_image(pdf_file, width=1200, height=700)
                print(f"  ✅ PDF:  {pdf_file}")
                successful_exports.append(('PDF', pdf_file))
                
                # SVG
                svg_file = f"{filename}.svg"
                fig.write_image(svg_file, width=1200, height=700)
                print(f"  ✅ SVG:  {svg_file}")
                successful_exports.append(('SVG', svg_file))
                
            except Exception as e:
                print(f"  ⚠️  Export immagini non disponibile (installa kaleido)")
                failed_exports.append((filename, 'images', str(e)))
            
        except Exception as e:
            print(f"❌ Errore completo in {filename}: {str(e)}")
            failed_exports.append((filename, 'all', str(e)))
    
    # Report finale
    print("\n" + "="*70)
    print("📊 REPORT GENERAZIONE FIGURE")
    print("="*70)
    
    if successful_exports:
        print(f"\n✅ SUCCESSI: {len(successful_exports)} file generati")
        print("   Le figure HTML sono interattive e sempre funzionanti!")
    
    if failed_exports:
        print(f"\n⚠️  ATTENZIONE: Alcuni export non disponibili")
        print("\n📝 Per abilitare l'export in PNG/PDF/SVG:")
        print("   pip install -U kaleido")
        print("   oppure")
        print("   conda install -c conda-forge python-kaleido")
    
    print("\n💡 SUGGERIMENTO:")
    print("   Le figure HTML sono perfette per presentazioni digitali")
    print("   Possono essere aperte direttamente nel browser")
    print("   e incorporate in presentazioni PowerPoint o siti web")
    
    print("\n" + "="*70)

if __name__ == '__main__':
    import sys
    
    # Check solo per plotly (kaleido è opzionale)
    try:
        import plotly
        print("✅ Plotly installato correttamente")
    except ImportError:
        print("\n❌ ERRORE: Plotly non installato!")
        print("-"*50)
        print("Installa con: pip install plotly pandas")
        sys.exit(1)
    
    # Check opzionale per kaleido
    try:
        import kaleido
        print("✅ Kaleido installato - export immagini disponibile")
    except ImportError:
        print("⚠️  Kaleido non installato - solo export HTML disponibile")
        print("   Per export PNG/PDF/SVG: pip install kaleido")
    
    print()
    
    # Genera tutte le figure
    save_all_plotly_figures()
