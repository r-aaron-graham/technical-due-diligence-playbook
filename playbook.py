"""CLI to generate a due diligence report from a template."""

from __future__ import annotations

import datetime
from pathlib import Path

import click


TEMPLATE_PATH = Path(__file__).resolve().parent / "report_template.md"


@click.command()
@click.option("--target", required=True, help="Name of the company or product under assessment.")
@click.option("--output", type=click.Path(dir_okay=False, path_type=Path), required=True, help="Report output path.")
@click.option("--author", default="Anonymous", show_default=True, help="Name of the report author.")
def main(target: str, output: Path, author: str):
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    today = datetime.date.today().isoformat()
    content = template.replace("{{ target }}", target).replace("{{ author }}", author).replace("{{ date }}", today)
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with output.open("x", encoding="utf-8") as report:
            report.write(content)
    except FileExistsError as exc:
        raise click.ClickException(f"Report already exists: {output}") from exc
    click.echo(f"Created report for {target} at {output}")


if __name__ == "__main__":  # pragma: no cover
    main()