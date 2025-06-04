# Automatic-Shift-Scheduler

This is a CLI-based shift scheduling system developed in Python for my university's Data Structures & Algorithms course.
It solves the following problem:
> Implement an automatic shifts arrangement system. **Problem description:** Given m staffs and n days, find an arrangement that can satisfy (1) each staff must take at least k days off; (2) given that each day requires at least aᵢ(1<=i<=n) staffs for working, the arrangement on each day should have more than aᵢ staffs (when possible).

The system I developed allows weekly shift scheduling with CSV/Excel import/export, supports historical schedule data for weekend fairness calibration, and enables dynamic leave handling.

## Features
- **Weekly scheduling**, with 7-day planning windows
- **Customizable staff count**, rest requirements, and daily minimums
- **Leave request handling** (eg, emergency or sick leave)
- **Data import**, for balancing weekend shifts
- **Export to CSV and Excel**, for easy sharing and adjustments
- **Schedule validation**, to ensure constraints are met

## Prerequisites 
Make sure you have Python 3.10+ installed. To use Excel export or import, install:

```
pip install openpyxl
```

## How it works 
This project is built in Python and runs entirely in a CLI. It is composed of two main files 
- ```main.py``` - handles the CLI, meny system and all user interaction 
- ```shift_planner.py``` - contains the logic for schedule generation, validation and display; leave requests handling and data import/export to CSV or Excel

### Core Concepts
- Staff representation: Each staff member is modeled as an object with a weekly schedule of boleans ```True = WORK, False = OFF```. They can be assigned shifts and checked for days off.
- Schedule generation: The system randomly assigns staff to workdays, making sure each person gets at least **k** days off and each day gets at least **aᵢ** staff. If a person is overbooked, shifts are removed to ensure they meet their off-day requirement.
- Leave handling: You can mark specific staff as ```OFF``` on a given day (e.g, sick leave). The system will try to automatically find a replacement to maintain coverage.
- Weekend fairness with history: you can import previous week schedules via .csv or .xlsx files to balance staff assigned to weekends in the new week.
- Exporting: Generated schedules can be saved as .csv or .xlsx format for external use or manual adjustments.

### Data Structures: 
- ```List[Staff]```: A list of Staff objects that represents the "workforce".
- ```List[List[bool]]```: A 2D matrix (schedule_matrix) tracks WORK/OFF status for each staff per day.
- ```Set``` and ```List``` are used to track available staff and shuffle assignments for randomization.
- Past schedures are stored as a ```List[List[List[bool]]]```. One week per staff per day
### Algorithms 
- Randomized assignments: For each day, the system randomly selects staff while checking off-day constraints
- Greedy reassignment: If someone goes on leave, a replacement is found by scanning for a staff member wo his off that day and has enough remaining days off.
- Post-Processing constraints checking: After initial generation, the system iterates over each staff to ensure they meet k off-days, adjusting if necessary.
-Fair Weekend Distribution: On Saturday and Sundays, the scheduler sorts staff based on how many weekend shifts they've had in previous weeks (from imported data) and how many weekend shifts they've been assigned so far this week, ensuring that weekend duties are evenly rotated across weeks, avoiding unfair workloads. 

## Future Improvements
Since this was a university project, I don't plan to come back to it. However, here are some possible updates I might do to this project in the future: 
- Shift preferences per staff
- Different roles handling
- GUI version
- Vacation handling
