"""Generate the writeup's plots from analysis CSVs into visuals/."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis"
OUT = ROOT / "visuals"
OUT.mkdir(exist_ok=True)

FONT_DIR = Path(__file__).resolve().parent / "fonts"
for ttf in FONT_DIR.glob("*.ttf"):
    font_manager.fontManager.addfont(str(ttf))

plt.rcParams.update({
    "figure.dpi": 140,
    "savefig.bbox": "tight",
    "font.size": 10,
    "font.family": "Inter",
    "figure.facecolor": "#fffef7",
    "axes.facecolor": "#fffef7",
    "savefig.facecolor": "#fffef7",
})


def plot_failure_modes():
    df = pd.read_csv(ANALYSIS / "failure_mode_summary.csv")
    df["share_num"] = df["share_of_total"].str.rstrip("%").astype(float)
    df = df.sort_values("count", ascending=True)

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(df["failure_mode"], df["count"], color="#6b4ee6")
    for bar, share in zip(bars, df["share_num"]):
        ax.text(bar.get_width() + 0.15, bar.get_y() + bar.get_height() / 2,
                f"{int(bar.get_width())} ({share:.1f}%)", va="center", fontsize=9)
    ax.set_xlabel("Question count (of 24)")
    ax.set_title("Failure modes across benchmark questions\nRetrieval issues dominate")
    ax.set_xlim(0, df["count"].max() + 3)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(OUT / "failure_modes.png")
    plt.close(fig)


def plot_company_scores():
    df = pd.read_csv(ANALYSIS / "company_score_summary.csv").sort_values("avg_total", ascending=False)
    brand = {"DoorDash": "#E01600", "Instacart": "#ff8833",
             "Lyft": "#ff5cd6", "Uber": "#1f1f1f"}
    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.bar(df["company"], df["avg_total"],
                  color=[brand.get(c, "#888") for c in df["company"]])
    for bar, v in zip(bars, df["avg_total"]):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.03, f"{v:.1f}",
                ha="center", fontsize=10, fontweight="bold")
    ax.set_ylim(0, 3.2)
    ax.set_ylabel("Average total score (0–3)")
    ax.set_title("Average total score by company\nNarrow spread; no clear leader")
    ax.axhline(3, color="grey", linestyle=":", linewidth=0.8)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(OUT / "company_score_comparison.png")
    plt.close(fig)


def plot_issue_family_scores():
    df = pd.read_csv(ANALYSIS / "issue_family_summary.csv").sort_values("avg_total", ascending=True)
    colors = ["#8770EB" if v >= 2.4 else "#5A3BE3" if v >= 2.2 else "#401FD6" for v in df["avg_total"]]

    fig, ax = plt.subplots(figsize=(9, 6))
    bars = ax.barh(df["issue_family"], df["avg_total"], color=colors)
    for bar, v in zip(bars, df["avg_total"]):
        ax.text(bar.get_width() + 0.03, bar.get_y() + bar.get_height() / 2,
                f"{v:.1f}", va="center", fontsize=9)
    ax.set_xlim(0, 3.2)
    ax.set_xlabel("Average total score (0–3)")
    ax.set_title("Average score by issue family\nCharge/refund edge cases are weakest")
    ax.axvline(3, color="grey", linestyle=":", linewidth=0.8)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(OUT / "issue_family_score_comparison.png")
    plt.close(fig)


def plot_retrieval_vs_content_gap():
    df = pd.read_csv(ROOT / "data/processed/evaluation_results.csv")
    grouped = (df.groupby("company")[["retrievability_score", "public_kb_answerability_score"]]
                 .mean()
                 .sort_index()
                 .reset_index())
    x = range(len(grouped))
    width = 0.38

    pair = {
        "DoorDash": ("#CC1400", "#ff351f"),
        "Instacart": ("#f56600", "#ff8833"),
        "Lyft": ("#FF0AC2", "#FF70DB"),
        "Uber": ("#292929", "#666666"),
    }
    retr_colors = [pair.get(c, ("#888", "#bbb"))[0] for c in grouped["company"]]
    ans_colors = [pair.get(c, ("#888", "#bbb"))[1] for c in grouped["company"]]

    fig, ax = plt.subplots(figsize=(8, 4.8))
    b1 = ax.bar([i - width / 2 for i in x], grouped["retrievability_score"], width,
                color=retr_colors)
    b2 = ax.bar([i + width / 2 for i in x], grouped["public_kb_answerability_score"], width,
                color=ans_colors)
    for bars in (b1, b2):
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.03,
                    f"{bar.get_height():.1f}", ha="center", fontsize=9)
    ax.set_xticks(list(x))
    ax.set_xticklabels(grouped["company"])
    ax.set_ylim(1, 3.4)
    ax.set_ylabel("Average score (1–3)")
    ax.set_title("Retrievability vs. public KB answerability\nContent often answers the question better than native search can find it")
    legend_handles = [
        plt.Rectangle((0, 0), 1, 1, color="#666"),
        plt.Rectangle((0, 0), 1, 1, color="#bbb"),
    ]
    ax.legend(legend_handles, ["Retrievability", "Public KB answerability"],
              frameon=False, loc="upper right")
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(OUT / "retrieval_vs_content_gap.png")
    plt.close(fig)


def plot_category_scores_by_company():
    df = pd.read_csv(ROOT / "data/processed/evaluation_results.csv")
    categories = [
        ("retrievability_score", "Retrievability"),
        ("public_kb_answerability_score", "Public KB\nanswerability"),
        ("policy_clarity_score", "Policy clarity"),
        ("customer_actionability_score", "Customer\nactionability"),
        ("escalation_clarity_score", "Escalation\nclarity"),
        ("account_specific_dependency_score", "Account-specific\ndependency"),
        ("freshness_signal_score", "Freshness\nsignal"),
    ]
    cols = [c for c, _ in categories]
    labels = [l for _, l in categories]
    grouped = df.groupby("company")[cols].mean().sort_index()

    companies = grouped.index.tolist()
    colors = {"DoorDash": "#E01600", "Instacart": "#ff8833",
              "Lyft": "#ff5cd6", "Uber": "#1f1f1f"}
    n = len(companies)
    width = 0.8 / n
    x = range(len(labels))

    fig, ax = plt.subplots(figsize=(12, 5.5))
    for i, company in enumerate(companies):
        offsets = [xi - 0.4 + width / 2 + i * width for xi in x]
        vals = grouped.loc[company, cols].values
        bars = ax.bar(offsets, vals, width, label=company,
                      color=colors.get(company, "#888"))
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, v + 0.04,
                    f"{v:.1f}", ha="center", fontsize=8)

    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylim(1, 3.4)
    ax.set_ylabel("Average score (1–3)")
    ax.set_title("Average score by scoring category and company\nFreshness signal is uniformly weak; retrievability lags content quality")
    ax.legend(frameon=False, loc="upper right", ncol=len(companies))
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(OUT / "category_scores_by_company.png")
    plt.close(fig)


def main():
    plot_failure_modes()
    plot_company_scores()
    plot_issue_family_scores()
    plot_retrieval_vs_content_gap()
    plot_category_scores_by_company()
    print(f"Wrote 5 plots to {OUT}")


if __name__ == "__main__":
    main()
