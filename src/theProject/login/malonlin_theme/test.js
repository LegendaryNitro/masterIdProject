


$(document).ready(function(){

    setInterval(function(){
        $.ajax({
            type: 'GET',
            url: "{% url 'testing1' %}",
            success: function(response){
                console.log(response);
                $("#cont").empty();
                for(var key in response.code){
                    var temp =response.code[key];
                    $('#cont').append(temp);
                }
            },
            error : function(response){
                alert("error in getting data");

                

                },
        
            })

        }, 1000
      )
    }
)

