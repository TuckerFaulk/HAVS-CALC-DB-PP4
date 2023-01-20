// Global Varibles
let belowEAVWarning = "Exposure likely to be below 2.5m/s² A(8) EAV (100 Points).";
let aboveEAVWarning = "WARNING: Exposure at or above 2.5m/s² A(8) EAV (100 Points).";
let aboveELVWarning = "WARNING: Exposure above 5m/s² A(8) ELV (400 Points).";
let belowEAVControls = 
`<p>Where there is a risk to the health of an employee who is, or is liable to be, exposed to vibration, but their exposure is below the EAV, the employer must:</p>

<ol type="a">
  <li>Ensure that the employee is placed under suitable health surveillance.</li>
  <li>Provide the employee with suitable and sufficient information, instruction and training.</li>
</ol>`;
let aboveEAVControls = 
`<p>Where the daily personal HAV exposure is likely to equal or exceed the EAV the employer must:</p>

<ol type="a">
  <li>Reduce exposure to as low a level as is reasonably practicable by establishing and implementing 
  a programme of organisational and technical measures which is appropriate to the activity.</li>
  <li>Ensure that the employee is placed under suitable health surveillance.</li>
  <li>Provide the employee with suitable and sufficient information, instruction and training.</li>
</ol>`;
let aboveELVControls = 
`<p>Where the daily personal HAV exposure is likely to exceed the ELV the employer must take immediate action to:</p>

<ol type="a">
  <li>Reduce exposure to vibration below the limit value.</li>
  <li>Identify the reason for the limit being exceeded.</li>
  <li>Modify the measures taken to prevent it being exceeded again.</li>
</ol>`;


// Event listeners added on DomContentLoaded
document.addEventListener("DOMContentLoaded", function() {

  // Alert Meassage TimeOut

  setTimeout(function () {
    $('#msg').alert('close');
  }, 2500);

  /**
 * Calculates Daily Exposure and Total Exposure Points
 * Updates Exposure Warning and Specific Controls to Consider
 */

  $('#calc-daily-exposure').click(function () {

    let dailyExposure = calculateDailyExposure();
    calculateTotalExposurePoints();
    updateExposureWarnings(dailyExposure);
  });
});

/**
 * Pushes the partial exposure magnitude from the users calculator table into an array.
 * Then calculates the daily exposure from this information.
 */
function calculateDailyExposure() {

  let partialExposure = [];

  // Source: https://stackoverflow.com/questions/50850109/create-array-from-specific-classes-texts

  $('.partial-exposure').each(function(){
    partialExposure.push($(this).text());
  });

  let dailyExposure = 0;

  for (let i = 0; i < partialExposure.length; i++) {
    dailyExposure += Math.pow(partialExposure[i], 2);
  }

  dailyExposure = Math.sqrt(dailyExposure);
  dailyExposure = Math.round(dailyExposure * 10) / 10;

  $('#daily-exposure').text(dailyExposure);

  return dailyExposure;

}

/**
 * Pushes the partial exposure points from the users calculator table into an array.
 * Then calculates the total exposure points from this information.
 */
function calculateTotalExposurePoints() {

  let partialExposurePts = [];

  $('.partial-exposure-pts').each(function(){
    partialExposurePts.push($(this).text());
  });

  let dailyExposurePts = 0;

  for (let i = 0; i < partialExposurePts.length; i++) {
    dailyExposurePts += Number(partialExposurePts[i]);
  }

  $('#daily-exposure-pts').text(dailyExposurePts);

}

/**
 * Displays information in "Exposure Warning" and "EAV/ELV Specific Control Measures to Consider"
 * on the users calculator, once the daily exposure is calculated
 */
function updateExposureWarnings(dailyExposure) {

  if (dailyExposure > 5) {
    $('#exposure-warning').text(aboveELVWarning);
    $('#exposure-warning').css("background-color", "red");
    $('#specific-controls').html(aboveELVControls);
  } else if (dailyExposure > 2.5) {
    $('#exposure-warning').text(aboveEAVWarning);
    $('#exposure-warning').css("background-color", "yellow");
    $('#specific-controls').html(aboveEAVControls);
  } else if (dailyExposure < 2.5) {
    $('#exposure-warning').text(belowEAVWarning);
    $('#exposure-warning').css("background-color", "lime");
    $('#specific-controls').html(belowEAVControls);
  }

}
 