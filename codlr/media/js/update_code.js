jQuery(document).ready(function($) {
	


function update_code(){



id_text_editor = {"id": $("#text_code").attr('data') , 'code' :  $("#text_code").val() }
 

$.ajax({

  url:"/update/",
  
  type:"POST",
  
  data: JSON.stringify( id_text_editor ),
  
  contentType: 'application/json',
  
  dataType:"json",
  
  success: function(data){
    

  	 $("#text_code").val( data[0].fields.code_txt )


}

})

 




}


//*****************

var delay = (function(){
  var timer = 0;
  return function(callback, ms){
    clearTimeout (timer);
    timer = setTimeout(callback, ms);
  };
})();



//**************


 $("#text_code").change(function(){

 
 
update_code();

 
 

});



 

 

 
 setInterval(function(){


code_before_update = $("#text_code").val() 

id_text_editor = {"id": $("#text_code").attr('data') , 'code' : false }
 

$.ajax({

  url:"/update/",
  
  type:"POST",
  
  data: JSON.stringify( id_text_editor ),
  
  contentType: 'application/json',
  
  dataType:"json",
  
  success: function(data){
    
  	if ( code_before_update != data[0].fields.code_txt ){

  		 $("#text_code").val( data[0].fields.code_txt )

  	}
  	


}

})

 


 },2000)




//***************************************************************************


 





























 



});
