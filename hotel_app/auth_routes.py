from werkzeug.security import generate_password_hash,
check_password_hash
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

pass
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
if request.method == 'POST':
email = request.form['email']
password = request.form['password']
cursor = db.connection.cursor()
cursor.execute("SELECT * FROM usuarios WHERE email =
%s", (email,))
row = cursor.fetchone()
if row and check_password_hash(row[2], password):
user = Usuario(id=row[0], email=row[1],
password=row[2], nombre=row[3], rol=row[4])
login_user(user)
return redirect(url_for('home'))
else:
flash('Credenciales inválidas')
return render_template('login.html')
