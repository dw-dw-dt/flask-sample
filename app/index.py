from flask import Flask, render_template, make_response
import pathlib
app = Flask(__name__)


@app.route("/")
def index():
  files = pathlib.Path('files')
  file_list = [{'title': file.name, 'link': f'/download/{file.name}'} for file in files.iterdir() if file.is_file()]
  return render_template(
    'index.html',
    files=file_list
  )


@app.route("/download/<filename>")
def downloadzip(filename):
    response = make_response()
    response.data  = open(f'./files/{filename}', "rb").read()
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'
    return response


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)