$(function(){
  $('.menu-child').on('click', function(){
      $(this).next().children().children('ul').slideToggle();
      $(this).children().children().children("span").last().toggleClass("glyphicon-chevron-down");
  })
})
$(function(){
  $('#menu-open').on('click', function(){
      $(this).children().children("span:first").toggleClass("glyphicon-chevron-right");
      $(this).parent().parent().prev().toggleClass("menu-hidden");       
  })
})