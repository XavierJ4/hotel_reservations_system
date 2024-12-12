// assets/js/main.js
$(document).ready(function() {
// Código común para todas las páginas
  // Verificar si el usuario está autenticado
  var token = localStorage.getItem('token');
  if (token) {
    // Cambiar el menú para mostrar opciones de usuario
    $('.navbar-nav').html(`
      <li class="nav-item">
        <a class="nav-link" href="cliente/perfil.html">Mi Perfil</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" id="logout">Cerrar Sesión</a>
      </li>
    `);
    // Manejar el cierre de sesión
    $('#logout').click(function() {
      localStorage.removeItem('token');
      window.location.href = 'index.html';
    });
  }
});

