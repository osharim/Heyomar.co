jQuery(document).ready(function($) {

	
	$CONTENT_DATA = $(".str-data-assyc").animate({ opacity : 1 },3000);	
	$CONTENT_SKILL = $(".content_skill").children(".skill");
	$SKILL = $(".skill");


	for (var i = 0; i < $CONTENT_SKILL.length; i++) {
		
 	var $current_skill = $($CONTENT_SKILL[i]);

		$current_skill.animate({ width : $current_skill.attr('data')+'%' },2000) 

	};
 

});