function simulateButtonClick() {
  var reqButton = document.querySelector('.reqbtn');
  var startTime = new Date();

  reqButton.click();
  console.log('reqbtn clicked at:', startTime);

  // Wait for the reqbtn click to be processed before clicking alert_ok
  setTimeout(function () {
    var okButton = document.querySelector('#alert_ok');
    okButton.click();
    console.log('alert_ok clicked at:', new Date());
    
    var endTime = new Date();
    var elapsedTime = endTime - startTime;
    
    // Adjust the interval based on the time it took to execute
    var adjustedInterval = 58000 - elapsedTime;
    
    // Set the new interval for the next execution, considering the 10-second delay
    setTimeout(function() {
      setInterval(simulateButtonClick, 58000);
    }, adjustedInterval > 10000 ? adjustedInterval - 10000 : 0);
  }, 0); // Use a minimal timeout to wait for the reqbtn click to be processed
}

simulateButtonClick();
function simulateButtonClick() {
  // Calculate the time until the next minute and set timeout accordingly for reqButton
  var now = new Date();
  var nextMinute = new Date(now);
  nextMinute.setSeconds(0);
  nextMinute.setMilliseconds(0);
  var timeUntilNextMinute = 58000 - (now.getTime() - nextMinute.getTime());

  setTimeout(function () {
    var reqButton = document.querySelector('.reqbtn');
    reqButton.click();
    console.log('reqbtn clicked at:', new Date());

    // Set a timeout to click the second button after 10 seconds
    setTimeout(function () {
      var okButton = document.querySelector('#alert_ok');
      okButton.click();
      console.log('alert_ok clicked at:', new Date());
    }, 10000); // 10 seconds in milliseconds
  }, timeUntilNextMinute);
}

// Set the interval to simulate the button click every 60 seconds
setInterval(simulateButtonClick, 58000);
