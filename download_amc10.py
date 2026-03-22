#!/usr/bin/env python3
"""
AMC 10 Mock Tests Downloader
Downloads high-quality AMC 10 mock tests from multiple sources.
Usage: python3 download_amc10.py [--all] [--mockamc] [--ziml] [--github] [--detoasty3] [--other]
"""

import os, sys, time, argparse
from pathlib import Path

try:
    import requests
except ImportError:
    print("Installing requests...")
    os.system("pip install requests")
    import requests

BASE_DIR = Path("amc10_mocks")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def download_file(url, dest, retries=2):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        print(f"  [SKIP] {dest.name} (already exists)")
        return True
    for attempt in range(retries):
        try:
            r = requests.get(url, headers=HEADERS, timeout=30, stream=True)
            r.raise_for_status()
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            sz = dest.stat().st_size
            print(f"  [ OK ] {dest.name} ({sz//1024}KB)")
            return True
        except Exception as e:
            if attempt < retries-1:
                time.sleep(1)
                continue
            print(f"  [FAIL] {dest.name}: {e}")
            return False

def section(title):
    print(f"\n{'='*60}\n  {title}\n{'='*60}")

BASE_DIR.mkdir(parents=True, exist_ok=True)

def download_mockamc():
    section("1. MockAMC (mockamc.github.io)")
    base = "https://mockamc.github.io"
    exams_dir = BASE_DIR / "MockAMC" / "exams"
    sols_dir = BASE_DIR / "MockAMC" / "solutions"
    exams_dir.mkdir(parents=True, exist_ok=True)
    sols_dir.mkdir(parents=True, exist_ok=True)

    files = [
        ("exams/amc10/2024_aops_tmc.pdf","2024_TMC_MockAMC10_Problems.pdf"),
        ("exams/amc10/2023_aops_qidb602.pdf","2023_AoPS_MockAMC10_QIDb602_Problems.pdf"),
        ("exams/amc10/2022_aops_wmc.pdf","2022_WMC10_Problems.pdf"),
        ("solutions/amc10/2022_aops_wmc_sol.pdf","2022_WMC10_Solutions.pdf"),
        ("exams/amc10/2022_aops_omc.pdf","2022_OMC10_Problems.pdf"),
        ("solutions/amc10/2022_aops_omc_sol.pdf","2022_OMC10_Solutions.pdf"),
        ("exams/amc10/2021_aops_omc.pdf","2021_OMC10_Problems.pdf"),
        ("solutions/amc10/2021_aops_omc_sol.txt","2021_OMC10_Answers.txt"),
        ("exams/amc10/2021_aops_wertguk.pdf","2021_AoPS_MockAMC10_wertguk_Problems.pdf"),
        ("solutions/amc10/2021_aops_wertguk_sol.pdf","2021_AoPS_MockAMC10_wertguk_Solutions.pdf"),
        ("exams/amc10/2021_aops_mimc_mar.pdf","2021_March_MIMC10_Problems.pdf"),
        ("solutions/amc10/2021_aops_mimc_mar_sol.pdf","2021_March_MIMC10_Solutions.pdf"),
        ("exams/amc10/2021_aops_mimc_apr.pdf","2021_April_MIMC10_Problems.pdf"),
        ("solutions/amc10/2021_aops_mimc_apr_sol.pdf","2021_April_MIMC10_Solutions.pdf"),
        ("exams/amc10/2021_aops_dmc_10a.pdf","2021_DMC10A_Problems.pdf"),
        ("solutions/amc10/2021_aops_dmc_10a_sol.pdf","2021_DMC10A_Solutions.pdf"),
        ("exams/amc10/2021_aops_dmc_10b.pdf","2021_DMC10B_Problems.pdf"),
        ("solutions/amc10/2021_aops_dmc_10b_sol.pdf","2021_DMC10B_Solutions.pdf"),
        ("exams/amc10/2021_aops_dmc_10c.pdf","2021_DMC10C_Problems.pdf"),
        ("solutions/amc10/2021_aops_dmc_10c_sol.pdf","2021_DMC10C_Solutions.pdf"),
        ("exams/amc10/2021_aops_kmmc.pdf","2021_KMMC10_Problems.pdf"),
        ("solutions/amc10/2021_aops_kmmc_sol.pdf","2021_KMMC10_Solutions.pdf"),
        ("exams/amc10/2021_aops_aamc_10a.pdf","2021_AAMC10A_Problems.pdf"),
        ("exams/amc10/2021_aops_aamc_10b.pdf","2021_AAMC10B_Problems.pdf"),
        ("exams/amc10/2020_aops_pgroudon.pdf","2020_AoPS_MockAMC10_PGroudon_Problems.pdf"),
        ("solutions/amc10/2020_aops_pgroudon_sol.txt","2020_AoPS_MockAMC10_PGroudon_Answers.txt"),
        ("exams/amc10/2020_aops_tmc_10a.pdf","2020_TMC10A_Problems.pdf"),
        ("solutions/amc10/2020_aops_tmc_10a_sol.pdf","2020_TMC10A_Solutions.pdf"),
        ("exams/amc10/2020_aops_tmc_10b.pdf","2020_TMC10B_Problems.pdf"),
        ("solutions/amc10/2020_aops_tmc_10b_sol.pdf","2020_TMC10B_Solutions.pdf"),
        ("exams/amc10/2020_aops_scrabbler94.pdf","2020_AoPS_MockAMC10_scrabbler94_Problems.pdf"),
        ("solutions/amc10/2020_aops_scrabbler94_sol.pdf","2020_AoPS_MockAMC10_scrabbler94_Solutions.pdf"),
        ("exams/amc10/2020_aops_pmc.pdf","2020_PMC10_Problems.pdf"),
        ("solutions/amc10/2020_aops_pmc_sol.txt","2020_PMC10_Answers.txt"),
        ("exams/amc10/2020_aops_dmc.pdf","2020_DMC10_Problems.pdf"),
        ("solutions/amc10/2020_aops_dmc_sol.pdf","2020_DMC10_Solutions.pdf"),
        ("exams/amc10/2020_aops_tmc.pdf","2020_TMC10_Problems.pdf"),
        ("solutions/amc10/2020_aops_tmc_sol.pdf","2020_TMC10_Solutions.pdf"),
        ("exams/amc10/2019_aops_fidgetboss4000.pdf","2019_MockAMC10B_fidgetboss4000_Problems.pdf"),
        ("solutions/amc10/2019_aops_fidgetboss4000_sol.txt","2019_MockAMC10B_fidgetboss4000_Answers.txt"),
        ("exams/amc10/2019_aops_cmc_10a.pdf","2019_CMC10A_Problems.pdf"),
        ("solutions/amc10/2019_aops_cmc_10a_sol.pdf","2019_CMC10A_Solutions.pdf"),
        ("exams/amc10/2019_aops_cmc_10b.pdf","2019_CMC10B_Problems.pdf"),
        ("solutions/amc10/2019_aops_cmc_10b_sol.pdf","2019_CMC10B_Solutions.pdf"),
        ("exams/amc10/2018_aops_scrabbler94.pdf","2018_AoPS_MockAMC10_scrabbler94_Problems.pdf"),
        ("solutions/amc10/2018_aops_scrabbler94_sol.pdf","2018_AoPS_MockAMC10_scrabbler94_Solutions.pdf"),
        ("exams/amc10/2018_aops_blue8931.pdf","2018_MockAMC18_blue8931_Problems.pdf"),
        ("solutions/amc10/2018_aops_blue8931_sol.txt","2018_MockAMC18_blue8931_Answers.txt"),
        ("exams/amc10/2018_aops_memorialday.pdf","2018_MemorialDay_MockAMC10_Problems.pdf"),
        ("solutions/amc10/2018_aops_memorialday_sol.pdf","2018_MemorialDay_MockAMC10_Solutions.pdf"),
        ("exams/amc10/2018_aops_autumnmock.pdf","2018_AutumnMock_MockAMC10_Problems.pdf"),
        ("solutions/amc10/2018_aops_autumnmock_sol.txt","2018_AutumnMock_MockAMC10_Answers.txt"),
        ("exams/amc10/2017_aops_eisirrational.pdf","2017_AoPS_MockAMC10_eisirrational_Problems.pdf"),
        ("solutions/amc10/2017_aops_eisirrational_sol.txt","2017_AoPS_MockAMC10_eisirrational_Answers.txt"),
        ("exams/amc10/2017_aops_summermock.pdf","2017_Summer_MockAMC10_Problems.pdf"),
        ("solutions/amc10/2017_aops_summermock_sol.pdf","2017_Summer_MockAMC10_Solutions.pdf"),
        ("exams/amc10/2016_aops_meepymeepmeep.pdf","2016_AoPS_MockAMC10_MeepyMeepMeep_Problems.pdf"),
        ("solutions/amc10/2016_aops_meepymeepmeep_sol.txt","2016_AoPS_MockAMC10_MeepyMeepMeep_Answers.txt"),
        ("exams/amc10/2015_aops_bca.pdf","2015_BCA_MockAMC10_Problems.pdf"),
        ("exams/amc10/2015_aops_joey8189681.pdf","2015_AoPS_MockAMC10_joey8189681_Problems.pdf"),
        ("solutions/amc10/2015_aops_joey8189681_sol.pdf","2015_AoPS_MockAMC10_joey8189681_Solutions.pdf"),
        ("exams/amc10/2015_aops_azmath333.pdf","2015_AoPS_MockAMC10_azmath333_Problems.pdf"),
        ("solutions/amc10/2015_aops_azmath333_sol.pdf","2015_AoPS_MockAMC10_azmath333_Solutions.pdf"),
        ("exams/amc10/2015_aops_droid347.pdf","2015_AoPS_MockAMC10_droid347_Problems.pdf"),
        ("solutions/amc10/2015_aops_droid347_sol.txt","2015_AoPS_MockAMC10_droid347_Answers.txt"),
    ]

    for path, name in files:
        url = f"{base}/{path}"
        is_exam = not path.startswith("solutions")
        dest = exams_dir / name if is_exam else sols_dir / name
        ok = download_file(url, dest)
        time.sleep(0.3)

def download_ziml():
    section("2. ZIML (ziml.areteem.org)")
    dest = BASE_DIR / "ZIML"
    dest.mkdir(parents=True, exist_ok=True)
    urls = [
        ("https://ziml.areteem.org/ziml/download/MockAMC-10.pdf","MockAMC10_Sample.pdf"),
        ("https://ziml.areteem.org/ziml/download/MockAMC-12.pdf","MockAMC12_Sample.pdf"),
    ]
    s = f = 0
    for url, name in urls:
        if download_file(url, dest/name): s += 1
        else: f += 1
        time.sleep(0.5)
    print(f"\n  ZIML: {s} OK, {f} failed")
    print("  Note: ZIML requires free account for full archive PDFs")
    print("  Visit: https://ziml.areteem.org/ziml/practicecontests.php?f=1&p=AMC10")

def download_detoasty3():
    section("3. DeToasty3 (DMC Mock Contests)")
    base = "https://detoasty3.github.io"
    dest = BASE_DIR / "DMC_MockContests"
    dest.mkdir(parents=True, exist_ok=True)
    files = [
        ("/2021_DMC_10A.pdf","2021_DMC10A_Problems.pdf"),
        ("/2021_DMC_10A_Solutions.pdf","2021_DMC10A_Solutions.pdf"),
        ("/2021_DMC_10B.pdf","2021_DMC10B_Problems.pdf"),
        ("/2021_DMC_10B_Solutions.pdf","2021_DMC10B_Solutions.pdf"),
        ("/2021_DMC_10C.pdf","2021_DMC10C_Problems.pdf"),
        ("/2021_DMC_10C_Solutions.pdf","2021_DMC10C_Solutions.pdf"),
        ("/2020_DMC_10.pdf","2020_DMC10_Problems.pdf"),
        ("/2020_DMC_10_Solutions.pdf","2020_DMC10_Solutions.pdf"),
        ("/2020_KMMC_10.pdf","2020_KMMC10_Problems.pdf"),
        ("/2020_KMMC_10_Solutions.pdf","2020_KMMC10_Solutions.pdf"),
        ("/2021_KMMC_10.pdf","2021_KMMC10_Problems.pdf"),
        ("/2021_KMMC_10_Solutions.pdf","2021_KMMC10_Solutions.pdf"),
    ]
    s = f = 0
    for path, name in files:
        if download_file(f"{base}{path}", dest/name): s += 1
        else: f += 1
        time.sleep(0.3)
    print(f"\n  DeToasty3: {s} OK, {f} failed")

def download_altizio():
    section("4. David Altizio's Homemade Problem Collection")
    dest = BASE_DIR / "HomemadeProblems"
    dest.mkdir(parents=True, exist_ok=True)
    url = "https://davidaltizio.web.illinois.edu/HomemadeProblems.pdf"
    ok = download_file(url, dest/"HomemadeProblemCollection_DavidAltizio.pdf")
    print(f"\n  Altizio: {'OK' if ok else 'failed'}")

def clone_github_repos():
    section("5. GitHub Repos (AMC Tools)")
    repos = [
        ("https://github.com/andrewboldi/AMC-Trainer.git","AMC_Trainer","Online practice tool"),
        ("https://github.com/amctesseract/amctesseract.github.io.git","AMC_Tesseract","Web app for online practice"),
        ("https://github.com/detoasty3/detoasty3.github.io.git","DeToasty3_website","DMC contest source"),
        ("https://github.com/byronxu99/amc-pdf.git","amc_pdf_tool","Bash+LaTeX PDF generator"),
        ("https://github.com/arjvik/prepamc.git","PrepAMC","Shell script to download from AoPS"),
        ("https://github.com/mchen910/amc-prep.git","amc_prep","Python AMC problem scraper"),
        ("https://github.com/cymcymcymcym/amc_problem_set_creator.git","AMC_ProblemSetCreator","Random problem set generator"),
        ("https://github.com/Prachurja/AMC-Worksheet-Generator.git","AMC_WorksheetGenerator","CLI worksheet generator"),
        ("https://github.com/iuruoy-shao/training-problems.git","AMC_TrainingProblems","Adaptive problem trainer"),
        ("https://github.com/Octophi/pbank.git","ProblemBank","Problems by topic"),
        ("https://github.com/mockamc/mockamc.github.io.git","MockAMC_source","MockAMC website source"),
    ]
    tools_dir = BASE_DIR / "github_tools"
    tools_dir.mkdir(parents=True, exist_ok=True)
    for repo_url, dest_name, desc in repos:
        dest = tools_dir / dest_name
        if dest.exists():
            print(f"  [SKIP] {dest_name} (already cloned)")
            continue
        print(f"  Cloning {dest_name} ({desc})...")
        res = os.system(f"git clone --depth 1 {repo_url} '{dest}' 2>/dev/null")
        print(f"  [ OK ] {dest_name}" if res == 0 else f"  [FAIL] {dest_name}")

def report_manual():
    section("6. Manual Download Required")
    print("""
  The following sources require manual access (no direct download URLs):

  1. Morning Star Institute (模拟考试 PDF + 解答视频)
     https://www.morningstarinstitute.org/amc%E6%A8%A1%E6%8B%9F%E8%80%83%E8%AF%95/

  2. Think Academy (AMC10 模拟题资源包)
     https://www.thethinkacademy.com/blog/2025-amc-10a-real-questions-and-analysis/

  3. MathPrepPro (在线模拟考试，需注册免费账号)
     https://www.mathpreppro.com

  4. AMC Trainer (在线练习平台)
     https://andrewboldi.github.io/AMC-Trainer/

  5. AMC Tesseract (在线练习 + 保存成绩)
     https://amctesseract.github.io/

  6. AMC Problem Set Creator (HuggingFace, 随机抽题生成 PDF)
     https://huggingface.co/spaces/ymcmy/AMC_AIME_Random_Problem_Set_Generator

  7. ZIML Practice Contests (在线模拟 + 部分 PDF)
     https://ziml.areteem.org/ziml/practicecontests.php?f=1&p=AMC10

  8. AoPS Wiki Full Mock List
     https://artofproblemsolving.com/wiki/index.php/Mock_Amc_10

  9. Dr. Xue Math School (历年真题 Google Drive)
     https://www.xuemath.org/amc10-resources

 10. Po-Shen Loh LIVE (历年真题 PDF)
     https://live.poshenloh.com/past-contests
""")

def main():
    parser = argparse.ArgumentParser(description="AMC 10 Mock Tests Downloader")
    parser.add_argument("--all", action="store_true", help="Download everything")
    parser.add_argument("--mockamc", action="store_true", help="Download MockAMC collection")
    parser.add_argument("--ziml", action="store_true", help="Download ZIML PDFs")
    parser.add_argument("--detoasty3", action="store_true", help="Download DMC contests")
    parser.add_argument("--github", action="store_true", help="Clone GitHub repos")
    parser.add_argument("--altizio", action="store_true", help="Download Altizio collection")
    args = parser.parse_args()

    if len(sys.argv) == 1 or args.all:
        args.mockamc = args.ziml = args.detoasty3 = args.github = args.altizio = True

    print(f"""
╔════════════════════════════════════════════════════════════╗
║          AMC 10 Mock Tests Downloader                      ║
║          Target: {BASE_DIR}
╚════════════════════════════════════════════════════════════╝
    """)

    if args.mockamc:    download_mockamc()
    if args.ziml:       download_ziml()
    if args.detoasty3:  download_detoasty3()
    if args.altizio:    download_altizio()
    if args.github:     clone_github_repos()

    report_manual()

    section("Done!")
    print(f"  Output: {BASE_DIR.resolve()}")
    print()

if __name__ == "__main__":
    main()
