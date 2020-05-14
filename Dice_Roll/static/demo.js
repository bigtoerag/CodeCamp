(function() {
  'use strict';

  var settings = [
    {
      el: '#wheel-1',
      members: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
      colors: ['#ff0000', '#000000', '#ff0000', '#000000', '#ff0000', '#000000', '#ff0000', '#000000', '#ff0000', '#000000'],
      radius: 200,
      startAngle: 'random'
    }
  ];

  var wheels = [
    new PrizeWheel(settings[0])
  ];

  wheels.forEach(function(wheel) {
    wheel.init();
  });

  var spinBtn = document.querySelector('.btn-spin');
  var output = document.querySelector('#output');

  spinBtn.addEventListener('click', function(e) {
    output.textContent = '';
    wheels.forEach(function(wheel) {
      wheel.spin(function(member) {
        output.innerHTML = '<br /><strong>' + member + '</strong>';
      });
  }, false);
  });

})();
