from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Flask Welcome App</title>
    <style>
      body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #f4f4f9; }
      .card { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 100%; max-width: 400px; text-align: center; }
      input[type="text"] { width: 80%; padding: 0.5rem; margin: 1rem 0; border: 1px solid #ccc; border-radius: 4px; }
      button, .btn { background: #007bff; color: white; border: none; padding: 0.5rem 1rem; border-radius: 4px; cursor: pointer; text-decoration: none; display: inline-block; }
      button:hover, .btn:hover { background: #0056b3; }
      .message { font-size: 1.2rem; color: #333; margin-bottom: 1.5rem; }
      .nav-link { display: block; margin-top: 1rem; font-size: 0.9rem; color: #007bff; text-decoration: none; }
      .nav-link:hover { text-decoration: underline; }
    </style>
  </head>
  <body>
    <div class="card">
      {% if not name %}
        <h2>Welcome!</h2>
        <form method="POST">
          <label for="name">Enter your name:</label><br>
          <input type="text" id="name" name="name" required autocomplete="off"><br>
          <button type="submit">Submit</button>
        </form>
        <a href="/about" class="nav-link">About this project</a>
      {% else %}
        <div class="message">
          Hello, <strong>{{ name }}</strong>! Welcome to the application.
        </div>
        <a href="/" class="btn">Back</a>
      {% endif %}
    </div>
  </body>
</html>
"""

ABOUT_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>About - What I Would Build</title>
    <style>
      body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #f4f4f9; }
      .card { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 100%; max-width: 550px; text-align: left; line-height: 1.6; color: #333; }
      h2 { color: #007bff; margin-top: 0; text-align: center; }
      .btn { background: #007bff; color: white; border: none; padding: 0.5rem 1rem; border-radius: 4px; cursor: pointer; text-decoration: none; display: inline-block; margin-top: 1.5rem; }
      .btn:hover { background: #0056b3; }
      .center { text-align: center; }
    </style>
  </head>
  <body>
    <div class="card">
      <h2>What I Would Build in an Evening</h2>
      <p>If I had an entire evening instead of just a quarter of time to build something meaningful, I would create a smart daily task tracker tailored for work-life balance. Unlike standard to-do lists, this application would feature distinct categories for 'Household' and 'Personal' goals to ensure everyday management stays structured. Users could create tasks, tick them off as completed, and instantly view a dynamic completion percentage progress bar for each category. Crucially, it would include a daily reset mechanism to clear completed items and prep for the next day. This project would serve as a fantastic vehicle to demonstrate core low-code and full-stack capabilities, effectively combining HTML forms for data entry, backend data storage, filtering logic, and real-time calculations to provide an engaging and practical user experience.</p>
      <div class="center">
        <a href="/" class="btn">Back to Home</a>
      </div>
    </div>
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    user_name = None
    if request.method == "POST":
        user_name = request.form.get("name")
    return render_template_string(HTML_TEMPLATE, name=user_name)

@app.route("/about")
def about():
    return render_template_string(ABOUT_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True)