// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $dateInput = document.querySelector("#date");
var $dateSearchBtn = document.querySelector("#dateSearch");
// Add an event listener to the searchButton, call handleDateSearchButtonClick when clicked
$dateSearchBtn.addEventListener("click", handleDateSearchButtonClick);

// Set filteredAddresses to addressData initially
var filteredUFO = dataSet;

// renderTable renders the filteredAddresses to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filteredUFO.length; i++) {
    // Get get the current address object and its fields
    var address = filteredUFO[i];
    var fields = Object.keys(address);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the address object, create a new cell at set its inner text to be the current value at the current address's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = address[field];
    }
  }
};

function handleDateSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterDate = $dateInput.value.trim();
  // Set filteredAddresses to an array of all addresses whose "state" matches the filter
  filteredUFO = dataSet.filter(function(address) {
    var ufoDate = address.datetime;

    // If true, add the address to the filteredAddresses, otherwise don't add it to filteredAddresses
    return ufoDate === filterDate;
  });
  renderTable();
}
// Render the table for the first time on page load
renderTable();