from pathlib import Path
import subprocess
subprocess.run(["node",str(Path(__file__).resolve().parents[1]/"model/build-site.mjs")],check=True)
