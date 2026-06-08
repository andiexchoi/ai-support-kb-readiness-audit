"""Generate the writeup's plots from analysis CSVs into visuals/."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis"
OUT = ROOT / "visuals"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({"figure.dpi": 140, "savefig.bbox": "tight", "font.size": 10})


def plot_failure_modes():
    df = pd.read_csv(ANALYSIS / "failure_mode_summary.csv")
    df["share_num"] = df["share_of_total"].str.rstrip("%").astype(float)
    df = df.sort_values("count", ascending=True)

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(df["failure_mode"], df["count"], color="#3b6fb6")
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
    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.bar(df["company"], df["avg_total"], color=["#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"])
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
    colors = ["#c0392b" if v < 2.0 else "#e67e22" if v < 2.4 else "#27ae60" for v in df["avg_total"]]

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
    df = pd.read_csv(ANALYSIS / "company_score_summary.csv").sort_values("company")
    x = range(len(df))
    width = 0.38

    fig, ax = plt.subplots(figsize=(8, 4.5))
    b1 = ax.bar([i - width / 2 for i in x], df["avg_answerability"], width,
                label="Content (answerability)", color="#2a9d8f")
    b2 = ax.bar([i + width / 2 for i in x], df["avg_policy_clarity"], width,
                label="Retrieval-adjacent (policy clarity)", color="#e76f51")
    for bars in (b1, b2):
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.03,
                    f"{bar.get_height():.1f}", ha="center", fontsize=9)
    ax.set_xticks(list(x))
    ax.set_xticklabels(df["company"])
    ax.set_ylim(0, 3.4)
    ax.set_ylabel("Average score (0–3)")
    ax.set_title("Content answerability vs. policy clarity\nArticles can answer the question yet still be hard to surface")
    ax.legend(frameon=False, loc="upper right")
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(OUT / "retrieval_vs_content_gap.png")
    plt.close(fig)


def main():
    plot_failure_modes()
    plot_company_scores()
    plot_issue_family_scores()
    plot_retrieval_vs_content_gap()
    print(f"Wrote 4 plots to {OUT}")


if __name__ == "__main__":
    main()
