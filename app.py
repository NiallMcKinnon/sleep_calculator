from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_time = request.form['bedtime']
        wake_times = calculate_waking_times(selected_time)
        return render_template('index.html', wake_times=wake_times, bedtime=selected_time)
    else:
        return render_template('index.html')

def calculate_waking_times(bedtime):
    temp = bedtime.split(':')
    bed_hour = int(temp[0])
    bed_min = int(temp[1]) 
    
    wake_times = []
    current_hour = bed_hour
    current_min = bed_min
    for i in range(7):
        if (i == 0):
            current_min += 20
        
        current_hour += 1
        current_min += 30
        
        if current_min > 59:
            current_min -= 60
            current_hour += 1
            
        if current_hour > 23:
            current_hour -= 24
        
        wake_times.append(f"{current_hour:02}:{current_min:02}")
    
    return wake_times
