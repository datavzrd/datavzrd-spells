import glob
from pathlib import Path
import sys
import tempfile
import pytest
import subprocess as sp

spells = [Path(meta_path).parent for meta_path in glob.glob("**/meta.yaml")]

pytest.mark.parametrize("spell", spells)
def test_spell(spell):
    tests = list((spell / "tests").glob("*"))
    assert tests, f"No tests found for {spell}"

    for testcase in tests:
        config = testcase / "config.yaml"
        with tempfile.TemporaryDirectory() as tmpdir:
            sp.run(["datavzrd", config, "--output", tmpdir], check=True, stderr=sp.PIPE, cwd=testcase)