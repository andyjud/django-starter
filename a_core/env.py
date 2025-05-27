from pathlib import Path

import environ

env = environ.Env()

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

env.read_env(Path(BASE_DIR / '.env'))