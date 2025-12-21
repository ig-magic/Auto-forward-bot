from flask import Flask
import time

app = Flask(__name__)
START_TIME = time.time()

@app.route('/')
def hello_world():
    uptime = int(time.time() - START_TIME)
    hours = uptime // 3600
    minutes = (uptime % 3600) // 60
    seconds = uptime % 60

    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Bot Status</title>
    <style>
        body {{
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: radial-gradient(circle at top, #0f2027, #000);
            font-family: Arial, Helvetica, sans-serif;
            color: #ffffff;
        }}
        .box {{
            text-align: center;
            padding: 45px 70px;
            border-radius: 18px;
            background: rgba(255, 255, 255, 0.08);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.6);
        }}
        .pulse {{
            width: 18px;
            height: 18px;
            background: #00ff88;
            border-radius: 50%;
            margin: 0 auto 18px;
            box-shadow: 0 0 0 rgba(0, 255, 136, 0.7);
            animation: pulse 1.5s infinite;
        }}
        h1 {{
            margin: 0;
            font-size: 42px;
        }}
        p {{
            margin-top: 10px;
            font-size: 18px;
            opacity: 0.85;
        }}
        .uptime {{
            margin-top: 14px;
            font-size: 16px;
            color: #00ff88;
        }}
        @keyframes pulse {{
            0% {{
                box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.7);
            }}
            70% {{
                box-shadow: 0 0 0 18px rgba(0, 255, 136, 0);
            }}
            100% {{
                box-shadow: 0 0 0 0 rgba(0, 255, 136, 0);
            }}
        }}
    </style>
</head>
<body>
    <div class="box">
        <div class="pulse"></div>
        <h1>🤖 BOT IS RUNNING</h1>
        <p>Everything looks good 🤌</p>
        <div class="uptime">
            ⏱️ Uptime: {hours}h {minutes}m {seconds}s
        </div>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run()
