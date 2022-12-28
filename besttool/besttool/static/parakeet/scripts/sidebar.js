function toggleSidebar() {
  if ($('.wrapper-side').hasClass('toggled')) {
    $('.wrapper-side').removeClass('toggled');
    // $('.wrapper-side:not(.maintain-width)').css('min-width', '12rem');
    sessionStorage.setItem('sideBar', 'true');
  }
  else {
    $('.wrapper-side').addClass('toggled');
    $('.side-toggler').addClass('d-md-inline-block');
    //$('.wrapper-side:not(.maintain-width)').css('min-width', '0');
    sessionStorage.setItem('sideBar', 'false');
  }
}

function sidebarTooltip() {
  if ($('.sidenav a[data-original-title]').length == 0) {
    $('.sidenav a[data-toggle="tooltip"]').tooltip();
  }
  if ($(window).width() < 992) {
    $('.sidenav a[data-original-title]').tooltip('enable');
  } else {
    $('.sidenav a[data-original-title]').tooltip('disable');
  }
}

$(function() {
  if (sessionStorage.getItem('sideBar') == null) {
    sessionStorage.setItem('sideBar', 'true');
  }
  if (sessionStorage.getItem('sideBar') == 'true') {
    toggleSidebar(true);
  }
  // else $('.wrapper-side:not(.maintain-width)').css('min-width', '0');

  //Delay loading of selected classes for transition animation and position fixed.
  setTimeout(function() {
    $('.wrapper-side').addClass('sidebar-transition d-md-block');
    $('.sidebar-wrapper').addClass('position-fixed');
  })
  sidebarTooltip();

  $(window).on('resize', function () {
    sidebarTooltip();
  })

  //Change expandable icons
  $('#integration-sidebar').on('show.bs.collapse', function () {
    $('.sidenav i.fa-caret-down').removeClass('fa-caret-down').addClass('fa-caret-up');
  }).on('hide.bs.collapse', function () {
    $('.sidenav i.fa-caret-up').removeClass('fa-caret-up').addClass('fa-caret-down');
  })
})