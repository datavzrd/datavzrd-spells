import glob
from pathlib import Path
import shutil
import sys
import tempfile
import pytest
import subprocess as sp

spells = [meta_path.parent for meta_path in Path(".").glob("**/meta.yaml")]

outdir_base = Path("test_outputs")
if outdir_base.exists():
    print("Cleaning up previous test outputs", file=sys.stderr)
    shutil.rmtree(outdir_base)

@pytest.mark.parametrize("spell", spells)
def test_spell(spell):
    tests = list((spell / "tests").glob("test_*.yaml"))
    assert tests, f"No tests found for {spell}"

    for testcase in tests:
        test_dir = testcase.parent
        outdir = (outdir_base / test_dir / testcase.name).with_suffix("")
        outdir.mkdir(parents=True, exist_ok=True)
        print(f"Testcase {testcase}, storing result it {outdir}:", file=sys.stderr)
        try:
            sp.run(["datavzrd", testcase.name, "--output", outdir.absolute()], check=True, stderr=sp.PIPE, cwd=test_dir)
        except sp.CalledProcessError as e:
            print(e.stderr.decode(), file=sys.stderr)
            raise e
        print("OK", file=sys.stderr)
