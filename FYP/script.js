  function openCity(cityName, elmnt, color) {
    // Hide all elements with class="tabcontent" by default */
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }

    // Remove the background color of all tablinks/buttons
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].style.backgroundColor = "";
    }

    // Show the specific tab content
    document.getElementById(cityName).style.display = "block";
  }

  // Get the element with id="defaultOpen" and click on it
  document.getElementById("defaultOpen").click();

  // Function to show the banner popup
  function showBannerPopup() {
    document.getElementById("bannerPopup").style.display = "block";
    document.getElementById("overlay").style.display = "block";
  }

  // Function to close the banner popup
  function closeBannerPopup() {
    document.getElementById("bannerPopup").style.display = "none";
    document.getElementById("overlay").style.display = "none";
  }

  // Automatically show the popup when the page loads
  window.onload = function () {
    showBannerPopup();
  };

  //calendar
  