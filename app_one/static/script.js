$(document).ready(function(){
  $('#planet_wrapper').hide(function(){
  })
  $('#travel_menu').click(function(){
    $('#planet_wrapper').slideToggle()
  })
})

var count=300;

var counter=setInterval(timer, 1000); //1000 will  run it every 1 second

function timer()
{
  count=count-1;
  if (count <= 0)
  {
     clearInterval(counter);
     //counter ended, do something here
     return;
  }

  //Do code for showing the number of seconds here
}
