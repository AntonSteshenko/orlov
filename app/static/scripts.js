$(document).ready(function() {
    /*
        Dropdowns initialization
    */
    $(".dropdown-trigger").dropdown({
        coverTrigger: false
    });


    /*
        Sidenav initialization
    */
    $('.sidenav').sidenav();


    /*
        Collapsible initialization
    */
    $('.collapsible').collapsible();


    /*
        Datetimepicker initialization
    */
    $('[data-form-control="datetime"]').datetimepicker({
        format: 'd.m.Y H:i'
    });
});