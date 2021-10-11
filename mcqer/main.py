from pyfiglet import Figlet
import os
import typer
import time
app = typer.Typer()

f= Figlet(font = "slant")


def writeToFile(name : str, path : str, data : dict):
    try:
        with open(os.path.join(path, name), 'w') as wp:
            for key in data.keys():
                wp.write(f"{key} : {data[key]} \n")       
    except Exception as e:
        return False, e
    else:
        return True, "success"

@app.command()
def test():
    text = f.renderText("MCQer")
    typer.secho(f"""
{text}
==============================================================================================================================

Welcome to mcq-tool. The convenient CLI application which can help you do online mcqs quickly and check them simultaneously. 
    """, fg = typer.colors.BRIGHT_CYAN)

@app.command()
def mcq(name):
    data = {}
    score = 0
    typer.echo("Hello!! Before you start the test here are few things we need to check")
    type = typer.prompt("Is it serialised or no (y/n)")
    if type == "y":
        questions_numbers = int(typer.prompt("How many questions are there ?"))
        for i in range(1, questions_numbers+1):
            data[str(i)] = ""
    else:
        numbers = typer.prompt("Enter the numbers in this format : a-b; x-y")
        question_list = numbers.split("; ")
        for i in question_list :
            i = i.split("-")
            for j in range(int(i[0]), int(i[1]) + 1):
                data[str(j)] = ""
        questions_numbers = len(data)   
 
    typer.secho("""
==============================================
            LET'S START 
==============================================
    """, fg=typer.colors.GREEN)  
    for i in data.keys():
        response = typer.prompt(f"{i}")
        data[i] = str(response)

    typer.secho("""
=================================================
    LET'S START CHECKING THE ANSWERS
=================================================
    """, fg=typer.colors.GREEN)
    typer.echo("Enter what ma'am's/website's saying and we will check one by one")
    for i in data.keys():
        response = typer.prompt(f"{i}")
        if response == data[i] :
            data[i] = f"{data[i]}"
            score+=1
        else:
            data[i] = f"{data[i]} X - {response}"

    typer.secho("Calculating your marks", fg = typer.colors.GREEN)
    with typer.progressbar(range(100)) as progress:
        for _ in progress:
            time.sleep(0.01)
    typer.secho(f"""
-------------------------------
You got {score} questions right out of {questions_numbers}.
-------------------------------
    """, fg=typer.colors.GREEN)
    file_name = f"{name}.txt"
    file_path = typer.prompt("Enter the file path where you would want the file to be saved")
    typer.echo("Saving your file")
    code, status = writeToFile(file_name, file_path, data)
    with typer.progressbar(range(100)) as progress:
        for _ in progress:
            time.sleep(0.01)
    if code == True:
        typer.secho("""
  ---------
   DONE !!!
  ---------
""", fg=typer.colors.GREEN)
    else:
        typer.secho("Oops something went wrong !!!", fg = typer.colors.RED)
        typer.echo(status)
    


if __name__ == "__main__":
    app()