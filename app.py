from flask import Flask
import time

app = Flask(__name__)
START_TIME = time.time()

@app.route('/')
def hello_world():
    uptime = int(time.time() - START_TIME)

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Auto Forward Bot | Status</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
:root {{
  --bg:#0f2027;
  --card:rgba(255,255,255,0.08);
  --text:#ffffff;
  --accent:#00ff88;
}}

body.light {{
  --bg:#f5f7fa;
  --card:#ffffff;
  --text:#111;
  --accent:#0bbf6a;
}}

body {{
  margin:0;
  height:100vh;
  display:flex;
  justify-content:center;
  align-items:center;
  background:var(--bg);
  color:var(--text);
  font-family:Arial, Helvetica, sans-serif;
  transition:.3s;
}}

.card {{
  width:440px;
  padding:32px;
  border-radius:18px;
  background:var(--card);
  box-shadow:0 25px 50px rgba(0,0,0,.45);
}}

.pulse {{
  width:14px;
  height:14px;
  margin:auto;
  background:var(--accent);
  border-radius:50%;
  animation:pulse 1.5s infinite;
}}

@keyframes pulse {{
  0% {{ box-shadow:0 0 0 0 rgba(0,255,136,.7); }}
  70% {{ box-shadow:0 0 0 14px rgba(0,255,136,0); }}
}}

h1 {{
  text-align:center;
  margin:12px 0 4px;
}}

.info {{
  text-align:center;
  font-size:14px;
  opacity:.85;
}}

.info a {{
  color:var(--accent);
  text-decoration:none;
}}

.stat {{
  text-align:center;
  margin-top:10px;
  color:var(--accent);
  font-size:15px;
}}

ul {{
  margin-top:16px;
  font-size:14px;
  padding-left:18px;
}}

.actions {{
  margin-top:18px;
  text-align:center;
}}

button {{
  padding:6px 14px;
  border-radius:8px;
  border:none;
  cursor:pointer;
  background:var(--accent);
  font-weight:bold;
}}

footer {{
  margin-top:14px;
  text-align:center;
  font-size:12px;
  opacity:.6;
}}
</style>
</head>

<body>
<div class="card">

  <div class="pulse"></div>

  <h1>🤖 Auto Forward Bot</h1>

  <div class="info">
    👑 Owner:
    <a href="https://t.me/ig_magic" target="_blank">@ig_magic</a>
  </div>

  <div class="info">
    📢 Channel:
    <a href="https://t.me/MAGICxBots" target="_blank">
      @MAGICxBots
    </a>
  </div>

  <div class="stat">🟢 Status: RUNNING</div>
  <div class="stat" id="uptime"></div>

  <ul>
    <li>Public & Private Channel Forwarding</li>
    <li>Custom Caption & Button Support</li>
    <li>Duplicate Media Skip</li>
    <li>Auto Restart Safe</li>
    <li>Media & Message Forward</li>
  </ul>

  <div class="actions">
    <button onclick="toggleTheme()">🌙 / ☀️ Theme</button>
  </div>

  <footer>
    Powered by Flask · Status Page
  </footer>

</div>

<script>
let sec = {uptime};

function formatTime(s) {{
  let h=Math.floor(s/3600),
      m=Math.floor((s%3600)/60),
      x=s%60;
  return `⏱️ Uptime: ${{h}}h ${{m}}m ${{x}}s`;
}}

function tick(){{
  document.getElementById("uptime").innerText = formatTime(sec++);
}}
setInterval(tick,1000);
tick();

function toggleTheme(){{
  document.body.classList.toggle("light");
  localStorage.theme =
    document.body.classList.contains("light") ? "light" : "dark";
}}

if(localStorage.theme==="light") {{
  document.body.classList.add("light");
}}
</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()
