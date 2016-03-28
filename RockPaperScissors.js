/*var userChoice = prompt("Do you choose rock, paper or scissors?");
var computerChoice = Math.random();
if (computerChoice < 0.34) {
	computerChoice = "rock";
} else if(computerChoice <= 0.67) {
	computerChoice = "paper";
} else {
	computerChoice = "scissors";
}

compare(userChoice,computerChoice);*/
RPS();

var validChoice = function(choice){
	if (choice != "rock" && choice != "paper" && choice != "scissors"){
		return false;
	}else{
		return true;
	}
}

var compare = function(choice1,choice2){
    if (choice1 === choice2){
        return "The result is a tie!";
    }
    if (choice1 === "rock"){
        if (choice2 === "scissors"){
            return "rock wins";
        }else{
            return "paper wins";
        }
    }
    if (choice1 === "paper"){
        if (choice2 === "rock"){
            return "paper wins";
        }else{
            return "scissors wins";
        }
    }
    if (choice1 === "scissors"){
        if (choice2 === "paper"){
            return "scissors wins";
        }else{
            return "rock wins";
        }
    }
}

var computerChooser = function(){
    var choice = Math.random();
    if (choice < 0.34) {
        choice = "rock";
    } else if(choice <= 0.67) {
        choice = "paper";
    } else {
        choice = "scissors";
    }
    return choice;
}

var RPS = function(){
    var userChoice = prompt("Do you choose rock, paper or scissors?");
	while (validChoice(userChoice) === false){
		userChoice = prompt("Your choice is invalid. Choose rock, paper or scissors.");
	}
    var computerChoice = computerChooser();
	while (validChoice(computerChoice) === false){
		computerChoice = computerChooser();
	}
    var result = compare(userChoice,computerChoice);
    
    if (result === "The choice is a tie!"){
        alert("You both guessed " + userChoice + " and I won't allow it. Guess again.");
        RPS();
    }
    
    return result;
}

//2144028244