$(document).ready(function(){


	$("body").queryLoader2({

		barColor:"#eee",
		backgroundColor:"#000011",
		percentage:true,
		barHeight:1,
		deepSearch:true,

		completeAnimation:"fade",

		onComplete:function(){
			
				
	$(".message-content ul").animate({ 'padding-right' : '20%' , 'opacity' : 1 },1100,function(){

		
	})

$(".message-content ul li:last-child").delay(600).animate({ 'padding-left' : '0' },600)
	



		}
							});

});