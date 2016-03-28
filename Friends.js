// var friends = {};

// friends.bill = {firstName: 'Bill',lastName: 'Gates',number: '903-759-7847',address: ['1 Faux Dropout Lane','Redmond','WA','98051']};
// friends.steve = {firstName: 'Steve',lastName: 'Jobs',number: '642-754-5321',address: ['1 Original Lane','Franklin','WA','98051']};

// var list = function(obj){
    // for (var element in obj){
        // console.log(element);
    // }
// };

// var search = function(name){
    // for (var element in friends){
        // if (element.firstname === name){
            // list(element);
            // return element;
        // }
    // }
// };

// search('Steve');

// var words = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","hundred","and","thousand"];
// var count = 0;
// var repeats = 0;
// for (i = 1; i <= 1000; i++){
	// if (i < 20){ count = count + words[i].length; }
	// else if (i >= 20 && i < 100){
		// count = count + words[20 + (i/10) - 2].length + words[i%10].length;
	// }
	// else if (i >= 100 && i < 1000){
		// if (i%100 == 0){
			// if (i == 100) { repeats = count; }
			// count = count + words[i/100].length + words[30].length + repeats;
		// }
		// else{ count = count + words[i/100].length + words[30].length + words[31].length; }
	// }
	// else{ count = count + words[1].length + words[32].length; }
// }

// alert(count);

/****
If you add the feed and add photos, the photos do load.
If you drop the photos, they will not revert.
Photos will not revert unless the entire feed is deleted.
****/

// var count = 0;
// var months = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6];

// for (i = 1901; i <= 2000; i++){
	// if (i > 1901 && i%4 == 1){
		// months[1]++;
		// months[2]++;
	// }else if (i%4 == 0){
		// for (x = 3; x <= 12; x++){months[x]++;}
	// }	
	// for (y = 1; y <= 12; y++){
		// months[y]++;
		// if (months[y] >= 7) months[y]-=7;
		// if (months[y] == 0) count++;
	// }
// }
// alert(count);