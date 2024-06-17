from flask import Flask, render_template, redirect, url_for, request, session, flash
import json
from datetime import timedelta

# Crear una instancia de la aplicación Flask
app = Flask(__name__)
# Establecer una clave secreta para la sesión
app.secret_key = 'supersecretkey'
# Configurar la duración de la sesión
app.permanent_session_lifetime = timedelta(minutes=1)

with open('dataset.json', 'r') as f:
    usersdb = json.load(f)

@app.route('/')
def home():
   
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        # Obtener el nombre de usuario y la contraseña del formulario
        username = request.form['username']
        password = request.form['password']
        
        # Verificar si el nombre de usuario y la contraseña coinciden en usersdb
        user = next((user for user in usersdb if user['nombreUsuario'] == username and user['id'] == password), None)
        
        if user:
            # Establecer la sesión como permanente y almacenar el nombre de usuario
            session.permanent = True
            session['username'] = username
            # Mostrar un mensaje flash de éxito
            flash('Login successful!', 'success')
            # Redirigir al dashboard
            return redirect(url_for('dashboard'))
        else:
            # Mostrar un mensaje flash de error si las credenciales no son correctas
            flash('Login unsuccessful. Please check username and password', 'danger')
    
    # Renderizar la plantilla 'login.html'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
   
    if 'username' in session:
        # Renderizar la plantilla 'dashboard.html' con el nombre de usuario
        return render_template('dashboard.html', name=session['username'])
    else:
        # Mostrar un mensaje flash si el usuario no está autenticado
        flash('You need to login first.', 'danger')
        # Redirigir a la página de inicio de sesión
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    """
    Ruta para cerrar sesión.
    Elimina el nombre de usuario de la sesión.
    """
    # Eliminar el nombre de usuario de la sesión
    session.pop('username', None)
    # Mostrar un mensaje flash de éxito
    flash('You have been logged out.', 'success')
    # Redirigir a la página principal
    return redirect(url_for('home'))

# Encontrar la cantidad de juegos, géneros y plataformas compartidas de los usuarios
def find_common_interests(user1, user2):
    shared_games = set(user1['videojuegosFavoritos']) & set(user2['videojuegosFavoritos'])
    shared_genres = set(user1['generosPreferidos']) & set(user2['generosPreferidos'])
    shared_platforms = set(user1['plataformasJuego']) & set(user2['plataformasJuego'])
    total_shared = len(shared_games) + len(shared_genres) + len(shared_platforms)
    return total_shared

# Retorna los 5 usuarios con los que comparte más intereses
def get_recommended_users(current_user):
    recommendations = []
    for user in usersdb:
        if user['id'] != current_user['id']:
            shared_interests = find_common_interests(current_user, user)
            if shared_interests > 0:
                user['shared_interests'] = shared_interests
                recommendations.append(user)
    recommendations.sort(key=lambda x: x['shared_interests'], reverse=True)
    return recommendations[:5]

@app.route('/search', methods=['GET', 'POST'])
def search_users():
    search_results = []
    recommended_users = []
    logged_in_user = None

    if request.method == 'POST':
        search_username = request.form['search-username'].strip()
        search_results = [user for user in usersdb if search_username.lower() in user['nombreUsuario'].lower()]

    if 'username' in session:
        logged_in_user = next((user for user in usersdb if user['nombreUsuario'] == session['username']), None)
        if logged_in_user:
            recommended_users = get_recommended_users(logged_in_user)

    return render_template('search_users.html', search_results=search_results, recommended_users=recommended_users, logged_in_user=logged_in_user)

if __name__ == '__main__':
    # Ejecutar la aplicación en modo de depuración
    app.run(debug=True)
