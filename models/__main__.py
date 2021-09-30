from click.utils import echo
import typer

from .calhousing.model import CalhousingModel

app = typer.Typer()


@app.command()
def info():
    typer.echo("The CLI App")


@app.command()
def train(id: str = typer.Option(...)):
    typer.echo(f"Training model {id}...")
    model = CalhousingModel(id)
    model.train()
    typer.echo(f"Model {id} was successfully created: {model.model_path}")


@app.command()
def validate():
    typer.echo(f"Model validation...")
    model = CalhousingModel("validation")
    score = model.validate()
    typer.echo(
        f"The model was successfully validated with the following metrics: "
        f"{model.validation_parameters.metric_name}: {score}"
    )


if __name__ == "__main__":
    app()
