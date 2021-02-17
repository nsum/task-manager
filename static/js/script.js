$(document).ready(function(){
    // Code to initialize mobile nav
    $('.sidenav').sidenav({edge: "right"});
    // initialize accordion collapse
    $('.collapsible').collapsible();
    // enable urgent task tooltip
    $('.tooltipped').tooltip();
    // enable category select dropdown in new task creation
    $('select').formSelect();
    // enable date picker when creating new task
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
  });