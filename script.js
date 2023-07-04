document.getElementById('show_plans').addEventListener('click', function() {
    // Get input values
    let noBedroom = document.getElementById('no_bedroom').value;
    let noBath = document.getElementById('no_bath').value;
    let cars = document.getElementById('cars').value;
   localStorage.setItem("noBed",noBedroom);
   localStorage.setItem("cars",cars);
   localStorage.setItem("Bath",noBath);       
   window.location.href("plans.html")
  });
  
