/**
 * Created by user on 01.07.2017.
 */

$(document).ready(function () {

    // Select active section in top menu
   var uri = $(location).attr('href');
   if(uri.search('/questions/') > 0) {
       $('#nav-1').toggleClass('active-nav-btn');
   }
   else if(uri.search('/jobs/') > 0) {
       $('#nav-2').toggleClass('active-nav-btn');
   }
   else if(uri.search('/documentations/') > 0) {
       $('#nav-3').toggleClass('active-nav-btn');
   }
   else if(uri.search('/tags/') > 0) {
       $('#nav-4').toggleClass('active-nav-btn');
   }
   else if(uri.search('/users/') > 0) {
       $('#nav-5').toggleClass('active-nav-btn');
   }


   $('.js-dynamic-tag').on('mouseenter', function (e) {
       var block;
       if($(e.target).parents('.js-dynamic-tag').length) {
           return false;
       }
       block = $(e.target).find('.js-hidden-tag-info');
       if(!block.length) {
           var tag_id = $(e.target).attr('data-tag-id');
           $.ajax({
               url: '/tags/ajax_get_tag_sticker/',
               type: 'get',
               data: {
                   tag_id: tag_id
               }
           })
               .done(function (data) {
                   $(e.target).append(data);
                   $(e.target).find('.js-hidden-tag-info').fadeIn(400);
               });
       }
       else {
           block.css('display', 'block');
       }
   }).on('mouseleave', function (e) {
       var block = $(e.target);
       if(block.hasClass('.js-hidden-tag-info')) {
           block.fadeOut(400);
       }
       else if($('div.js-hidden-tag-info:first', this).length) {
           $('div.js-hidden-tag-info:first', this).fadeOut(400);
       }
   });

});