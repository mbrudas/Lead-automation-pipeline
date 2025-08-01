/**
 * Trigger function that runs on form submission.
 * Captures new lead data, validates essential fields,
 * and stores it in the 'Customers' sheet.
 */
function onFormSubmit(e) {
  const sheetName = 'Customers';
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName(sheetName);

  if (!sheet) {
    throw new Error(`Sheet '${sheetName}' not found.`);
  }

  const formData = e.values;

  // Simple validation
  const name = formData[1];
  const email = formData[2];
  const phone = formData[3];

  if (!name || !email.includes('@')) return; // skip invalid entries

  // Append validated data
  sheet.appendRow([new Date(), name, email, phone]);
}

/**
 * Installable trigger setup function.
 * Run this once manually to enable the automation.
 */
function createTrigger() {
  const ss = SpreadsheetApp.getActive();
  ScriptApp.newTrigger('onFormSubmit')
    .forSpreadsheet(ss)
    .onFormSubmit()
    .create();
}
