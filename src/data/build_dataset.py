import pandas as pd

def build_dataset(data):

    workouts = data["workouts"]
    rows = []

    for workout in workouts:

        workout_id = workout.get("id")
        date = workout.get("workout_perform_date")
        body_weight = workout.get("body_weight")
        total_volume = workout.get("total_volume")

        for exercise in workout.get("exercises", []):

            exercise_name = exercise.get("excercise_name")
            exercise_type = exercise.get("exercise_type")

            for i, set_data in enumerate(exercise.get("sets", []), start=1):

                weight = set_data.get("weight")
                reps = set_data.get("reps")
                duration = set_data.get("duration")
                distance = set_data.get("distance")

                weight = float(weight) if weight not in ["", None] else None
                reps = float(reps) if reps not in ["", None] else None

                volume = weight * reps if weight and reps else None

                rows.append({
                    "workout_id": workout_id,
                    "date": date,
                    "body_weight": body_weight,
                    "exercise": exercise_name,
                    "exercise_type": exercise_type,
                    "set": i,
                    "weight": weight,
                    "reps": reps,
                    "volume": volume,
                    "total_workout_volume": total_volume,
                    "duration": duration,
                    "distance": distance
                })

    df = pd.DataFrame(rows)
    save_path = "/Users/Apple/GitHub/Spotter/src/data/workouts.csv"
    df.to_csv(save_path, index=False)

    return df