import glob
from pathlib import Path
import re
import shutil
import sys
import tempfile
from yte import process_yaml

import yaml
import pytest
import subprocess as sp

spells = [meta_path.parent for meta_path in Path(".").glob("**/meta.yaml")]

outdir_base = Path("test_outputs")
if outdir_base.exists():
    print("Cleaning up previous test outputs", file=sys.stderr)
    shutil.rmtree(outdir_base)


@pytest.mark.parametrize("spell", spells, ids=map(str, spells))
def test_spell(spell):
    tests = list((spell / "tests").glob("test_*.yaml"))
    assert tests, f"No tests found for {spell}"

    for testcase in tests:
        test_dir = testcase.parent
        outdir = (outdir_base / "testcases" / test_dir / testcase.name).with_suffix("")
        outdir.mkdir(parents=True, exist_ok=True)
        print(f"Testcase {testcase}, storing result it {outdir}:", file=sys.stderr)
        try:
            sp.run(
                ["datavzrd", testcase.name, "--output", outdir.absolute()],
                check=True,
                stderr=sp.PIPE,
                cwd=test_dir,
            )
        except sp.CalledProcessError as e:
            print(e.stderr.decode(), file=sys.stderr)
            raise e
        print("OK", file=sys.stderr)


@pytest.mark.parametrize("spell", spells, ids=map(str, spells))
def test_example(spell):
    with open(spell / "meta.yaml", "r") as f:
        meta = yaml.load(f, Loader=yaml.SafeLoader)

    assert (
        "example" in meta
    ), f"No example found for {spell}, please add one to meta.yaml"
    example = meta["example"]
    assert (
        "code" in example
    ), f"No example/code found for {spell}, please add it to meta.yaml"
    assert (
        "test-data" in example
    ), f"No example/test-data found for {spell}, please add it to meta.yaml"
    assert (
        "<url>" in example["code"]
    ), f"Example code for spell has to contain <url> for pointing to the spell in {spell}"
    example["code"] = example["code"].replace("<url>", "spell.yaml")
    example_code = yaml.load(example["code"], Loader=yaml.SafeLoader)

    outdir = outdir_base / "examples" / spell
    outdir.mkdir(parents=True, exist_ok=True)

    if meta["type"] == "column":
        assert (
            "render-table" in example_code
        ), f"Example code for column spell has to start with render-table in spell {spell}"

        with open(
            Path(__file__).parent / "column_spell.config_template.yaml", "r"
        ) as f, tempfile.NamedTemporaryFile("w") as rendered_config:
            process_yaml(
                f,
                outfile=rendered_config,
                variables={
                    "example": example_code["render-table"],
                    "path": example["test-data"],
                },
            )
            rendered_config.flush()

            try:
                sp.run(
                    ["datavzrd", rendered_config.name, "--output", outdir.absolute()],
                    check=True,
                    stderr=sp.PIPE,
                    cwd=spell,
                )
            except sp.CalledProcessError as e:
                print(e.stderr.decode(), file=sys.stderr)
                raise e
