"""Generate career context folders without overwriting existing work."""
from pathlib import Path
from datetime import datetime
import argparse
REPOSITORIES=['2018-python-backend-journey', '2019-python-automation', '2020-machine-learning-lab', '2021-deep-learning-nlp', '2022-production-ml-platform', '2023-rag-knowledge-assistant', '2024-generative-ai-platform', '2025-agentic-ai-workflows', '2026-ai-product-engineering']
def generate(root):
    for name in REPOSITORIES:
        folder=Path(root)/name
        folder.mkdir(parents=True,exist_ok=True)
        readme=folder/'README.md'
        if not readme.exists():
            readme.write_text(f"# {name}\n\n## Career Context\n\nOriginal experience period: {name[:4]}. Recreated/modernized demonstration; not the original employer/client repository. Earlier work was primarily private. New commits keep actual dates.\n\nPortfolio maintained in {datetime.now().year}.\n",encoding='utf-8')
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--root',default='career-portfolio')
    generate(parser.parse_args().root)
    print('Portfolio structure generated without overwriting existing READMEs.')
