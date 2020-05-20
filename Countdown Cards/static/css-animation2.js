// Original JavaScript code by Chirp Internet: www.chirp.com.au
// Please acknowledge use of this code by including this header.

var CardGame = function(targetId)
{
  // private variables
  var cards = []

  var card_value = ["1C","2C","3C","4C","5C","6C","7C","8C","9C","10C","1H","2H","3H","4H","5H","6H","7H","8H","9H","10H"];
  var numbers = [ '&#x1F0D1', '&#x1F0D2', '&#x1F0D3', '&#x1F0D4', '&#x1F0D5', '&#x1F0D6', '&#x1F0D7', '&#x1F0D8', '&#x1F0D9', '&#x1F0DA','&#x1F0B1', '&#x1F0B2', '&#x1F0B3', '&#x1F0B4', '&#x1F0B5', '&#x1F0B6', '&#x1F0B7', '&#x1F0B8', '&#x1F0B9' ];
  var tot_cards = 18;
  var started = false;
  var matches_found = 0;
  var card1 = false, card2 = false;

  var hideCard = function(id) // turn card face down
  {
    cards[id].innerHTML = "&#x1F0A0";
    with(cards[id].style) {
      transform = "scale(1.0)";
    }
  };

  var moveToPack = function(id) // move card to pack
  {
    hideCard(id);
    cards[id].matched = true;
    cards[id].innerHTML = "&#x1F0CF"
    with(cards[id].style) {
      //zIndex = "1000";
      //top = "100px";
      //left = "-140px";
      //transform = "rotate(0deg)";
      //zIndex = "0";
      display = "hidden";
    }
  };

  var moveToPlace = function(id) // deal card
  {
    cards[id].matched = false;
    with(cards[id].style) {
      zIndex = "1000";
      //transform = "rotate(" + (Math.floor(Math.random() * 5) + 178) + "deg)";
      //zIndex = "0";

    }
  };

  var showCard = function(id) // turn card face up, check for match
  {
    if(id === card1) return;
    if(cards[id].matched) return;
    cards[id].innerHTML = shuffledCards[cards[id].id];
    console.log(cards[id]);
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
      if(parseInt(card_value[card1]) == parseInt(card_value[card2])) { // match found
        (function(card1, card2) {
          setTimeout(function() { moveToPack(card1); moveToPack(card2); }, 1000);
        })(card1, card2);
        if(++matches_found == 8) { // game over, reset
          matches_found = 0;
          started = false;
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
    if(started) {
      showCard(id);
    } else {
      // shuffle and deal cards
      //card_value.sort(function() { return Math.round(Math.random()) - 0.5; });
      //for(i=0; i < 18; i++) {
      //  (function(idx) {
      //    setTimeout(function() { moveToPlace(idx); }, idx * 100);
      //  })(i);
      //}
      started = true;
    }
  };

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
  felt.id = "felt";
  stage.appendChild(felt);

  // template for card
  var card = document.createElement("div");
  card.innerHTML = "&#x1F0A0";

  for(var i=0; i < tot_cards; i++) {
    var newCard = card.cloneNode(true);
    //newCard.innerHTML = numbers[i];
    var shuffledCards = shuffle(numbers.slice());
    newCard.id = numbers.indexOf(shuffledCards[i]);
    //newCard.fromtop = 15 + 120 * Math.floor(i/6);
    //newCard.fromleft = 70 + 100 * (i%6);
    (function(idx) {
      newCard.addEventListener("click", function() { cardClick(idx); }, false);
    })(i);
    started = true;
    felt.appendChild(newCard);
    cards.push(newCard);
  }
}
