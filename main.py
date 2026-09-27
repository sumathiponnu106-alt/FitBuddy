from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
app = FastAPI(title="FitBuddy")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post("/start")
def start(
    name: str = Form(...),
    age: int = Form(...),
    height: float = Form(...),
    weight: float = Form(...)
):
    bmi = weight / ((height / 100) ** 2)

    return RedirectResponse(
    url=f"/result?name={name}&age={age}&height={height}&weight={weight}&bmi={bmi}",
    status_code=303
)
@app.get("/result")
def result(
    request: Request,
    name: str,
    age: int,
    height: float,
    weight: float,
    bmi: float
):
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "name": name,
            "age": age,
            "height": height,
            "weight": weight,
            "bmi": round(bmi, 2),
            "category": category
        }
    )
@app.get("/workout")
def workout_page(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="workout.html",
    context={"request": request}
)
@app.post("/workout")
def workout(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    height: float = Form(...),
    weight: float = Form(...),
):
    bmi = weight / ((height / 100) ** 2)

    if bmi < 18.5:
        category = "Underweight"
        workout_level = "Beginner Workout"
        workouts = [
            "Walking - 20 minutes",
            "Squats - 10 reps",
            "Wall Push-ups - 10 reps"
        ]

    elif bmi < 25:
        category = "Normal"
        workout_level = "Intermediate Workout"
        workouts = [
            "Walking - 30 minutes",
            "Squats - 15 reps",
            "Push-ups - 10 reps"
        ]

    elif bmi < 30:
        category = "Overweight"
        workout_level = "Beginner Workout"
        workouts = [
            "Walking - 20 minutes",
            "Squats - 10 reps",
            "Wall Push-ups - 10 reps"
        ]

    else:
        category = "Obese"
        workout_level = "Beginner Workout"
        workouts = [
            "Walking - 20 minutes",
            "Chair Squats - 10 reps",
            "Wall Push-ups - 10 reps"
        ]

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "name": name,
            "age": age,
            "height": height,
            "weight": weight,
            "bmi": round(bmi, 2),
            "category": category,
            "workout_level": workout_level,
            "workouts": workouts
        }
    )
@app.get("/diet")
def diet(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="diet.html",
        context={}
    )

@app.get("/bmi")
def bmi(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="bmi.html",
        context={}
    )
@app.post("/calculate-bmi")
def calculate_bmi(
    request: Request,
    height: float = Form(...),
    weight: float = Form(...)
):
    bmi_value = weight / ((height / 100) ** 2)

    if bmi_value < 18.5:
        category = "Underweight"
    elif bmi_value < 25:
        category = "Normal"
    elif bmi_value < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return templates.TemplateResponse(
        request=request,
        name="bmi_result.html",
        context={
            "bmi": round(bmi_value, 2),
            "category": category
        }
    )