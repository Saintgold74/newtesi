% ============================================================================
% Diagrammi TikZ per il Capitolo 3
% Da inserire nel documento LaTeX principale
% ============================================================================

% Preambolo necessario (da aggiungere nel preambolo del documento principale):
% \usepackage{tikz}
% \usepackage{pgfplots}
% \pgfplotsset{compat=1.17}
% \usetikzlibrary{shapes,arrows,positioning,calc,patterns,decorations.pathreplacing,shadows}
% \usetikzlibrary{shapes.geometric,shapes.symbols,shapes.misc}
% \usetikzlibrary{matrix,chains,scopes,fit,backgrounds}

% ============================================================================
% FIGURA 3.2b: Evoluzione dell'Architettura di Rete (Diagramma Architetturale)
% ============================================================================

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
    % Stili
    \tikzstyle{hub} = [circle, draw, fill=red!30, minimum size=1.5cm, font=\small]
    \tikzstyle{spoke} = [circle, draw, fill=blue!20, minimum size=1cm, font=\tiny]
    \tikzstyle{edge} = [rectangle, draw, fill=green!20, minimum size=0.8cm, font=\tiny]
    \tikzstyle{cloud} = [cloud, draw, fill=yellow!20, minimum width=2cm, minimum height=1.5cm, font=\small]
    \tikzstyle{arrow} = [thick,->,>=stealth]
    \tikzstyle{line} = [thick]
    \tikzstyle{dashedline} = [thick, dashed]
    
    % Legacy Hub-and-Spoke (Sinistra)
    \begin{scope}[shift={(0,0)}]
        \node[hub] (hub1) at (0,0) {HQ};
        \foreach \i/\angle in {1/0,2/60,3/120,4/180,5/240,6/300} {
            \node[spoke] (spoke1-\i) at (\angle:2.5cm) {PV\i};
            \draw[line] (hub1) -- (spoke1-\i);
        }
        \node[below=3cm of hub1, font=\footnotesize\bfseries] {Legacy Hub-and-Spoke};
        \node[below=3.5cm of hub1, font=\tiny, text=red] {MTTR: 4.7h};
    \end{scope}
    
    % Hybrid SD-WAN (Centro)
    \begin{scope}[shift={(7,0)}]
        \node[hub] (hub2) at (0,0) {SD-WAN\\Controller};
        \node[cloud] (cloud2) at (0,2.5) {Cloud};
        \foreach \i/\angle in {1/0,2/60,3/120,4/180,5/240,6/300} {
            \node[spoke] (spoke2-\i) at (\angle:2.5cm) {PV\i};
            \draw[line] (hub2) -- (spoke2-\i);
            \draw[dashedline, gray] (spoke2-\i) -- (cloud2);
        }
        \draw[arrow, very thick, blue] (hub2) -- (cloud2);
        \node[below=3cm of hub2, font=\footnotesize\bfseries] {Hybrid SD-WAN};
        \node[below=3.5cm of hub2, font=\tiny, text=orange] {MTTR: 2.3h};
    \end{scope}
    
    % Full Mesh SD-WAN (Destra)
    \begin{scope}[shift={(14,0)}]
        \node[cloud] (cloud3) at (0,0) {Multi-Cloud\\Orchestrator};
        \foreach \i/\angle/\y in {1/30/1.5,2/90/1.5,3/150/1.5,4/210/1.5,5/270/1.5,6/330/1.5} {
            \node[edge] (edge3-\i) at (\angle:2.5cm) {Edge\i};
            \draw[arrow, green!60!black] (cloud3) -- (edge3-\i);
        }
        % Mesh connections
        \foreach \i in {1,...,5} {
            \foreach \j in {\i,...,6} {
                \ifnum\i<\j
                    \draw[dashedline, gray!50, very thin] (edge3-\i) -- (edge3-\j);
                \fi
            }
        }
        \node[below=3cm of cloud3, font=\footnotesize\bfseries] {Full Mesh SD-WAN};
        \node[below=3.5cm of cloud3, font=\tiny, text=green!60!black] {MTTR: 1.2h};
    \end{scope}
    
    % Frecce di evoluzione
    \draw[arrow, ultra thick, orange, ->] (3,-1) -- (4.5,-1) node[midway, above, font=\small] {Fase 1};
    \draw[arrow, ultra thick, orange, ->] (10,-1) -- (11.5,-1) node[midway, above, font=\small] {Fase 2};
\end{tikzpicture}
\caption{Evoluzione dell'Architettura di Rete: Dal Legacy Hub-and-Spoke al Full Mesh SD-WAN}
\label{fig:network_evolution_arch}
\end{figure}

% ============================================================================
% FIGURA 3.3b: Architettura Multi-Cloud di Riferimento per la GDO
% ============================================================================

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=1.0]
    % Stili
    \tikzstyle{cloudprovider} = [cloud, draw, minimum width=3cm, minimum height=2cm, font=\small\bfseries]
    \tikzstyle{workload} = [rectangle, rounded corners, draw, minimum width=2cm, minimum height=0.8cm, font=\tiny]
    \tikzstyle{component} = [rectangle, draw, minimum width=1.8cm, minimum height=0.6cm, font=\tiny]
    \tikzstyle{cmp} = [rectangle, draw, fill=yellow!30, minimum width=8cm, minimum height=1.2cm, font=\small\bfseries]
    \tikzstyle{store} = [rectangle, draw, fill=gray!20, minimum width=1.5cm, minimum height=0.8cm, font=\tiny]
    
    % Cloud Management Platform
    \node[cmp] (cmp) at (0,5) {Cloud Management Platform (CMP)};
    \node[below=0.1cm of cmp, font=\tiny] {Governance | Cost Optimization | Security Policy | Compliance};
    
    % Cloud Providers
    \node[cloudprovider, fill=blue!20] (aws) at (-5,2) {AWS};
    \node[cloudprovider, fill=green!20] (azure) at (0,2) {Azure};
    \node[cloudprovider, fill=red!20] (gcp) at (5,2) {GCP};
    
    % Workloads in AWS
    \node[workload, fill=blue!10] (aws-iaas) at (-5,0.5) {IaaS\\Legacy Apps};
    \node[workload, fill=blue!10] (aws-storage) at (-5,-0.5) {S3\\Cold Storage};
    
    % Workloads in Azure
    \node[workload, fill=green!10] (azure-paas) at (0,0.5) {PaaS\\Development};
    \node[workload, fill=green!10] (azure-ai) at (0,-0.5) {AI/ML\\Services};
    
    % Workloads in GCP
    \node[workload, fill=red!10] (gcp-k8s) at (5,0.5) {GKE\\Containers};
    \node[workload, fill=red!10] (gcp-analytics) at (5,-0.5) {BigQuery\\Analytics};
    
    % On-Premise
    \node[rectangle, draw, fill=orange!20, minimum width=4cm, minimum height=2cm] (onprem) at (-5,-3) {On-Premise DC};
    \node[component, fill=orange!10] (critical) at (-5,-2.5) {Critical Systems};
    \node[component, fill=orange!10] (compliance) at (-5,-3.5) {PCI-DSS Scope};
    
    % Edge Locations
    \node[store] (store1) at (2,-3) {Store 1};
    \node[store] (store2) at (4,-3) {Store 2};
    \node[store] (storen) at (6,-3) {Store N};
    \node[above=0.1cm of store2, font=\tiny\bfseries] {Edge Locations};
    
    % Connections
    \draw[thick, <->] (cmp) -- (aws);
    \draw[thick, <->] (cmp) -- (azure);
    \draw[thick, <->] (cmp) -- (gcp);
    
    \draw[thick, ->] (aws) -- (aws-iaas);
    \draw[thick, ->] (aws) -- (aws-storage);
    \draw[thick, ->] (azure) -- (azure-paas);
    \draw[thick, ->] (azure) -- (azure-ai);
    \draw[thick, ->] (gcp) -- (gcp-k8s);
    \draw[thick, ->] (gcp) -- (gcp-analytics);
    
    % Hybrid connections
    \draw[thick, dashed, <->, orange] (onprem) -- (aws);
    \draw[thick, dashed, <->, orange] (onprem) -- (azure);
    
    % Edge connections
    \draw[thick, dotted, ->] (store1) -- (gcp);
    \draw[thick, dotted, ->] (store2) -- (gcp);
    \draw[thick, dotted, ->] (storen) -- (gcp);
    \draw[thick, dotted, <->] (store2) -- (onprem);
    
    % Labels for connection types
    \node[font=\tiny, text=orange] at (-6.5,-1) {VPN/Direct\\Connect};
    \node[font=\tiny, text=gray] at (4,-1.5) {Edge\\Computing};
    
    % Cost distribution pie (simplified representation)
    \begin{scope}[shift={(9,0)}]
        \node[font=\small\bfseries] at (0,2) {Distribuzione Costi};
        \draw[fill=blue!30] (0,0) -- (0:1.5cm) arc (0:120:1.5cm) -- cycle;
        \draw[fill=green!30] (0,0) -- (120:1.5cm) arc (120:210:1.5cm) -- cycle;
        \draw[fill=red!30] (0,0) -- (210:1.5cm) arc (210:300:1.5cm) -- cycle;
        \draw[fill=orange!30] (0,0) -- (300:1.5cm) arc (300:360:1.5cm) -- cycle;
        
        \node[font=\tiny] at (60:2cm) {AWS 33\%};
        \node[font=\tiny] at (165:2cm) {Azure 25\%};
        \node[font=\tiny] at (255:2cm) {GCP 25\%};
        \node[font=\tiny] at (330:2cm) {On-Prem 17\%};
    \end{scope}
    
    % Performance metrics
    \node[rectangle, draw, fill=white, align=left, font=\tiny] at (9,-3) {
        \textbf{KPI Target:}\\
        Availability: 99.96\%\\
        Latency: <50ms\\
        TCO: -38.2\%\\
        ASSA: -42.7\%
    };
\end{tikzpicture}
\caption{Architettura Multi-Cloud di Riferimento per la GDO con Distribuzione Workload}
\label{fig:multicloud_architecture}
\end{figure}

% ============================================================================
% FIGURA 3.6: Framework Integrato - Dall'Infrastruttura alla Compliance
% ============================================================================

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.85]
    % Stili
    \tikzstyle{layer} = [rectangle, draw, minimum width=10cm, minimum height=1.5cm, font=\small\bfseries]
    \tikzstyle{component} = [rectangle, rounded corners, draw, minimum width=2cm, minimum height=0.8cm, font=\tiny]
    \tikzstyle{arrow} = [thick, ->, >=stealth]
    \tikzstyle{biarrow} = [thick, <->, >=stealth]
    \tikzstyle{metric} = [rectangle, draw, fill=yellow!20, minimum width=1.5cm, minimum height=0.6cm, font=\tiny]
    
    % Layer 1: Fondamenta Fisiche
    \node[layer, fill=gray!30] (physical) at (0,0) {Fondamenta Fisiche};
    \node[component, fill=gray!20] (power) at (-3,-0.5) {Power\\2N Config};
    \node[component, fill=gray!20] (cooling) at (0,-0.5) {Cooling\\PUE 1.22};
    \node[component, fill=gray!20] (network) at (3,-0.5) {Network\\Connectivity};
    
    % Layer 2: Infrastruttura di Rete
    \node[layer, fill=blue!30] (network_layer) at (0,-2.5) {Evoluzione Rete};
    \node[component, fill=blue!20] (sdwan) at (-3,-3) {SD-WAN};
    \node[component, fill=blue!20] (edge) at (0,-3) {Edge\\Computing};
    \node[component, fill=blue!20] (mesh) at (3,-3) {Full Mesh};
    
    % Layer 3: Cloud Transformation
    \node[layer, fill=green!30] (cloud) at (0,-5) {Trasformazione Cloud};
    \node[component, fill=green!20] (hybrid) at (-3,-5.5) {Hybrid\\Cloud};
    \node[component, fill=green!20] (multicloud) at (0,-5.5) {Multi-Cloud\\Orchestration};
    \node[component, fill=green!20] (native) at (3,-5.5) {Cloud\\Native};
    
    % Layer 4: Security Architecture
    \node[layer, fill=red!30] (security) at (0,-7.5) {Architettura di Sicurezza};
    \node[component, fill=red!20] (zerotrust) at (-3,-8) {Zero Trust\\-42.7\% ASSA};
    \node[component, fill=red!20] (microseg) at (0,-8) {Micro-\\segmentation};
    \node[component, fill=red!20] (sase) at (3,-8) {SASE/\\SSE};
    
    % Layer 5: Compliance
    \node[layer, fill=purple!30] (compliance) at (0,-10) {Compliance Integrata};
    \node[component, fill=purple!20] (pcidss) at (-3,-10.5) {PCI-DSS\\4.0};
    \node[component, fill=purple!20] (gdpr) at (0,-10.5) {GDPR};
    \node[component, fill=purple!20] (nis2) at (3,-10.5) {NIS2};
    
    % Vertical connections
    \foreach \i in {power,cooling,network} {
        \draw[arrow, gray] (\i) -- (network_layer);
    }
    \foreach \i in {sdwan,edge,mesh} {
        \draw[arrow, blue] (\i) -- (cloud);
    }
    \foreach \i in {hybrid,multicloud,native} {
        \draw[arrow, green] (\i) -- (security);
    }
    \foreach \i in {zerotrust,microseg,sase} {
        \draw[arrow, red] (\i) -- (compliance);
    }
    
    % Metrics on the right
    \node[metric] (availability) at (6.5,-1) {Availability\\99.96\%};
    \node[metric] (mttr) at (6.5,-3.5) {MTTR\\1.2h};
    \node[metric] (tco) at (6.5,-5.5) {TCO\\-38.2\%};
    \node[metric] (assa) at (6.5,-8) {ASSA\\-42.7\%};
    \node[metric] (comp_cost) at (6.5,-10.5) {Compliance\\Cost -37.8\%};
    
    % Connect metrics to layers
    \draw[biarrow, gray!50] (physical) -- (availability);
    \draw[biarrow, blue!50] (network_layer) -- (mttr);
    \draw[biarrow, green!50] (cloud) -- (tco);
    \draw[biarrow, red!50] (security) -- (assa);
    \draw[biarrow, purple!50] (compliance) -- (comp_cost);
    
    % ROI Timeline on the left
    \begin{scope}[shift={(-7,-5.5)}]
        \node[font=\small\bfseries] at (0,3) {ROI Timeline};
        \draw[thick] (0,2.5) -- (0,-3);
        \draw[thick] (-0.1,2.5) -- (0.1,2.5) node[right, font=\tiny] {0 mesi};
        \draw[thick] (-0.1,1) -- (0.1,1) node[right, font=\tiny] {6 mesi};
        \draw[thick] (-0.1,-0.5) -- (0.1,-0.5) node[right, font=\tiny] {18 mesi};
        \draw[thick] (-0.1,-2) -- (0.1,-2) node[right, font=\tiny] {30 mesi};
        \draw[thick] (-0.1,-3) -- (0.1,-3) node[right, font=\tiny] {36 mesi};
        
        \draw[thick, green, ->] (0.2,2.5) -- (0.2,-3) node[below, font=\tiny] {ROI 237\%};
    \end{scope}
    
    % Title
    \node[font=\large\bfseries] at (0,2) {Framework GIST: Stack Integrato di Trasformazione};
    
    % Legend
    \begin{scope}[shift={(0,-12.5)}]
        \draw[arrow] (0,0) -- (1,0) node[right, font=\tiny] {Dipendenza diretta};
        \draw[biarrow] (3,0) -- (4,0) node[right, font=\tiny] {Impatto bidirezionale};
    \end{scope}
\end{tikzpicture}
\caption{Framework Integrato GIST: Dall'Infrastruttura Fisica alla Compliance}
\label{fig:framework_integrato}
\end{figure}

% ============================================================================
% Tabella Comparativa per Sezione 3.2 (come suggerito nel feedback)
% ============================================================================

\begin{table}[htbp]
\centering
\caption{Analisi Comparativa delle Configurazioni di Ridondanza Power}
\label{tab:power_redundancy_comparison}
\begin{tabular}{lcccccc}
\hline
\textbf{Configurazione} & \textbf{MTBF} & \textbf{Availability} & \textbf{Costo} & \textbf{PUE} & \textbf{Payback} & \textbf{Raccomandazione} \\
 & \textbf{(ore)} & \textbf{(\%)} & \textbf{Relativo} & \textbf{Tipico} & \textbf{(mesi)} & \\
\hline
\hline
N+1 & 52.560 & 99.82 & 100 & 1.82 & -- & Minimo per\\
 & (±3.840) & (±0.12) & (baseline) & (±0.12) & & ambienti critici\\
\hline
2N & 175.200 & 99.94 & 143 & 1.65 & 28 & Standard per\\
 & (±12.100) & (±0.04) & (±8) & (±0.09) & (±4) & GDO moderna\\
\hline
2N+1 & 350.400 & 99.97 & 186 & 1.58 & 42 & Solo per\\
 & (±24.300) & (±0.02) & (±12) & (±0.07) & (±6) & ultra-critical\\
\hline
N+1 con ML* & 69.141 & 99.88 & 112 & 1.40 & 14 & Best practice\\
 & (±4.820) & (±0.08) & (±5) & (±0.08) & (±2) & costo-efficacia\\
\hline
\end{tabular}
\vspace{0.2cm}
\begin{flushleft}
\footnotesize
*N+1 con Machine Learning predittivo per manutenzione preventiva\\
IC 95\% mostrati tra parentesi\\
Fonte: Aggregazione dati da 23 implementazioni GDO (2020-2024)
\end{flushleft}
\end{table}

% ============================================================================
% Box di Sintesi per l'inizio del Capitolo (come suggerito nel feedback)
% ============================================================================

\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{Executive Summary - Capitolo 3}]
\textbf{Key Findings:}
\begin{itemize}[leftmargin=*,noitemsep,topsep=0pt]
    \item \textbf{H1 Validata}: Architetture cloud-ibride raggiungono SLA >99.95\% nell'84.3\% dei casi con riduzione TCO del 38.2\%
    \item \textbf{H2 Confermata}: Zero Trust riduce ASSA del 42.7\% mantenendo latenza <50ms nel 94\% delle transazioni
    \item \textbf{H3 Supportata}: Multi-cloud contribuisce 27.3\% alla riduzione costi compliance con ROI positivo in 18 mesi
\end{itemize}

\textbf{Implicazioni Pratiche:}
\begin{itemize}[leftmargin=*,noitemsep,topsep=0pt]
    \item Investimento iniziale €8-10M per organizzazione media (100 PV)
    \item Payback period: 15.7 mesi (mediana)
    \item ROI a 36 mesi: 237\%
\end{itemize}

\textbf{Raccomandazione}: Approccio progressivo in 3 fasi con quick wins iniziali per autofinanziare trasformazione completa.
\end{tcolorbox}