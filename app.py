from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
import json

# Crear una instancia de la aplicación Flask
app = Flask(__name__)
# Establecer una clave secreta para la sesión
app.secret_key = 'supersecretkey'

# Base de datos ficticia de usuarios
users = {'testuser': 'password123'}

@app.route('/')
def home():
    """
    Ruta para la página principal.
    Renderiza la plantilla 'index.html'.
    """
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Ruta para el inicio de sesión.
    Maneja tanto las solicitudes GET como POST.
    """
    if request.method == 'POST':
        # Obtener el nombre de usuario y la contraseña del formulario
        username = request.form['username']
        password = request.form['password']
        
        # Verificar si el nombre de usuario y la contraseña coinciden
        if username in users and users[username] == password:
            # Almacenar el nombre de usuario en la sesión
            session['username'] = username
            # Mostrar un mensaje flash de éxito
            flash('Login successful!', 'success')
            # Redirigir al tablero
            return redirect(url_for('dashboard'))
        else:
            # Mostrar un mensaje flash de error si las credenciales no son correctas
            flash('Login unsuccessful. Please check username and password', 'danger')
    
    # Renderizar la plantilla 'login.html'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """
    Ruta para el tablero de usuario.
    Requiere que el usuario esté autenticado.
    """
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




@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    """
    Ruta para agregar datos.
    Maneja tanto las solicitudes GET como POST.
    """
    if request.method == 'POST':
        # Obtener los datos del formulario y convertirlos a un diccionario normal
        data = request.form.to_dict()

        # Convertir las cadenas de texto en listas
        data['videojuegosFavoritos'] = data['videojuegosFavoritos'].split(',')
        data['generosPreferidos'] = data['generosPreferidos'].split(',')
        data['plataformasJuego'] = data['plataformasJuego'].split(',')

        # Leer el dataset actual
        with open('dataset.json', 'r') as file:
            dataset = json.load(file)

        # Agregar los nuevos datos al dataset
        dataset.append(data)

        # Guardar el dataset actualizado
        with open('dataset.json', 'w') as file:
            json.dump(dataset, file)

        # Mostrar un mensaje flash de éxito
        flash('Data added successfully!', 'success')

        # Redirigir a la página principal
        return redirect(url_for('home'))

    # Renderizar la plantilla 'add_data.html' para las solicitudes GET
    return render_template('add_data.html')

if __name__ == '__main__':
    # Ejecutar la aplicación en modo de depuración
    app.run(debug=True)
