jQuery(document).ready(function($) {
	

//**********************************************
//hand and apps animate
$content_apps = $(".str_apps").find(".apps");

$hand  = $(".hand").animate({opacity:1,marginRight : "-250px" },2000,function(){

		for (var i = 0; i <=  $content_apps.length ; i++) {
			
			$($content_apps[i]).delay(i*180).fadeIn("slow");
		};

});

//**********************************************





 

});