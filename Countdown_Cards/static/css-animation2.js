// Original JavaScript code by Chirp Internet: www.chirp.com.au
// Please acknowledge use of this code by including this header.


var CardGame = function(targetId)
{
  // private variables
  var cards = []
  var card_value = ["1C","2C","3C","4C","5C","6C","7C","8C","9C","10C","11C","12C","13C","1H","2H","3H","4H","5H","6H","7H","8H","9H","10H","11H","12H","13H","1S","2S","3S","4S","5S","6S","7S","8S","9S","10S","11S","12S","13S","1D","2D","3D","4D","5D","6D","7D","8D","9D","10D","11D","12D","13D"];
  var numbers = [ '&#x1F0D1', '&#x1F0D2', '&#x1F0D3', '&#x1F0D4', '&#x1F0D5', '&#x1F0D6', '&#x1F0D7', '&#x1F0D8', '&#x1F0D9', '&#x1F0DA', '&#x1F0DB', '&#x1F0DD', '&#x1F0DE','&#x1F0B1', '&#x1F0B2', '&#x1F0B3', '&#x1F0B4', '&#x1F0B5', '&#x1F0B6', '&#x1F0B7', '&#x1F0B8', '&#x1F0B9', '&#x1F0BA', '&#x1F0BB', '&#x1F0BD', '&#x1F0BE','&#x1F0A1', '&#x1F0A2', '&#x1F0A3', '&#x1F0A4', '&#x1F0A5', '&#x1F0A6', '&#x1F0A7', '&#x1F0A8', '&#x1F0A9', '&#x1F0AA', '&#x1F0AB', '&#x1F0AD', '&#x1F0AE','&#x1F0C1', '&#x1F0C2', '&#x1F0C3', '&#x1F0C4', '&#x1F0C5', '&#x1F0C6', '&#x1F0C7', '&#x1F0C8', '&#x1F0C9', '&#x1F0CA', '&#x1F0CB', '&#x1F0CD', '&#x1F0CE' ];
  var total_cards = card_value.length;
  var started = false;
  var matches_found = 0;
  var card1 = false, card2 = false;
  var firstClick = true;

  var hideCard = function(id) // turn card face down
  {
    cards[id].innerHTML = "&#x1F0A0";
    with(cards[id].style) {
    transform = "scale(1.0)";
    }
  };

  var showCard = function(id) // turn card face up, check for match
  {
    if(id === card1) return;
    if(cards[id].matched) return;
    cards[id].innerHTML = cards[id].getAttribute('cardunicode');
    with(cards[id].style) {
      // Firefox doesn't know which way to rotate
      if(matches = transform.match(/^rotate\((\d+)deg\)$/)) {
        if(matches[1] <= 180) {
          transform = "scale(1.2)";
        } else {
          transform = "scale(1.2)";
        }
      } else {
        transform = "scale(1.2)";
      }
    }

    if(card1 !== false) {
      card2 = id;
      if(parseInt(card_value[cards[card1].id]) == parseInt(card_value[cards[card2].id])) { // match found
        (function(card1, card2) {
          setTimeout(function() { cardMatched(card1); cardMatched(card2); }, 600);
        })(card1, card2);
        if(++matches_found == total_cards/2) { // game over, reset
          pauseTimer();
          final_time = document.getElementById('stopwatch').innerHTML
          matches_found = 0;
          started = false;
          alert("Well Done, Your time was " + final_time);
        }

      } else { // no match
        (function(card1, card2) {
          setTimeout(function() { hideCard(card1); hideCard(card2); }, 800);
        })(card1, card2);
      }
      card1 = card2 = false;
    } else { // first card turned over
      card1 = id;

    }
  };

  var cardClick = function(id)
  {
    if (firstClick == true) {
      startTimer();
      if(started) {
        showCard(id);
      } else {
        started = true;
  			showCard(id);
      }
      firstClick = false;
  } else {
    started = true;
    showCard(id);
  }
  };
  var cardMatched = function(card)
  {
    //disable clocking on the card
    cards[card].style.pointerEvents = 'none';
    //set the card to the joker image
    cards[card].innerHTML = "&#x1F0DF";
    //disable the transform on the card
    cards[card].style.transform = "scale(1)";
  }
  // initialise
  var shuffle = function (array) {

  	var currentIndex = array.length;
  	var temporaryValue, randomIndex;

  	// While there remain elements to shuffle...
  	while (0 !== currentIndex) {
  		// Pick a remaining element...
  		randomIndex = Math.floor(Math.random() * currentIndex);
  		currentIndex -= 1;

  		// And swap it with the current element.
  		temporaryValue = array[currentIndex];
  		array[currentIndex] = array[randomIndex];
  		array[randomIndex] = temporaryValue;
  	}

  	return array;

  };


  var stage = document.getElementById(targetId);
  var felt = document.createElement("div");
  var stopwatch = document.getElementById('stopwatch');
  felt.id = "felt";
  stage.appendChild(felt);
  // template for card
  var card = document.createElement("div");
  card.innerHTML = "&#x1F0A0";
  var shuffledCards = shuffle(numbers.slice());
  for(var i=0; i < total_cards; i++) {
    var newCard = card.cloneNode(true);
    newCard.id = numbers.indexOf(shuffledCards[i]);
    newCard.setAttribute("cardunicode", shuffledCards[i]);
    (function(idx) {
      newCard.addEventListener("click", function() { cardClick(idx); }, false);
    })(i);
    started = true;
    felt.appendChild(newCard);
    cards.push(newCard);

  }
}
