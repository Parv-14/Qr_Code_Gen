from flask import Flask, render_template, request, send_file, redirect, url_for
import qrcode
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = 'static/qrcodes'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        fill_color = request.form.get('fill_color')
        back_color = request.form.get('back_color')
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_L,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        unique_filename = f"{uuid.uuid4()}.png"
        qr_code_path = os.path.join(UPLOAD_FOLDER, unique_filename)
        img.save(qr_code_path)

        return render_template('index.html', qr_code_path=qr_code_path)

    return render_template('index.html', qr_code_path='')

@app.route('/download/<filename>')
def download(filename):
    print(filename)
    qr_code_path = f"static/qrcodes/{filename}"
    return send_file(path_or_file=qr_code_path,  as_attachment=True)
    
@app.route('/download/Desi_Ide')
def desi_ide():
    return send_file(path_or_file="static/DESI IDE.zip", as_attachment=True)

@app.route('/cleanup')
def cleanup():
    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=False)
