# Create a dictionary for subjects and marks allocated to the subject.
# The marks are too low, so the teacher changed the marks.
# Add 10 to all numeric values in a dictionary using a loop and if.

scores = {"name":"John","math":70,"science":65,"history":80,"pass":"Yes"}

for key in scores:
    if type(scores[key]) == int:
         increase = scores[key] + 10
         print(increase)

