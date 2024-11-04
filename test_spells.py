import glob
from pathlib import Path
import sys
import tempfile
import pytest
import subprocess as sp

spells = [meta_path.parent for meta_path in Path(".").glob("**/meta.yaml")]

@pytest.mark.parametrize("spell", spells)
def test_spell(spell):
    tests = list((spell / "tests").glob("test_*.yaml"))
    assert tests, f"No tests found for {spell}"

    for testcase in tests:
        test_dir = testcase.parent
        print(f"Testcase {testcase}:", file=sys.stderr)
        with tempfile.TemporaryDirectory() as tmpdir:
            try:
                sp.run(["datavzrd", testcase.name, "--output", tmpdir], check=True, stderr=sp.PIPE, cwd=test_dir)
            except sp.CalledProcessError as e:
                print(e.stderr.decode(), file=sys.stderr)
                raise e
            print("OK", file=sys.stderr)
