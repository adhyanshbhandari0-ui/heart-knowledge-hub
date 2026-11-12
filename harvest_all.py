import os, re, subprocess, requests
from bs4 import BeautifulSoup

# The 4 list repositories inside your repos/ folder
list_files = [
    "repos/awesome-ai-cardiology/README.md",
    "repos/awesome-hrv/README.md",
    "repos/awesome-healthcare-datasets/README.md",
    "repos/medical-data/README.md"
]

os.makedirs("linked-repos", exist_ok=True)
os.makedirs("linked-papers-and-articles", exist_ok=True)

# 1. Save the CORAL study text you pasted earlier
coral_path = "linked-papers-and-articles/CORAL_ML_Cardiovascular_Outcomes_2019.md"
if not os.path.exists(coral_path):
    with open(coral_path, "w", encoding="utf-8") as f:
        f.write("# Prediction of cardiovascular outcomes with machine learning techniques: application to the CORAL study\n")
        f.write("- **Authors:** Tian Chen, Pamela Brewster, Katherine R Tuttle, Lance Dworkin, Joseph I Shapiro, et al.\n")
        f.write("- **Journal:** International Journal of Nephrology and Renovascular Disease (March 2019, 12:49-58)\n")
        f.write("- **DOI:** 10.2147/IJNRD.S194727\n\n")
        f.write("## Key Findings\n")
        f.write("- Analyzed 573 CORAL subjects with complete baseline data (80:20 train/test split across 10 seeds using R CARET).\n")
        f.write("- Models tested: GLM (62.7% ROC), SVM (65.3% ROC), Decision Tree/RPART (53.0% ROC), Neural Network (63.1% ROC), Random Forest (68.1% ± 4.3% ROC).\n")
        f.write("- Top predictors in Random Forest: Systolic BP (SBP), Serum Creatinine, Glycosylated Hemoglobin (HbA1c), Diastolic BP (DBP).\n")
        f.write("- Treatment assignment (stenting vs. medical therapy alone) was not an important predictor in any model.\n")

all_links = []
for md_path in list_files:
    if os.path.exists(md_path):
        with open(md_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        found = re.findall(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', content)
        all_links.extend(found)

seen_urls = set()
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

for title, url in all_links:
    clean_url = url.split("#")[0].rstrip("/")
    if clean_url in seen_urls:
        continue
    seen_urls.add(clean_url)

    # Case A: It is a GitHub repository -> clone shallow copy & strip .git
    gh_match = re.match(r'^https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)$', clean_url)
    if gh_match:
        repo_name = gh_match.group(2)
        target_dir = os.path.join("linked-repos", repo_name)
        if not os.path.exists(target_dir) and not os.path.exists(os.path.join("repos", repo_name)):
            print(f"[CLONING REPO] {clean_url}")
            subprocess.run(["git", "clone", "--depth", "1", clean_url, target_dir],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            git_dir = os.path.join(target_dir, ".git")
            if os.path.exists(git_dir):
                subprocess.run(["rm", "-rf", git_dir])
        continue

    # Case B: Web article, arXiv abstract, PubMed, or dataset page -> save clean Markdown
    safe_title = re.sub(r'[^a-zA-Z0-9_-]', '_', title).strip("_")[:65]
    if not safe_title:
        continue
    md_out = os.path.join("linked-papers-and-articles", f"{safe_title}.md")
    if os.path.exists(md_out):
        continue

    try:
        resp = requests.get(clean_url, headers=headers, timeout=10)
        if resp.status_code == 200 and "text/html" in resp.headers.get("Content-Type", ""):
            soup = BeautifulSoup(resp.text, "html.parser")
            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()
            paragraphs = [p.get_text(" ", strip=True) for p in soup.find_all(["h1", "h2", "h3", "p", "li"])]
            body = "\n\n".join([p for p in paragraphs if len(p) > 40])
            if len(body) > 300:
                with open(md_out, "w", encoding="utf-8") as out:
                    out.write(f"# {title}\n\n**Source:** {clean_url}\n\n---\n\n{body}\n")
                print(f"[SAVED ARTICLE] {safe_title}.md")
    except Exception:
        pass

print("\nDone! Check linked-repos/ and linked-papers-and-articles/")
