scores_maths = [100, 75, 90, 95, 60, 50, 95, 85, 70, 75,
                90, 85, 60, 45, 100, 70, 65, 50, 55, 95,
                50, 45, 35, 100, 95, 90, 85, 90, 80, 85,
                95, 45, 60, 45, 80, 70, 55, 45, 60, 90]

scores_physics = [50, 65, 85, 100, 60, 55, 90, 85, 70, 90,
                  50, 40, 100, 45, 95, 70, 75, 60, 50, 100,
                  60, 90, 40, 90, 95, 90, 80, 95, 85, 80,
                  95, 90, 75, 50, 80, 70, 50, 35, 65, 90]

scores_english = [50, 40, 100, 45, 95, 70, 75, 60, 50, 100,
                  50, 45, 35, 100, 95, 90, 85, 90, 80, 85,
                  90, 85, 60, 45, 100, 70, 65, 50, 55, 95,
                  50, 65, 85, 100, 60, 55, 90, 85, 70, 90]

overall_scores = [math + physics + english for math, physics, english in
                  zip(scores_maths, scores_physics, scores_english)]

admitted_students = [score for score in overall_scores if score >= 270]

print(len(admitted_students))
