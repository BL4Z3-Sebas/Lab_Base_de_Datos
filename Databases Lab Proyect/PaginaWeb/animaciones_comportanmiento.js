document.addEventListener("DOMContentLoaded", () => {

  // selecciona botones
  const botonesComparar = document.querySelectorAll(".boton-comparar");

  // función auxiliar: cierra todos los menús
  function cerrarTodosMenus(excepto = null) {
    document.querySelectorAll(".menu-comparacion").forEach(m => {
      if (m !== excepto) m.classList.add("oculto");
    });
  }

  botonesComparar.forEach(boton => {
    boton.addEventListener("click", (ev) => {
      ev.stopPropagation(); // evitar que el document click los cierre inmediatamente

      // menu está dentro de .control-comparacion según tu HTML
      const contenedor = boton.closest(".control-comparacion");
      const menu = contenedor.querySelector(".menu-comparacion");

      // primero cerramos los otros menús
      cerrarTodosMenus(menu);

      // alternamos clase oculto
      menu.classList.toggle("oculto");

      // si quedó visible, calculamos la posición (evitar salirse de la ventana)
      if (!menu.classList.contains("oculto")) {
        // quitar cualquier posicionamiento previo
        menu.style.left = "";
        menu.style.right = "";
        menu.style.top = "";
        menu.style.transform = "";

        // forzamos render para obtener width (si estaba display:none)
        menu.style.display = "flex";
        const menuRect = menu.getBoundingClientRect();
        const botonRect = boton.getBoundingClientRect();
        const espacioDerecha = window.innerWidth - botonRect.right;
        const espacioIzquierda = botonRect.left;

        // si hay espacio suficiente a la derecha, lo ponemos a la derecha del botón
        if (espacioDerecha > menuRect.width + 16) {
          // posicionamos relativo al contenedor (.control-comparacion)
          menu.style.left = `${boton.offsetLeft + boton.offsetWidth + 10}px`;
          menu.style.top  = `${boton.offsetTop + (boton.offsetHeight/2) - (menuRect.height/2)}px`;
          menu.style.transform = `translateY(0)`; // ya usamos offsetTop
        } else if (espacioIzquierda > menuRect.width + 16) {
          // lo ponemos a la izquierda del botón
          // calculamos distancia desde right del contenedor
          const contW = contenedor.clientWidth;
          const botonRightDentro = contenedor.clientWidth - (boton.offsetLeft + boton.offsetWidth);
          menu.style.right = `${botonRightDentro + 10}px`;
          menu.style.top  = `${boton.offsetTop + (boton.offsetHeight/2) - (menuRect.height/2)}px`;
          menu.style.left = "auto";
          menu.style.transform = `translateY(0)`;
        } else {
          // si no cabe a los lados, colocarlo debajo del botón (fallback)
          menu.style.left = `${boton.offsetLeft}px`;
          menu.style.top  = `${boton.offsetTop + boton.offsetHeight + 8}px`;
          menu.style.transform = `translateY(0)`;
          menu.style.width = "auto";
        }

        // asegurar que si estamos en modo móvil (css media query), el CSS toma control
        // no forzamos display:none aquí; la clase .oculto controla visibilidad
      } else {
        // se ocultó: devolver display por si lo habíamos tocado
        menu.style.display = "";
      }
    });
  });

  // cerrar menús si clic fuera
  document.addEventListener("click", (ev) => {
    // si el click no está dentro de un .control-comparacion
    if (!ev.target.closest(".control-comparacion")) {
      cerrarTodosMenus();
    }
  });

  // prevenir scroll extraño cuando el menú esté abierto y el usuario toque selects
  document.querySelectorAll(".menu-comparacion select").forEach(sel => {
    sel.addEventListener("click", (e) => { e.stopPropagation(); });
  });
  const botonesAplicar = document.querySelectorAll(".boton-aplicar");
  const botonesReset = document.querySelectorAll(".boton-reset");

  botonesAplicar.forEach((boton) => {
    boton.addEventListener("click", (e) => {
      e.preventDefault();

      const contenedor = boton.closest(".menu-comparacion");
      const mes1 = contenedor.querySelector(".mes1").value; /*se guardan los valores al oprimir aplicar*/
      const mes2 = contenedor.querySelector(".mes2").value;

      if (mes1 && mes2) {
        alert(`Comparando ${mes1} vs ${mes2} 📊`);
        // Aquí podrías actualizar la gráfica
      } else {
        alert("⚠️ Por favor selecciona ambos meses antes de aplicar.");
      }
    });
  });

  botonesReset.forEach((boton) => {
    boton.addEventListener("click", (e) => {
      e.preventDefault();

      const contenedor = boton.closest(".menu-comparacion");
      contenedor.querySelector(".mes1").value = "";
      contenedor.querySelector(".mes2").value = "";
      alert("🔄 Selecciones reiniciadas.");
    });
  });

  // mantén el resto de tu lógica de aplicar/reset (si ya la tienes)
  // si no, puedes reaplicar tu código existente para aplicar/reset aquí
});