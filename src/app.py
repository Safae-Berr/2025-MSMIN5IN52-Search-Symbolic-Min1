"""Streamlit front-end for interactive Job-Shop analysis."""

import pandas as pd
import streamlit as st

from data import JobShopInstance, get_instances, instance_horizon
from solver import SolutionResult, solve
from visualization import gantt_figure, operations_dataframe, save_figure


st.set_page_config(page_title="Job-Shop CSP avec OR-Tools", layout="wide")

# Subtle UI theming to make the page more legible.
st.markdown(
    """
    <style>
    .main { padding: 1.5rem 2rem; }
    .metric-card { background: #f7f9fb; padding: 12px 14px; border-radius: 8px; border: 1px solid #e2e8f0; }
    .hero { background: linear-gradient(135deg, #eef6ff, #f8fbff); padding: 16px 18px; border-radius: 10px; border: 1px solid #dce7f7; }
    </style>
    """,
    unsafe_allow_html=True,
)


# Simple cache to avoid re-solving identical instances repeatedly during UI exploration.
@st.cache_data(show_spinner=False)
def cached_solve(instance_name: str, time_limit: float | None, num_workers: int = 8) -> SolutionResult:
    instances = get_instances()
    instance = instances[instance_name]
    return solve(instance=instance, time_limit=time_limit, num_workers=num_workers)


def describe_instance(instance: JobShopInstance):
    st.subheader("Instance")
    st.caption(instance.description)
    nb_jobs = len(instance.jobs)
    nb_ops = sum(len(job.operations) for job in instance.jobs)
    horizon = instance_horizon(instance)
    cols = st.columns(4)
    cols[0].metric("Commandes / Jobs", nb_jobs)
    cols[1].metric("Ressources", len(instance.machines))
    cols[2].metric("Operations", nb_ops)
    cols[3].metric("Horizon max", horizon)

    machines_list = " • ".join(instance.machines)
    st.markdown(f"**Ressources impliquees:** {machines_list}")
    etapes = {op.label for job in instance.jobs for op in job.operations}
    st.markdown(
        f"**Etapes typiques:** {', '.join(sorted(etapes))}"
    )
    rows = []
    for job in instance.jobs:
        for op in job.operations:
            rows.append(
                {
                    "Job": job.job_id,
                    "Etape": op.label,
                    "Operation": op.op_id,
                    "Machine": op.machine,
                    "Duree": op.duration,
                }
            )
    st.dataframe(rows, use_container_width=True, hide_index=True)

def machine_utilization(df: pd.DataFrame) -> pd.DataFrame:
    """Compute per-machine load and utilization."""
    if df.empty:
        return pd.DataFrame(columns=["machine", "workload", "utilisation_%", "horizon"])
    horizon = df["end"].max()
    util = (
        df.groupby("machine")["duration"]
        .sum()
        .reset_index()
        .rename(columns={"duration": "workload"})
    )
    util["utilisation_%"] = (util["workload"] / horizon * 100).round(1)
    util["horizon"] = horizon
    return util


def show_solution(solution: SolutionResult, zoom_max: int):
    if solution.makespan is None:
        st.error(f"Aucune solution: statut {solution.status}")
        return

    st.subheader("Solution CP-SAT")
    st.caption("Synthese de la meilleure solution trouvee.")
    col1, col2, col3 = st.columns(3)
    col1.metric("Statut", solution.status)
    col2.metric("Makespan", f"{solution.makespan} unites")
    col3.metric("Temps solveur (s)", f"{solution.solver_statistics.get('wall_time', 0):.3f}")
    col4, col5, col6 = st.columns(3)
    col4.metric("Borne inferieure", f"{solution.solver_statistics.get('best_bound', 0):.2f}")
    col5.metric("Conflits", f"{solution.solver_statistics.get('conflicts', 0):.0f}")
    col6.metric("Branches", f"{solution.solver_statistics.get('branches', 0):.0f}")

    df = operations_dataframe(solution)
    st.markdown("Ordonnancement detaille (operations triees par machine/start)")
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.subheader("Diagramme de Gantt")
    st.caption("Couleurs par commande, axe Y = ressources (stations), ligne verticale = makespan.")
    fig = gantt_figure(solution, maintenance=st.session_state.get("maintenance_for_plot", []), x_max=zoom_max)
    if fig is not None:
        fig.update_layout(height=520, plot_bgcolor="#fbfdff")
        st.plotly_chart(fig, use_container_width=True)
        if st.button("Exporter le Gantt en PNG"):
            destination = save_figure(fig)
            st.success(f"Export enregistre dans {destination}")
    else:
        st.warning("Aucune figure a afficher (solution vide).")


def show_insights(solution: SolutionResult, baseline: SolutionResult | None):
    st.subheader("Insights pedagogiques")
    current_ms = solution.makespan or 0
    base_ms = baseline.makespan if baseline else None
    delta = None if base_ms is None else current_ms - base_ms
    col1, col2, col3 = st.columns(3)
    col1.metric("Makespan scenario", f"{current_ms} unites")
    if base_ms is not None:
        col2.metric("Delta vs baseline", f"{delta:+} unites", delta=delta)
    else:
        col2.metric("Delta vs baseline", "N/A")
    col3.metric("Conflits CP-SAT", f"{solution.solver_statistics.get('conflicts', 0):.0f}")

    df = operations_dataframe(solution)
    util = machine_utilization(df)
    if not util.empty:
        st.markdown("Utilisation par ressource (sur le planning obtenu)")
        st.dataframe(util, hide_index=True, use_container_width=True)
    with st.expander("Comment lire ces resultats ?", expanded=False):
        st.markdown(
            "- Le delta de makespan montre l'effet des contraintes (maintenance ou rush) par rapport au flux nominal.\n"
            "- Les conflits CP-SAT refletent la difficulte de la recherche (plus il y en a, plus le probleme est serre).\n"
            "- L'utilisation par ressource indique les goulets d'etranglement (utilisation proche de 100%)."
        )


def main():
    st.title("Ordonnancement Job-Shop par CSP (OR-Tools CP-SAT)")
    st.markdown(
        """
        <div class="hero">
        <strong>Cas d'usage realiste :</strong> orchestration d'un flux logistique (picking, emballage, etiquetage, depart camion).
        Modele declaratif: variables d'intervalle, precedences intra-commande, non-chevauchement machine, objectif de makespan minimal.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption(
        "Choisissez une instance, ajustez la limite de temps et lancez la resolution. "
        "La visualisation est analytique (pas de retroaction sur le solveur)."
    )
    with st.expander("Pourquoi c'est de l'IA (symbolique / CP) ?", expanded=False):
        st.markdown(
            "- Etat = positions temporelles des operations; actions = placer une operation; but = minimiser le makespan.\n"
            "- Connaissances = contraintes explicites (precedence, non-chevauchement, maintenance). Recherche = CP-SAT.\n"
            "- Ce bac a sable permet de voir l'effet des contraintes (maintenance, rush) sur le planning et le critere."
        )
    with st.expander("Mode d'emploi rapide", expanded=True):
        st.markdown(
            "1. Selectionnez un **scenario** (simpliste, maintenance, rush) dans le menu de gauche.\n"
            "2. Cliquez sur **Resoudre / Recalculer**.\n"
            "3. Lisez la section **Insights pedagogiques** pour comprendre l'impact sur le makespan et l'utilisation machines.\n"
            "4. Observez le Gantt et les metrics solveur (makespan, conflits CP-SAT).\n"
            "5. Changez de scenario pour comparer: les deltas vs baseline s'ajustent automatiquement."
        )

    instances = get_instances()
    instance_names = list(instances.keys())
    scenario_labels = {
        "preparation_commandes": "Scenario simpliste (flux nominal)",
        "preparation_commandes_maintenance": "Scenario complique (maintenance planifiee)",
        "preparation_commandes_rush": "Scenario rush (commande flash R99)",
    }
    baseline_key = "preparation_commandes"

    with st.sidebar:
        st.header("Configuration solveur")
        chosen = st.selectbox(
            "Scenario",
            options=instance_names,
            format_func=lambda k: scenario_labels.get(k, k),
            index=0,
            help="Simpliste: flux nominal. Complique: maintenance. Rush: commande flash prioritaire.",
        )
        instance = instances[chosen]
        horizon = instance_horizon(instance)
        st.session_state["maintenance_for_plot"] = instance.maintenance
        time_limit = st.slider(
            "Limite de temps solveur (secondes, 0 = sans limite)", 0.0, 60.0, 8.0, step=0.5
        )
        zoom_max = st.slider(
            "Zoom temporel (borne max)",
            min_value=max(5, horizon // 2),
            max_value=max(20, horizon * 2),
            value=max(20, int(horizon * 1.2)),
            step=1,
            help="Ajustez pour recadrer l'axe temps du Gantt.",
        )
        run_requested = st.button("Resoudre / Recalculer", type="primary")

    scenario_tips = {
        "preparation_commandes": "Flux nominal: observe l'enchainement naturel des 3 commandes.",
        "preparation_commandes_maintenance": "Maintenance: note les blocs grises qui bloquent les ressources et decalent le planning.",
        "preparation_commandes_rush": "Commande flash R99: verifiez si elle se glisse avant certaines etapes des autres commandes.",
    }
    st.info(scenario_labels.get(chosen, instance.description))
    st.caption(scenario_tips.get(chosen, ""))
    describe_instance(instance)

    if "ran_once" not in st.session_state:
        st.session_state["ran_once"] = True
        run_requested = True

    if run_requested:
        with st.spinner("Resolution en cours..."):
            solution = cached_solve(chosen, time_limit if time_limit > 0 else None)
            baseline_solution = cached_solve(baseline_key, time_limit if time_limit > 0 else None)
        show_insights(solution, baseline_solution)
        show_solution(solution, zoom_max=zoom_max)


if __name__ == "__main__":
    main()
