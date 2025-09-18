#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Organigramma Moderno per la Conformità Integrata
Versione Premium con design professionale
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Polygon
import matplotlib.patheffects as path_effects
import numpy as np

# Configurazione stile premium
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Segoe UI', 'Helvetica', 'Arial'],
    'font.size': 11,
    'figure.facecolor': 'white',
    'axes.facecolor': '#f8f9fa',
})

# Palette colori professionale e moderna
COLORS = {
    'strategic': '#2E4057',    # Blu scuro elegante
    'tactical': '#048A81',     # Verde acqua professionale  
    'operational': '#54C6EB',  # Blu chiaro
    'accent': '#F18F01',       # Arancione per evidenziare
    'danger': '#C73E1D',       # Rosso per audit
    'info': '#8B80F9',         # Viola per report
    'bg_light': '#F7F7F7',     # Sfondo chiaro
    'text': '#2C3E50',         # Testo principale
    'text_light': '#FFFFFF',   # Testo su sfondo scuro
}

def create_modern_org_chart():
    """
    Crea un organigramma moderno e visualmente accattivante
    """
    fig = plt.figure(figsize=(16, 12), facecolor='white')
    ax = fig.add_subplot(111)
    ax.set_xlim(-8, 8)
    ax.set_ylim(-2, 10)
    ax.axis('off')
    
    # Sfondo con gradiente sottile
    for i in range(10):
        rect = plt.Rectangle((-8, -2+i*1.2), 16, 1.2, 
                            facecolor=COLORS['bg_light'], 
                            alpha=0.05-i*0.005, zorder=0)
        ax.add_patch(rect)
    
    # =================================================================
    # LIVELLO STRATEGICO
    # =================================================================
    
    # Consiglio di Amministrazione
    cda_box = FancyBboxPatch((-2.5, 8), 5, 1.2,
                            boxstyle="round,pad=0.05",
                            facecolor=COLORS['strategic'],
                            edgecolor='white',
                            linewidth=3,
                            zorder=3)
    ax.add_patch(cda_box)
    
    # Icona CdA
    ax.text(-2, 8.6, '👥', fontsize=20, ha='left', va='center', zorder=4)
    ax.text(0, 8.6, 'CONSIGLIO DI\nAMMINISTRAZIONE', 
           fontsize=12, fontweight='bold',
           color=COLORS['text_light'], ha='center', va='center',
           zorder=4)
    
    # Comitato Governance Conformità
    comitato_box = FancyBboxPatch((-2.5, 5.5), 5, 1.2,
                                 boxstyle="round,pad=0.05",
                                 facecolor=COLORS['strategic'],
                                 edgecolor='white',
                                 linewidth=3,
                                 alpha=0.9,
                                 zorder=3)
    ax.add_patch(comitato_box)
    
    ax.text(-2, 6.1, '🎯', fontsize=20, ha='left', va='center', zorder=4)
    ax.text(0, 6.1, 'COMITATO\nGOVERNANCE CONFORMITÀ', 
           fontsize=12, fontweight='bold',
           color=COLORS['text_light'], ha='center', va='center',
           zorder=4)
    
    # Connessione CdA -> Comitato
    ax.plot([0, 0], [7.8, 6.7], color=COLORS['strategic'], 
           linewidth=4, zorder=2)
    
    # Label Livello Strategico
    strategic_label = FancyBboxPatch((-7.5, 6.5), 1.8, 2.8,
                                    boxstyle="round,pad=0.05",
                                    facecolor=COLORS['strategic'],
                                    alpha=0.1,
                                    edgecolor=COLORS['strategic'],
                                    linewidth=2,
                                    linestyle='--',
                                    zorder=1)
    ax.add_patch(strategic_label)
    ax.text(-6.6, 7.9, 'LIVELLO\nSTRATEGICO', fontsize=10, 
           fontweight='bold', color=COLORS['strategic'],
           ha='center', va='center', rotation=90)
    
    # =================================================================
    # LIVELLO TATTICO
    # =================================================================
    
    # Centro di Eccellenza Conformità
    cec_box = FancyBboxPatch((-5, 3), 4, 1,
                            boxstyle="round,pad=0.05",
                            facecolor=COLORS['tactical'],
                            edgecolor='white',
                            linewidth=3,
                            zorder=3)
    ax.add_patch(cec_box)
    
    ax.text(-4.5, 3.5, '🏆', fontsize=18, ha='left', va='center', zorder=4)
    ax.text(-3, 3.5, 'Centro di Eccellenza\nConformità', 
           fontsize=11, fontweight='bold',
           color=COLORS['text_light'], ha='center', va='center',
           zorder=4)
    
    # Risk Management
    risk_box = FancyBboxPatch((1, 3), 4, 1,
                            boxstyle="round,pad=0.05",
                            facecolor=COLORS['tactical'],
                            edgecolor='white',
                            linewidth=3,
                            zorder=3)
    ax.add_patch(risk_box)
    
    ax.text(1.5, 3.5, '⚠️', fontsize=18, ha='left', va='center', zorder=4)
    ax.text(3, 3.5, 'Risk\nManagement', 
           fontsize=11, fontweight='bold',
           color=COLORS['text_light'], ha='center', va='center',
           zorder=4)
    
    # Connessioni Strategico -> Tattico
    ax.plot([0, -3], [5.5, 4], color=COLORS['strategic'], 
           linewidth=3, alpha=0.7, zorder=2)
    ax.plot([0, 3], [5.5, 4], color=COLORS['strategic'], 
           linewidth=3, alpha=0.7, zorder=2)
    
    # Label Livello Tattico
    tactical_label = FancyBboxPatch((-7.5, 2.5), 1.8, 2,
                                   boxstyle="round,pad=0.05",
                                   facecolor=COLORS['tactical'],
                                   alpha=0.1,
                                   edgecolor=COLORS['tactical'],
                                   linewidth=2,
                                   linestyle='--',
                                   zorder=1)
    ax.add_patch(tactical_label)
    ax.text(-6.6, 3.5, 'LIVELLO\nTATTICO', fontsize=10, 
           fontweight='bold', color=COLORS['tactical'],
           ha='center', va='center', rotation=90)
    
    # =================================================================
    # LIVELLO OPERATIVO
    # =================================================================
    
    # Box operativi con design moderno
    operational_boxes = [
        (-6, 0.5, '🛡️', 'SOC', COLORS['operational']),
        (-3.5, 0.5, '⚙️', 'IT Ops', COLORS['operational']),
        (-1, 0.5, '🏢', 'Business\nUnits', COLORS['operational']),
        (1.5, 0.5, '🔍', 'Internal\nAudit', COLORS['danger']),
        (4, 0.5, '⚖️', 'Legal &\nCompliance', COLORS['info']),
    ]
    
    for x, y, icon, text, color in operational_boxes:
        # Effetto ombra
        shadow = FancyBboxPatch((x-0.9, y-0.35), 2, 0.8,
                               boxstyle="round,pad=0.03",
                               facecolor='gray',
                               alpha=0.2,
                               edgecolor='none',
                               zorder=2)
        ax.add_patch(shadow)
        
        # Box principale
        box = FancyBboxPatch((x-0.85, y-0.3), 2, 0.8,
                            boxstyle="round,pad=0.03",
                            facecolor=color,
                            edgecolor='white',
                            linewidth=2,
                            zorder=3)
        ax.add_patch(box)
        
        # Icona e testo
        ax.text(x-0.5, y+0.1, icon, fontsize=14, ha='left', va='center', zorder=4)
        ax.text(x+0.3, y+0.1, text, fontsize=9, fontweight='bold',
               color=COLORS['text_light'], ha='center', va='center',
               zorder=4)
    
    # Connessioni Tattico -> Operativo
    connections_ops = [
        (-3, 3, -6, 1.3),
        (-3, 3, -3.5, 1.3),
        (-3, 3, -1, 1.3),
        (3, 3, 1.5, 1.3),
        (3, 3, 4, 1.3),
    ]
    
    for x1, y1, x2, y2 in connections_ops:
        ax.plot([x1, x2], [y1, y2], color=COLORS['tactical'], 
               linewidth=2, alpha=0.6, zorder=2)
    
    # Label Livello Operativo
    operational_label = FancyBboxPatch((-7.5, 0), 1.8, 1.5,
                                      boxstyle="round,pad=0.05",
                                      facecolor=COLORS['operational'],
                                      alpha=0.1,
                                      edgecolor=COLORS['operational'],
                                      linewidth=2,
                                      linestyle='--',
                                      zorder=1)
    ax.add_patch(operational_label)
    ax.text(-6.6, 0.75, 'LIVELLO\nOPERATIVO', fontsize=10, 
           fontweight='bold', color=COLORS['operational'],
           ha='center', va='center', rotation=90)
    
    # =================================================================
    # FRECCE DI REPORTING E AUDIT
    # =================================================================
    
    # Freccia Report (blu)
    report_arrow = FancyArrowPatch((-5.5, 0.5), (-2, 5),
                                 connectionstyle="arc3,rad=0.5",
                                 arrowstyle='-|>',
                                 mutation_scale=25,
                                 linewidth=2,
                                 color=COLORS['info'],
                                 linestyle='--',
                                 alpha=0.7,
                                 zorder=2)
    ax.add_patch(report_arrow)
    ax.text(-4.5, 2.5, 'Report', fontsize=9, 
           color=COLORS['info'], fontweight='bold',
           rotation=60)
    
    # Freccia Audit (rosso)
    audit_arrow = FancyArrowPatch((2, 0.5), (1, 5),
                                connectionstyle="arc3,rad=-0.5",
                                arrowstyle='-|>',
                                mutation_scale=25,
                                linewidth=2,
                                color=COLORS['danger'],
                                linestyle='--',
                                alpha=0.7,
                                zorder=2)
    ax.add_patch(audit_arrow)
    ax.text(2.5, 2.5, 'Audit', fontsize=9, 
           color=COLORS['danger'], fontweight='bold',
           rotation=-60)
    
    # =================================================================
    # BOX INFORMATIVO MEMBRI COMITATO
    # =================================================================
    
    info_box = FancyBboxPatch((4.5, 5), 3, 2.7,
                             boxstyle="round,pad=0.1",
                             facecolor='white',
                             edgecolor=COLORS['strategic'],
                             linewidth=2,
                             zorder=3)
    ax.add_patch(info_box)
    
    ax.text(6, 7.3, '📋 MEMBRI COMITATO', fontsize=10, 
           fontweight='bold', color=COLORS['strategic'],
           ha='center', va='center')
    
    members = [
        ('👔', 'Chief Risk Officer', '(Presidente)'),
        ('🔒', 'CISO', ''),
        ('🛡️', 'DPO', ''),
        ('💰', 'CFO', ''),
        ('⚖️', 'Head of Compliance', ''),
    ]
    
    for i, (icon, title, role) in enumerate(members):
        y_pos = 6.7 - i*0.35
        ax.text(4.8, y_pos, icon, fontsize=10, ha='left', va='center')
        ax.text(5.2, y_pos, title, fontsize=9, ha='left', va='center',
               color=COLORS['text'])
        if role:
            ax.text(6.8, y_pos, role, fontsize=8, ha='left', va='center',
                   color=COLORS['text'], style='italic')
    
    # =================================================================
    # TITOLO E SOTTOTITOLO
    # =================================================================
    
    title = ax.text(0, 9.5, 'MODELLO ORGANIZZATIVO PER LA CONFORMITÀ INTEGRATA', 
                   fontsize=16, fontweight='bold',
                   color=COLORS['strategic'], ha='center', va='center')
    title.set_path_effects([path_effects.SimplePatchShadow(offset=(1, -1), 
                                                          shadow_rgbFace='gray', 
                                                          alpha=0.3),
                          path_effects.Normal()])
    
    ax.text(0, 9, 'Struttura gerarchica e flussi di comunicazione', 
           fontsize=11, style='italic',
           color=COLORS['text'], ha='center', va='center', alpha=0.8)
    
    # Badge con statistiche
    stats_badges = [
        (-5, -1.3, '19', 'Risorse\nTotali', COLORS['tactical']),
        (-2, -1.3, '3', 'Livelli\nGerarchici', COLORS['strategic']),
        (1, -1.3, '5', 'Funzioni\nOperative', COLORS['operational']),
        (4, -1.3, '2', 'Flussi\nReporting', COLORS['info']),
    ]
    
    for x, y, number, label, color in stats_badges:
        badge = Circle((x, y), 0.6, facecolor=color, 
                      edgecolor='white', linewidth=2,
                      alpha=0.9, zorder=3)
        ax.add_patch(badge)
        ax.text(x, y+0.1, number, fontsize=16, fontweight='bold',
               color='white', ha='center', va='center', zorder=4)
        ax.text(x, y-0.25, label, fontsize=8,
               color='white', ha='center', va='center', zorder=4)
    
    plt.tight_layout()
    return fig

def create_plotly_org_chart():
    """
    Versione Plotly interattiva dell'organigramma
    """
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    
    # Colori
    colors = {
        'strategic': '#2E4057',
        'tactical': '#048A81',
        'operational': '#54C6EB',
        'danger': '#C73E1D',
        'info': '#8B80F9',
        'bg': '#F7F7F7',
    }
    
    fig = go.Figure()
    
    # Nodi dell'organigramma
    nodes = {
        # Strategico
        'cda': dict(x=0, y=3, label='Consiglio di<br>Amministrazione', 
                   level='strategic', icon='👥'),
        'comitato': dict(x=0, y=2.5, label='Comitato Governance<br>Conformità', 
                        level='strategic', icon='🎯'),
        
        # Tattico
        'cec': dict(x=-1.5, y=1.5, label='Centro Eccellenza<br>Conformità', 
                   level='tactical', icon='🏆'),
        'risk': dict(x=1.5, y=1.5, label='Risk<br>Management', 
                    level='tactical', icon='⚠️'),
        
        # Operativo
        'soc': dict(x=-2.5, y=0.5, label='SOC', level='operational', icon='🛡️'),
        'it': dict(x=-1.5, y=0.5, label='IT Ops', level='operational', icon='⚙️'),
        'bu': dict(x=-0.5, y=0.5, label='Business Units', level='operational', icon='🏢'),
        'audit': dict(x=1, y=0.5, label='Internal Audit', level='danger', icon='🔍'),
        'legal': dict(x=2, y=0.5, label='Legal &<br>Compliance', level='info', icon='⚖️'),
    }
    
    # Aggiungi i nodi
    for node_id, node_data in nodes.items():
        color = colors.get(node_data['level'], colors['operational'])
        
        # Box del nodo
        fig.add_trace(go.Scatter(
            x=[node_data['x']], 
            y=[node_data['y']],
            mode='markers+text',
            marker=dict(
                size=80,
                color=color,
                line=dict(width=3, color='white'),
            ),
            text=f"{node_data['icon']}<br><b>{node_data['label']}</b>",
            textposition='middle center',
            textfont=dict(size=10, color='white', family='Arial'),
            hovertemplate=f"<b>{node_data['label']}</b><br>Livello: {node_data['level'].title()}<extra></extra>",
            showlegend=False
        ))
    
    # Connessioni gerarchiche
    connections = [
        ('cda', 'comitato'),
        ('comitato', 'cec'),
        ('comitato', 'risk'),
        ('cec', 'soc'),
        ('cec', 'it'),
        ('cec', 'bu'),
        ('risk', 'audit'),
        ('risk', 'legal'),
    ]
    
    for start, end in connections:
        x0, y0 = nodes[start]['x'], nodes[start]['y']
        x1, y1 = nodes[end]['x'], nodes[end]['y']
        
        fig.add_shape(
            type="line",
            x0=x0, y0=y0, x1=x1, y1=y1,
            line=dict(color="gray", width=2)
        )
    
    # Frecce di reporting
    fig.add_annotation(
        x=nodes['audit']['x'], y=nodes['audit']['y'],
        ax=nodes['comitato']['x'], ay=nodes['comitato']['y'],
        xref='x', yref='y',
        axref='x', ayref='y',
        showarrow=True,
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=2,
        arrowcolor=colors['danger'],
        opacity=0.6,
        standoff=40
    )
    
    fig.add_annotation(
        x=nodes['soc']['x'], y=nodes['soc']['y'],
        ax=nodes['comitato']['x']-0.2, ay=nodes['comitato']['y'],
        xref='x', yref='y',
        axref='x', ayref='y',
        showarrow=True,
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=2,
        arrowcolor=colors['info'],
        opacity=0.6,
        standoff=40
    )
    
    # Box per i livelli
    levels_boxes = [
        dict(y0=2.3, y1=3.2, label='LIVELLO STRATEGICO', color=colors['strategic']),
        dict(y0=1.2, y1=1.8, label='LIVELLO TATTICO', color=colors['tactical']),
        dict(y0=0.2, y1=0.8, label='LIVELLO OPERATIVO', color=colors['operational']),
    ]
    
    for level in levels_boxes:
        fig.add_shape(
            type="rect",
            x0=-3.5, x1=3.5,
            y0=level['y0'], y1=level['y1'],
            line=dict(color=level['color'], width=2, dash="dash"),
            fillcolor=level['color'],
            opacity=0.05,
            layer="below"
        )
        
        fig.add_annotation(
            x=-3.2, y=(level['y0'] + level['y1'])/2,
            text=f"<b>{level['label']}</b>",
            showarrow=False,
            font=dict(size=9, color=level['color']),
            textangle=-90
        )
    
    # Box membri comitato
    fig.add_shape(
        type="rect",
        x0=2.5, x1=3.8,
        y0=2, y1=3,
        line=dict(color=colors['strategic'], width=2),
        fillcolor="white",
        layer="below"
    )
    
    members_text = """<b>MEMBRI COMITATO</b>
    
• Chief Risk Officer (Presidente)
• CISO
• DPO  
• CFO
• Head of Compliance"""
    
    fig.add_annotation(
        x=3.15, y=2.5,
        text=members_text,
        showarrow=False,
        font=dict(size=8, color=colors['strategic']),
        align="left",
        bgcolor="white",
        borderpad=4
    )
    
    # Layout
    fig.update_layout(
        title=dict(
            text='<b>Modello Organizzativo per la Conformità Integrata</b><br><sub>Struttura gerarchica interattiva</sub>',
            font=dict(size=18, color=colors['strategic']),
            x=0.5
        ),
        xaxis=dict(visible=False, range=[-4, 4.5]),
        yaxis=dict(visible=False, range=[0, 3.5]),
        height=700,
        hovermode='closest',
        plot_bgcolor=colors['bg'],
        paper_bgcolor='white',
        margin=dict(l=50, r=50, t=100, b=50)
    )
    
    return fig

def save_all_org_charts():
    """
    Salva entrambe le versioni dell'organigramma
    """
    print("\n" + "="*70)
    print("🎨 GENERAZIONE ORGANIGRAMMA MODERNO")
    print("="*70 + "\n")
    
    # Versione Matplotlib
    try:
        fig_matplotlib = create_modern_org_chart()
        
        # Salva in vari formati
        fig_matplotlib.savefig('organigramma_moderno.pdf', 
                              format='pdf', bbox_inches='tight', dpi=300)
        fig_matplotlib.savefig('organigramma_moderno.png', 
                              format='png', bbox_inches='tight', dpi=200)
        fig_matplotlib.savefig('organigramma_moderno.svg', 
                              format='svg', bbox_inches='tight')
        
        print("✅ Versione Matplotlib generata:")
        print("   ├─ PDF: organigramma_moderno.pdf")
        print("   ├─ PNG: organigramma_moderno.png")
        print("   └─ SVG: organigramma_moderno.svg")
        
        plt.close(fig_matplotlib)
        
    except Exception as e:
        print(f"❌ Errore Matplotlib: {e}")
    
    # Versione Plotly (se disponibile)
    try:
        import plotly
        fig_plotly = create_plotly_org_chart()
        
        # Salva HTML interattivo
        fig_plotly.write_html('organigramma_interattivo.html')
        print("\n✅ Versione Plotly generata:")
        print("   └─ HTML: organigramma_interattivo.html (interattivo)")
        
        # Prova export immagini se kaleido disponibile
        try:
            fig_plotly.write_image('organigramma_plotly.pdf', width=1400, height=900)
            fig_plotly.write_image('organigramma_plotly.png', width=1400, height=900, scale=2)
            print("   ├─ PDF: organigramma_plotly.pdf")
            print("   └─ PNG: organigramma_plotly.png")
        except:
            print("   ℹ️  Per export PDF/PNG installa: pip install kaleido")
            
    except ImportError:
        print("\n⚠️  Plotly non installato - solo versione Matplotlib generata")
        print("   Per versione interattiva: pip install plotly")
    
    print("\n" + "="*70)
    print("✨ ORGANIGRAMMA MODERNO COMPLETATO!")
    print("="*70)
    print("\nCaratteristiche del nuovo design:")
    print("• Palette colori professionale e moderna")
    print("• Icone intuitive per ogni funzione")
    print("• Effetti visivi (ombre, gradienti)")
    print("• Layout pulito e gerarchico")
    print("• Badge con statistiche chiave")
    print("• Box informativo membri comitato")
    print("• Frecce di reporting/audit evidenziate")

if __name__ == '__main__':
    save_all_org_charts()
