$.fn.tallier = function(action) {
  var $this = this,
  bgUrl = '../static/tally.png',
  bgHeight = 62,
  bgVals = [
    [22, 12],
    [32, -17],
    [42, -57],
    [52, -107],
    [70, -180]
  ];

  if ($this.data("count") == undefined) {
    $this.data("count", 0);
  }

  var add = function() {
    $this.data("count", $this.data("count") + 1);
    var count = $this.data("count");
    if (count % 5 == 1) {
      var $newTally = $('<div>').addClass('tally');
      $newTally.css({
        background: 'url("' + bgUrl + '") ' +
          bgVals[0][1] + 'px 0 no-repeat transparent',
        float: 'left',
        width: bgVals[0][0] + 'px',
        height: bgHeight + 'px'
      });
      $this.append($newTally);
    }
    var $lastTally = $this.find('.tally:last'),
      i = count % 5 - 1;
    i = i < 0 ? 4 : i;
    $lastTally.css({
      'background-position': bgVals[i][1] + 'px 0',
      width: bgVals[i][0] + 'px'
    });
  };

  var sub = function() {
    if ($this.data("count") == 1) {
      return false;
    }
    $this.data("count", $this.data("count") - 1);
    var count = $this.data("count");
    var $lastTally = $this.find('.tally:last');
    if (count % 5 == 0) {
      $lastTally.remove();
    } else {
      var i = count % 5 - 1;
      i = i < 0 ? 4 : i;
      $lastTally.css({
        'background-position': bgVals[i][1] + 'px 0',
        width: bgVals[i][0] + 'px'
      });
    }
  };
  if (action == "add") {
    tallied = document.getElementById("tallied").getAttribute("value");
    tallied ++;
    document.getElementById("tallied").setAttribute('value', tallied);
    add();
  } else {
    tallied = document.getElementById("tallied").getAttribute("value");
    if (tallied > 0) {
      tallied --;
      document.getElementById("tallied").setAttribute('value', tallied);
    }
    sub();
  }
}

var $t = $('#tally');

$t.tallier("add");

$t.click(function() {
  $t.tallier("add");
});

$(".remove").click(function() {
  $t.tallier("sub");
});